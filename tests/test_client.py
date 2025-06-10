import dotenv
import os
import process_street
import unittest

dotenv.load_dotenv("../.local/.env")
PRST_API_KEY = os.getenv("PRST_API_KEY")


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = process_street.ProcessStreetClient(PRST_API_KEY)

    def test_api_key(self):
        self.assertEqual(self.client.api_key, PRST_API_KEY)

    def test_get_data_sets(self):
        response = self.client.get_data_sets()
        self.assertIn("dataSets", response)

    def test_get_test_auth(self):
        response = self.client.get_test_auth()
        self.assertIn("apiKeyLabel", response)
