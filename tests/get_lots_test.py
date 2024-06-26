import unittest
from funpay_scrapper.lots import Lots

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.lots = Lots(2027)

    def test_get_profile_info(self):
        self.assertEqual(self.lots.lots_links(), {})
        self.assertEqual(self.lots.sort_lots(), {})

if __name__ == '__main__':
    unittest.main()