from share.provider import OAIProviderAppConfig


class AppConfig(OAIProviderAppConfig):
    name = 'providers.edu.cornell'
    version = '0.0.1'
    title = 'cornell'
    long_title = 'Cornell University'
    home_page = 'https://ecommons.cornell.edu'
    url = 'https://ecommons.cornell.edu/dspace-oai/request'
    approved_sets = ['com_1813_35']
