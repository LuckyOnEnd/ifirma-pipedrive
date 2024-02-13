import json
from typing import Optional, List

import requests

api_token = "7519a95a31dc3cbc342b55d742201075c38f533b"
url = f"https://api.pipedrive.com/v1/deals?api_token={api_token}&sort=id DESC&limit=20"


headers = {
    "Accept": "application/json"
}

def get_data():
    response = requests.get(url, headers=headers)

    # Проверяем успешность запроса
    if response.status_code == 200:
        json_response = response.json()
        return json_response['data']
    else:
        return None


def mark_as_sent(id):
    uri = f"https://api.pipedrive.com/v1/deals/{id}?api_token=7519a95a31dc3cbc342b55d742201075c38f533b"

    data = {
        "5f784ebfd4428d6e26e2af34d67b268f6b22ca0f": "Wysłana"
    }

    print(f"mark as sent reuqest {id}")
    response = requests.put(uri, json=data)
    print(f"mark as sent success {id}")
    return response
