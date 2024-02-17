import time
from datetime import datetime
import requests
import pipedrive_service
from services.ifirma_service import get_invoice_by_id, \
    send_in_foreign_currency_mail, create_in_country_invoice, create_in_foreign_currency_invoice
from static.invoice_template import get_currency_template, get_country_template

pipeservice = pipedrive_service

def create_new_invoice(products, currency):
    for product in products:
        nip = ""
        if product['e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_subpremise'] == None:
            nip = ""
        else:
            nip = product['e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_subpremise']
        ulica = ""
        if product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_route"] == None and product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_street_number"] == None:
            if product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91"] != None:
                ulica = product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91"].split(",")[0]
        else:
            ulica = f'{product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_route"]} {product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_street_number"]}'

        if product['id'] == 473:
            invoice_model = get_currency_template(
                        current_date=datetime.now().strftime("%Y-%m-%d"),
                        currency=currency,
                        price=product['463274f945608f73a35db47670b946186f723386'],
                        title=product['title'],
                        fullname=product['8edef253a2dab4c978cca356b4ca689b8d089634'],
                        nip=nip,
                        ulica=ulica,
                        postal_code=product['e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_postal_code'],
                        country=product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_country"],
                        city=product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_locality"]
                    ),
            status, new_invoice = create_in_foreign_currency_invoice(invoice_model)
        #if product['6b12c94620ef88cea439f652fc648e4b5036ef2f'] == "46":
            invoice_model = get_country_template(
                current_date=datetime.now().strftime("%Y-%m-%d"),
                price=product['463274f945608f73a35db47670b946186f723386'],
                title=product['title'],
                fullname=product['8edef253a2dab4c978cca356b4ca689b8d089634'],
                nip=nip,
                ulica=ulica,
                postal_code=product['e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_postal_code'],
                country=product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_country"],
                city=product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_locality"],
                email=product["person_id"]["email"][0]["value"]
            ),
            print("create foreign currency invoice")
            status, new_invoice = create_in_country_invoice(invoice_model)
            if status == 0:
                invoice_nr, price = get_invoice_by_id(new_invoice)
                send_in_foreign_currency_mail(product["person_id"]["email"][0]["value"], new_invoice, invoice_nr, price, product['10cb2dd06a7a60d9d9e19bd3819a6569ffb208c1'], product['5073621992b2b327ea4ca4733833c97af8aadc4e'],product['199cc63d9c8efe4d49249d9a7e97318015d8cb10'], product['4f14897cef15702d7cf7583bea70e89bafa36646'])
                pipedrive_service.mark_as_sent_country(product["id"])

        # if product['5f784ebfd4428d6e26e2af34d67b268f6b22ca0f'] == "45":
        #     invoice_model = get_currency_template(
        #         current_date=datetime.now().strftime("%Y-%m-%d"),
        #         currency=currency,
        #         price=product['463274f945608f73a35db47670b946186f723386'],
        #         title=product['title'],
        #         fullname=product['8edef253a2dab4c978cca356b4ca689b8d089634'],
        #         nip=nip,
        #         ulica=ulica,
        #         postal_code=product['e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_postal_code'],
        #         country=product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_country"],
        #         city=product["e134f8360b17a18963ca6ea8cfaa7e0b156b7f91_locality"]
        #     ),
        #     print("create country invoice")
        #     status, new_invoice = create_invoice(invoice_model)
        #     if status == 0:
        #         invoice_nr, price = get_invoice_by_id(new_invoice)
        #         send_mail(product["person_id"]["email"][0]["value"], new_invoice, invoice_nr, price, product['10cb2dd06a7a60d9d9e19bd3819a6569ffb208c1'], product['5073621992b2b327ea4ca4733833c97af8aadc4e'],product['199cc63d9c8efe4d49249d9a7e97318015d8cb10'], product['4f14897cef15702d7cf7583bea70e89bafa36646'])
        #         pipedrive_service.mark_as_sent_in_foreign_currency(product["id"])


while True:
    try:
        #time.sleep(20)
        product_to_create_invoice = pipeservice.get_data()

        if len(product_to_create_invoice) > 0:
            print("get currency started")
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            responseObject = response.json()
            currency = responseObject['rates']['PLN']
            print("get currency finished")
            create_new_invoice(product_to_create_invoice, currency)
    except Exception as ex:
        print(ex.args)
        time.sleep(10)
        continue
