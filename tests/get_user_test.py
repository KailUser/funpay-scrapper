import unittest
from funpay_scraper.profile import Profile

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.profile = Profile(5682424)

    def test_get_profile_info(self):
        self.assertEqual(self.profile.nickname(), "Syirezz")
        self.assertEqual(self.profile.rating(), "?")
        self.assertEqual(self.profile.offers(), [])
        self.assertEqual(self.profile.url, "https://funpay.com/users/5682424/")

if __name__ == '__main__':
    unittest.main()