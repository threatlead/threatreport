# from .context import crowdstrike
from ..threatreport import crowdstrike, securelist, unit42
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_crowdstrike_latest(self):
        articles = crowdstrike.CrowdStrike.get_latest()
        self.assertEqual(len(articles), 10, 'Found a total of {0} CrowdStrike articles on a page'.format(len(articles)))

    def test_crowdstrike_get_article(self):
        test_url = 'https://www.crowdstrike.com/blog/doppelpaymer-ransomware-and-dridex-2/'
        articles = crowdstrike.CrowdStrike.CrowdStrikeArticle(url=test_url)
        self.assertEqual(len(articles.authors), 3, 'CrowdStrike Test Failed on Author Count')

    def test_securelist_latest(self):
        articles = securelist.Securelist.get_latest()
        self.assertEqual(len(articles), 10, 'Found a total of {0} Securelist articles on a page'.format(len(articles)))

    def test_securelist_get_article(self):
        test_url = 'https://securelist.com/sodin-ransomware/91473/'
        articles = securelist.Securelist.SecurelistArticle(url=test_url)
        self.assertEqual(len(articles.authors), 3, 'Securelist Test Failed on Author Count')

    def test_unit42_latest(self):
        articles = unit42.Unit42.get_latest()
        self.assertEqual(len(articles), 15, 'Found a total of {0} Unit42 articles on a page'.format(len(articles)))

    def test_unit42_get_article(self):
        test_url = 'https://unit42.paloaltonetworks.com/evasion-of-security-policies-by-vpn-clients-poses-great-risk-to-network-operators/'
        articles = unit42.Unit42.Unit42Article(url=test_url)
        self.assertEqual(len(articles.authors), 2, 'Unit42 Test Failed on Author Count')


if __name__ == '__main__':
    unittest.main()
