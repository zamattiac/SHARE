from share.provider import ProviderAppConfig
from .harvester import UNCHarvester


class AppConfig(ProviderAppConfig):
    name = 'providers.edu.unc'
    version = '0.0.1'
    title = 'Carolina Digital Repository'
    long_title = 'University of North Carolina at Chapel Hill Libraries'
    home_page = 'http://library.unc.edu/about/mission/'
    url = 'https://cdr.lib.unc.edu/services/api/search/'
    approved_sets = [
        '91c587a8-439f-4b96-bf12-9f2115153e39',
        'ce342a89-d33e-4ddd-b8f1-6c09743b48e7',
        'bded4944-f033-4015-af0f-3d39595f4d30',
        '4ed9c5df-efe2-4066-9df8-ef64548a6257',
        '1add9fbc-f5c4-49a8-848e-96a52e3ade9c',
        '1d4673ac-3475-4200-880c-022c3c3ed1cd',
        '51cf6d7e-5f96-4946-b3da-2e67366c5696',
        '18e1a42e-b113-4b88-adea-179e73e099ce',
        'dfebbdf7-3361-4097-9fa4-7001ab6fcc11',
        '043d68c6-d7ba-43f1-8c06-2bd25e94510a',
        'de6c470c-eba2-46a3-970d-a0c71bff4104',
        '48d45480-1d70-4e03-a184-1a3687153413',
        '6b0f68d5-2af4-4dbb-bf2e-b2d885ba1999',
        '8e6cb1d6-ed77-446f-8b1e-9ead911c9584',
        'cbbc2cc1-c538-4e28-b567-55db61b7942e',
        '91b45bd3-18d6-4dc2-a6b5-67f345cdf8ef',
        'bce46b81-6d8f-48cc-8e9b-bbdf8c5a9724',
        '0c4a01a5-f8b6-4b4c-93e7-846c61d8e327',
        '740571bc-c72b-43fa-a1b7-b5cf9b198c61',
        'b803dc0a-6952-47f8-97ee-9bd56947e443'
    ]
    harvester = UNCHarvester
