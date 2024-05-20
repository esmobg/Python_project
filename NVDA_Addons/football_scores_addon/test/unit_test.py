import unittest
import urllib.request
import json

class TestFootballAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = "7b24650c2e2e410dbd63106f665ad992"
        self.url = "https://api.football-data.org/v4/matches"
        self.headers = {
            "X-Auth-Token": self.api_key
        }
        self.req = urllib.request.Request(self.url, headers=self.headers)

    def test_api_key(self):
        # Проверка дали API ключът е валиден
        try:
            response = urllib.request.urlopen(self.req)
            data = json.loads(response.read().decode())
            self.assertTrue("matches" in data)
        except urllib.error.HTTPError as e:
            self.fail(f"API key is invalid: {e}")

    def test_response_data(self):
        # Проверка дали отговорът от API съдържа очакваните данни
        try:
            response = urllib.request.urlopen(self.req)
            data = json.loads(response.read().decode())
            self.assertIsInstance(data, dict)
            self.assertIsInstance(data["matches"], list)
            self.assertTrue(len(data["matches"]) > 0)
            match = data["matches"][0]
            self.assertIn("home_team", match)
            self.assertIn("away_team", match)
            self.assertIn("score", match["home_team"])
            self.assertIn("score", match["away_team"])
        except Exception as e:
            self.fail(f"Error in API response: {e}")

if __name__ == "__main__":
    unittest.main()