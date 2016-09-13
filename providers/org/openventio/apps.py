from share.provider import ProviderAppConfig
from .harvester import OpenventioHarvester


class AppConfig(ProviderAppConfig):
    name = 'providers.org.openventio'
    version = '0.0.1'
    title = 'openventio'
    long_title = 'Openventio Publishers'
    home_page = 'http://openventio.org/'
    harvester = OpenventioHarvester
    emitted_type = 'publication'
