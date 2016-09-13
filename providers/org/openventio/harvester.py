import logging
import json

import requests
import arrow
from bs4 import BeautifulSoup

from share import Harvester

logger = logging.getLogger(__name__)

class OpenventioHarvester:
# class OpenventioHarvester(Harvester):
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        self.base_url = 'http://openventio.org/'
        self.journals = {
            # Many of the publications don't have issues yet
            'Archive/PulmonaryResearchandRespiratoryMedicine.php': 'PRRMOJ',
            # 'Archive/Anthropology.php': 'ANTPOJ',
            'Archive/Dermatology.php': 'DRMTOJ',
            'Archive/DiabetesResearch.php': 'DROJ',
            # 'Archive/PathologyandLaboratoryMedicine.php': 'PLMOJ',
            'Archive/ObesityResearch.php': 'OROJ',
            'Archive/GynecologyandObstetricsResearch.php': 'GOROJ',
            'Archive/PsychologyandCognitiveSciences.php': 'PCSOJ',
            # 'Archive/SocialBehaviorResearchandPractice.php': 'SBRPOJ',
            'Archive/LiverResearch.php': 'LROJ',
            # 'Archive/Radiology.php': 'ROJ',
            'Archive/CancerStudiesandMolecularMedicine.php': 'CSMMOJ',
            # 'Archive/TrichologyandCosmetology.php': 'TCOJ',
            'Archive/HeartResearch.php': 'HROJ',
            # 'Archive/InternalMedicine.php': 'IMOJ', 'Archive/EmergencyMedicine.php': 'EMOJ',
            'Archive/PalliativeMedicineandHospiceCare.php': 'PMHCOJ',
            'Archive/AdvancesInFoodTechnologyandNutritionSciences.php': 'AFTNSOJ',
            'Archive/SportsandExerciseMedicine.php': 'SEMOJ',
            # 'Archive/OrthopedicsResearchandTraumatology.php': 'ORTOJ',
            # 'Archive/Ophthalmology.php': 'OOJ',
            # 'Archive/VeterinaryMedicine.php': 'VMOJ',
            'Archive/Neuro.php': 'NOJ',
            # 'Archive/VaccinationResearch.php': 'VROJ',
            'Archive/SurgicalResearch.php': 'SROJ',
            'Archive/PublicHealth.php': 'PHOJ',
            'Archive/Gastro.php': 'GOJ',
            'Archive/Otolaryngology.php': 'OTLOJ',
            # 'Archive/OsteologyandRheumatology.php': 'ORHOJ',
            'Archive/PediatricsandNeonatalNursing.php': 'PNNOJ',
            'Archive/WomensHealth.php': 'WHOJ',
            # 'Archive/ClinicalTrialsandPractice.php': 'CTPOJ',
            'Archive/HIVAIDSResearchandTreatment.php': 'HARTOJ',
            # 'Archive/Anesthesiology.php': 'AOJ',
            'Archive/Dentistry.php': 'DOJ',
            'Archive/Pancreas.php': 'POJ',
            'Archive/Nephrology.php': 'NPOJ',
            # 'Archive/UrologyandAndrology.php': 'UAOJ',
            # 'Archive/ToxicologyandForensicMedicine.php': 'TFMOJ',
            # 'Archive/Epidemiology.php': 'EPOJ'
            }

    # TODO: date sorting, put it all together

    def do_harvest(self, start_date: arrow.Arrow, end_date: arrow.Arrow):
        for journal in self.journals:
            journal_issues = self.get_publication_issues(journal)
            print('journal', journal_issues)
            for issue in journal_issues:
                print('issue', issue)
                works = self.fetch_records(issue)
                for work in works:
                    print('work', work)
                    # yield self.fetch_page(work)
        return

    def get_publication_issues(self, journal):
        """
        :param journal: The URL for a journal's archive (from self.journals)
        :return: List of URLs for individual issues
        """
        r = requests.get(self.base_url + journal)

        # Several journals have no issues yet
        if r.status_code != 200:
            logger.warning("Publication {} has no works yet.".format(journal))
            return []

        soup = BeautifulSoup(r.text, 'html.parser')

        issues = [x.text.replace('../', '') for x in soup.select('div > p > a')]
        return issues

    def fetch_records(self, issue):
        """
        :param issue: URL for a single issue
        :return: List of DOIs for an issue of a publication
        """
        r = requests.get(self.base_url + issue)
        soup = BeautifulSoup(r.text, 'html.parser')

        article_dois = [x.text.replace(' ', '') for x in soup.select('p a strong')]

        return article_dois

    def fetch_page(self, url):
        r = requests.Session().get(url, headers={'Accept': 'application/json'})
        try:
            j = json.loads(r.text)
            return j['DOI'], j
        except:
            logging.warning("{} is not a valid url".format(url))

h = OpenventioHarvester()
for p in h.get_publication_issues(''):
    print(p)