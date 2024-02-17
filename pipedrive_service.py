import json
from typing import Optional, List

import requests

from static import config
from static.config import Config

config = Config()

url = f"https://api.pipedrive.com/v1/deals?api_token={config.api_pipedrive_token}&sort=id DESC&limit=500"


headers = {
    "Accept": "application/json"
}

def get_data():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        return json_response['data']
    else:
        return None


def mark_as_sent_country(id):
    print(f"request 'mark_as_sent_country' start id -> {id}")
    try:

        uri = f"https://api.pipedrive.com/v1/deals/{id}?api_token={config.API_PIPEDRIVE}"

        data = {
            '6b12c94620ef88cea439f652fc648e4b5036ef2f': "Wystaw"
           # '6b12c94620ef88cea439f652fc648e4b5036ef2f': "Wysłana"
        }

        response = requests.put(uri, json=data)
        print(f"request 'mark_as_sent_country' success id -> {id}")
        return response
    except:
        print(f"request 'mark_as_sent_country' fail id -> {id}")

def mark_as_sent_in_foreign_currency(id):
    print(f"request 'mark_as_sent_in_foreign_currency' start id -> {id}")
    try:

        uri = f"https://api.pipedrive.com/v1/deals/{id}?api_token={config.API_PIPEDRIVE}"

        data = {
            "5f784ebfd4428d6e26e2af34d67b268f6b22ca0f": "Wysłana"
        }

        response = requests.put(uri, json=data)
        print(f"request 'mark_as_sent_in_foreign_currency' success id -> {id}")
        return response
    except:
        print(f"request 'mark_as_sent_in_foreign_currency' fail id -> {id}")