import json
import logging

import pendulum

from share import Harvester

logger = logging.getLogger(__name__)


class UNCHarvester(Harvester):
    url = 'https://cdr.lib.unc.edu/services/api/search/'
    sets = [
        'uuid:91c587a8-439f-4b96-bf12-9f2115153e39',
        'uuid:ce342a89-d33e-4ddd-b8f1-6c09743b48e7',
        'uuid:bded4944-f033-4015-af0f-3d39595f4d30',
        'uuid:4ed9c5df-efe2-4066-9df8-ef64548a6257',
        'uuid:1add9fbc-f5c4-49a8-848e-96a52e3ade9c',
        'uuid:1d4673ac-3475-4200-880c-022c3c3ed1cd',
        'uuid:51cf6d7e-5f96-4946-b3da-2e67366c5696',
        'uuid:18e1a42e-b113-4b88-adea-179e73e099ce',
        'uuid:dfebbdf7-3361-4097-9fa4-7001ab6fcc11',
        'uuid:043d68c6-d7ba-43f1-8c06-2bd25e94510a',
        'uuid:de6c470c-eba2-46a3-970d-a0c71bff4104',
        'uuid:48d45480-1d70-4e03-a184-1a3687153413',
        'uuid:6b0f68d5-2af4-4dbb-bf2e-b2d885ba1999',
        'uuid:8e6cb1d6-ed77-446f-8b1e-9ead911c9584',
        'uuid:cbbc2cc1-c538-4e28-b567-55db61b7942e',
        'uuid:91b45bd3-18d6-4dc2-a6b5-67f345cdf8ef',
        'uuid:bce46b81-6d8f-48cc-8e9b-bbdf8c5a9724',
        'uuid:0c4a01a5-f8b6-4b4c-93e7-846c61d8e327',
        'uuid:740571bc-c72b-43fa-a1b7-b5cf9b198c61',
        'uuid:b803dc0a-6952-47f8-97ee-9bd56947e443',
    ]

    def do_harvest(self, start_date: pendulum.Pendulum, end_date: pendulum.Pendulum):
        # start_date = start_date.date()
        # end_date = end_date.date()
        return self.fetch_records(self.sets, start_date, end_date)

    def fetch_records(self, lst, start_date, end_date):
        for item in lst:
            records = self.fetch_page(self.url + item)
            for record in records:
                # There are collections and folders inside of collections and folders
                if record['type'] != 'File':
                    self.fetch_records([record['type']], start_date, end_date)
                else:
                    # They aren't ordered by time
                    if pendulum.parse(record['added']) < start_date:
                        continue
                    if pendulum.parse(record['added']) > end_date:
                        continue
                    yield (record['id'], record)



    def fetch_page(self, url):

        logger.info('Making request to {}'.format(url))
        r = self.requests.get(url)
        results = json.loads(r.text)['results']

        logger.info('Found {} records.'.format(len(results)))

        return results
