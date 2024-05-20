# coding=utf-8
import globalPluginHandler
import ui
import api
import urllib.request
import json

# Replace with your actual API key
api_key = "7b24650c2e2e410dbd63106f665ad992"

# Set the request URL and headers
url = "https://api.football-data.org/v4/matches"
headers = {
    "X-Auth-Token": api_key
}
req = urllib.request.Request(url, headers=headers)

class FootballScoreAnnouncer(globalPluginHandler.GlobalPlugin):
    description = "Announces the latest football scores"
    scriptCategory = "Football Score Announcer"

    def script_announceScores(self, gesture):
        try:
            # Make the API request
            response = urllib.request.urlopen(req)
            data = json.loads(response.read().decode())

            # Extract the relevant score information from the API response
            scores = []
            for match in data["matches"]:
                home_team = match["home_team"]["name"]
                away_team = match["away_team"]["name"]
                home_score = match["home_team"]["score"]
                away_score = match["away_team"]["score"]
                scores.append(f"{home_team} {home_score} - {away_score} {away_team}")

            # Announce the scores
            ui.message(" | ".join(scores))
        except Exception as e:
            ui.message(f"Error: {str(e)}")

    __gestures = {
        "kb:NVDA+Shift+S": "announceScores",
    }