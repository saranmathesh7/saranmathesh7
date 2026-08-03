import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import json

USERNAME = "saranmathesh7"

url = f"https://github.com/users/{USERNAME}/contributions"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

days = soup.find_all("td", class_="ContributionCalendar-day")

contributions = []

for day in days:

    contributions.append({

        "date": day.get("data-date"),

        "level": day.get("data-level")

    })

with open("data/contributions.json", "w") as file:
    json.dump(contributions, file, indent=4)

print("Saved", len(contributions), "days")