import abc
import time
import logging

import pendulum
from furl import furl
from lxml import etree

from .harvester import Harvester

logger = logging.getLogger(__name__)


class OAIHarvester(Harvester, metaclass=abc.ABCMeta):

    namespaces = {
        'dc': 'http://purl.org/dc/elements/1.1/',
        'ns0': 'http://www.openarchives.org/OAI/2.0/',
        'oai_dc': 'http://www.openarchives.org/OAI/2.0/',
    }
    url = None
    time_granularity = True

    def __init__(self, app_config):
        super().__init__(app_config)

        self.url = getattr(self.config, 'url', self.url)
        if not self.url:
            raise NotImplementedError('url')

        self.time_granularity = getattr(self.config, 'time_granularity', self.time_granularity)

    def do_harvest(self, start_date: pendulum.Pendulum, end_date: pendulum.Pendulum) -> list:
        url = furl(self.url)
        url.args['verb'] = 'ListRecords'
        url.args['metadataPrefix'] = 'oai_dc'

        if self.time_granularity:
            url.args['from'] = start_date.format('YYYY-MM-DDT00:00:00', formatter='alternative') + 'Z'
            url.args['until'] = end_date.format('YYYY-MM-DDT00:00:00', formatter='alternative') + 'Z'
        else:
            url.args['from'] = start_date.date().isoformat()
            url.args['until'] = end_date.date().isoformat()

        return self.fetch_records(url)

    def fetch_records(self, url: furl) -> list:
        records, token = self.fetch_page(url, token=None)

        while True:
            for record in records:
                yield (
                    record.xpath('ns0:header/ns0:identifier', namespaces=self.namespaces)[0].text,
                    etree.tostring(record),
                )

            records, token = self.fetch_page(url, token=token)

            if not token or not records:
                break

    def fetch_page(self, url: furl, token: str=None) -> (list, str):
        if token:
            url.remove('from')
            url.remove('until')
            url.remove('metadataPrefix')
            url.args['resumptionToken'] = token

        while True:
            logger.info('Making request to {}'.format(url.url))
            resp = self.requests.get(url.url)
            if resp.ok:
                break
            if resp.status_code == 503:
                sleep = int(resp.headers.get('retry-after', 5)) + 2  # additional 2 seconds for good measure
                logger.warning('Server responded with %s. Waiting %s seconds.', resp, sleep)
                time.sleep(sleep)
                continue
            resp.raise_for_status()

        parsed = etree.fromstring(resp.content)

        records = parsed.xpath('//ns0:record', namespaces=self.namespaces)
        token = (parsed.xpath('//ns0:resumptionToken/node()', namespaces=self.namespaces) + [None])[0]

        logger.info('Found {} records. Continuing with token {}'.format(len(records), token))

        return records, token
