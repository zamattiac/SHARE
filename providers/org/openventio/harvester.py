import logging
import json

import requests
import arrow
from bs4 import BeautifulSoup

from share import Harvester

logger = logging.getLogger(__name__)


# class OpenventioHarvester(Harvester):
class OpenventioHarvester:
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        self.base_url = 'http://openventio.org/'
        self.journals = {
            'Archive/PulmonaryResearchandRespiratoryMedicine.php': 'PRRMOJ',
            'Archive/Anthropology.php': 'ANTPOJ',
            'Archive/Dermatology.php': 'DRMTOJ',
            'Archive/DiabetesResearch.php': 'DROJ',
            'Archive/PathologyandLaboratoryMedicine.php': 'PLMOJ',
            'Archive/ObesityResearch.php': 'OROJ',
            'Archive/GynecologyandObstetricsResearch.php': 'GOROJ',
            'Archive/PsychologyandCognitiveSciences.php': 'PCSOJ',
            'Archive/SocialBehaviorResearchandPractice.php': 'SBRPOJ',
            'Archive/LiverResearch.php': 'LROJ', 'Archive/Radiology.php': 'ROJ',
            'Archive/CancerStudiesandMolecularMedicine.php': 'CSMMOJ',
            'Archive/TrichologyandCosmetology.php': 'TCOJ', 'Archive/HeartResearch.php': 'HROJ',
            'Archive/InternalMedicine.php': 'IMOJ', 'Archive/EmergencyMedicine.php': 'EMOJ',
            'Archive/PalliativeMedicineandHospiceCare.php': 'PMHCOJ',
            'Archive/AdvancesInFoodTechnologyandNutritionSciences.php': 'AFTNSOJ',
            'Archive/SportsMedicine.php': 'SEMOJ',
            'Archive/OrthopedicsResearchandTraumatology.php': 'ORTOJ',
            'Archive/Ophthalmology.php': 'OOJ', 'Archive/VeterinaryMedicine.php': 'VMOJ',
            'Archive/Neuro.php': 'NOJ', 'Archive/VaccinationResearch.php': 'VROJ',
            'Archive/SurgicalResearch.php': 'SROJ', 'Archive/PublicHealth.php': 'PHOJ',
            'Archive/Gastro.php': 'GOJ', 'Archive/Otolaryngology.php': 'OTLOJ',
            'Archive/OsteologyandRheumatology.php': 'ORHOJ',
            'Archive/PediatricsandNeonatalNursing.php': 'PNNOJ', 'Archive/WomensHealth.php': 'WHOJ',
            'Archive/ClinicalTrialsandPractice.php': 'CTPOJ',
            'Archive/HIVAIDSResearchandTreatment.php': 'HARTOJ', 'Archive/Anesthesiology.php': 'AOJ',
            'Archive/Dentistry.php': 'DOJ', 'Archive/Pancreas.php': 'POJ',
            'Archive/Nephrology.php': 'NPOJ', 'Archive/UrologyandAndrology.php': 'UAOJ',
            'Archive/ToxicologyandForensicMedicine.php': 'TFMOJ', 'Archive/Epidemiology.php': 'EPOJ'
            }

    def do_harvest(self, start_date: arrow.Arrow, end_date: arrow.Arrow):
        return

    def get_publication_issues(self, journal):
        """
        :param journal: The URL for a journal's archive (from self.journals)
        :return: List of URLs for individual issues
        """
        r = requests.get(self.base_url + journal)

        # Several journals have no issues yet
        if r.status_code != 200:
            return

        soup = BeautifulSoup(r.text, 'html.parser')

        issues = [x.get('href').replace('../', '') for x in soup.select('div.arc1 > a')]
        return issues

    def fetch_records(self, issue):
        """
        :param issue: URL for a single issue
        :return: List of creative work DOIs
        """
        r = requests.get(self.base_url + issue)
        soup = BeautifulSoup(r.text, 'html.parser')

        article_dois = [x.text for x in soup.select('p a strong')]

        for article_doi in article_dois:
            yield self.fetch_page(article_doi)

    def fetch_page(self, url):
        r = requests.Session().get(url, headers={'Accept': 'application/json'})
        j = json.loads(r.text)
        return j['DOI'], j


harvester = OpenventioHarvester()
print(harvester.fetch_records('CurrentIssue/CancerStudiesandMolecularMedicine.php'))
