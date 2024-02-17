import json
from datetime import datetime

import requests

from static import email_template
from static.config import Config

config = Config()

def sign_raw(data, key):
    import hmac
    from binascii import unhexlify
    from hashlib import sha1

    api_key = key if isinstance(key, bytes) else unhexlify(key)
    bin_data = data.encode(encoding="utf-8", errors="strict")

    return hmac.new(api_key, bin_data, sha1).hexdigest()

def create_in_foreign_currency_invoice(data):
    try:
        username = "nikodem.pawlowski@me.com"
        api_token = config.api_ifirma_in_foreign_currency
        url = "https://www.ifirma.pl/iapi/fakturawaluta.json"

        json_content = json.dumps(data, ensure_ascii=False)
        sign_data = f"{url}{username}faktura{json_content or ''}"

        hashWiadomosci = sign_raw(sign_data, api_token)

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json; charset=UTF-8',
            'Authentication': f"IAPIS user={username}, hmac-sha1={hashWiadomosci}"
        }

        print("create invoce post")
        response = requests.post(url, data=json_content.encode('utf-8'), headers=headers)
        print("create invoce send")
        data_response = response.json()
        result = data_response['response']
        if result["Kod"] == 0:
            identyficator = result["Identyfikator"]
            print(f"create invoce identyfikator {identyficator}")
            return 0, (int)(identyficator)
        else:
            print(f"create invoce error")
            return 500, 0
    except Exception as e:
        return 500, 0

def get_invoice_by_id(id):
    username = "nikodem.pawlowski@me.com"
    api_token = config.api_ifirma_country_token
    url = f"https://www.ifirma.pl/iapi/faktury.json"

    sign_data = f"{url}{username}faktura"

    hashWiadomosci = sign_raw(sign_data, api_token)
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json; charset=UTF-8',
        'Authentication': f"IAPIS user={username}, hmac-sha1={hashWiadomosci}"
    }

    print("get invoice by id reuqest send")
    response = requests.get(f"{url}?dataOd={datetime.now().strftime('2024-02-12')}", headers=headers)
    print("get invoice by id reuqest success")
    data = response.json()
    for invoice in data['response']['Wynik']:
        if invoice['FakturaId'] == id:
            print("get invoice by id , invoice found")
            return invoice['PelnyNumer'], invoice['Brutto']

    return None, None

def send_in_foreign_currency_mail(email, invoice_number, invoice_nr, price, freightInsure, freight, broker, last_price):
    template = email_template.value()
    email_content = template.format(
        numer_faktury=f'{invoice_nr}',
        kwota=f'{price}',
        usluga_brokera=f'{broker}USD',
        odbior_frachtu=f'{freight}USD',
        ubezpieczenie_cargo=f'{freightInsure}USD',
        oplata=f'{last_price}USD'
    )

    email_url = "https://www.ifirma.pl/iapi/fakturawaluta/send"
    username = "nikodem.pawlowski@me.com"
    api_token = config.api_ifirma_country_token

    url = f"{email_url}/{invoice_number}.json?wyslijEfaktura=true"

    data = {
        "Tekst": email_content,
        "SkrzynkaEmail": "app@spautomotive.pl",
        "SzablonEmail": "Pusty",
        "SkrzynkaEmailOdbiorcy": email
    }

    json_content = json.dumps(data, ensure_ascii=False)

    base_url = url.split("?")[0]
    sign_data = f"{base_url}{username}faktura{json_content or ''}"

    hashWiadomosci = sign_raw(sign_data, api_token)

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json; charset=UTF-8',
        'Authentication': f"IAPIS user={username}, hmac-sha1={hashWiadomosci}"
    }

    print(f"send email {invoice_number} {invoice_nr}")
    requests.post(url, data=json_content.encode('utf-8'), headers=headers)
    print(f"send email success {invoice_number} {invoice_nr}")

def create_in_country_invoice(data):
    try:
        username = "michal@spautomotive.pl"
        api_token = "0FB0456A7BD7B3A4"
        url = "https://www.ifirma.pl/iapi/rachunekkraj.json"

        json_content = json.dumps(data, ensure_ascii=False)
        sign_data = f"{url}{username}rachunek{json_content or ''}"

        hashWiadomosci = sign_raw(sign_data, api_token)

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json; charset=UTF-8',
            'Authentication': f"IAPIS user={username}, hmac-sha1={hashWiadomosci}"
        }

        print("create invoce post")
        response = requests.post(url, data=json_content.encode('utf-8'), headers=headers)
        print("create invoce send")
        data_response = response.json()
        result = data_response['response']
        if result["Kod"] == 0:
            identyficator = result["Identyfikator"]
            print(f"create invoce identyfikator {identyficator}")
            return 0, (int)(identyficator)
        else:
            print(f"create invoce error")
            return 500, 0
    except Exception as e:
        return 500, 0