def get_currency_template(current_date, currency, price,
                          title, fullname, nip, ulica, postal_code, country, city):
    return {
                "TypSprzedazy": "KRAJOWA",
                "ZaplaconoNaDokumencie": 0,
                "Zaplacono": 0,
                "LiczOd": "BRT",
                "NumerKontaBankowego": "PL57102049000000890230925632",
                "DataWystawienia": current_date,
                "MiejsceWystawienia": "POZNAŃ",
                "DataSprzedazy": current_date,
                "FormatDatySprzedazy": "DZN",
                "SposobZaplaty": "PRZ",
                "Jezyk": "en",
                "Waluta": "USD",
                "KursWalutyWidoczny": False,
                "KursWalutyZDniaPoprzedzajacegoDzienWystawieniaFaktury": currency,
                "RodzajPodpisuOdbiorcy": "BPO",
                "WidocznyNumerGios": False,
                "WidocznyNumerBdo": False,
                "Numer": None,
                "Pozycje": [
                    {
                        "StawkaVat": 0.00,
                        "Ilosc": 1,
                        "CenaJednostkowa": price,
                        "NazwaPelna": f"Fracht morski - Rotterdam: {title}",
                        "Jednostka": "szt",
                        "TypStawkiVat": "PRC"
                    }
                ],
                "Kontrahent": {
                    "Nazwa": fullname,
                    "NIP": nip,
                    "Ulica": ulica,
                    "KodPocztowy": postal_code,
                    "Kraj": country,
                    "Miejscowosc": city,
                }
            }

def get_country_template(current_date, price,
                          title, fullname, nip, ulica, postal_code, country, city, email):
    return {
                "Zaplacono": 0,
                "NumerKontaBankowego": "40102052420000240204694057",
                "DataWystawienia": current_date,
                "MiejsceWystawienia": "WROCŁAW",
                "DataSprzedazy": current_date,
                "FormatDatySprzedazy": "DZN",
                "SposobZaplaty": "PRZ",
                "WpisDoKpir": "NIE",
                "Numer": None,
                "Pozycje": [
                    {
                        "Ilosc": 1,
                        "CenaJednostkowa": price,
                        "NazwaPelna": f"Prowizja za organizacje importu pojazdu z USA: {title}",
                        "Jednostka": "szt.",
                    }
                ],
                "Kontrahent": {
                    "Nazwa": fullname,
                    "Ulica": ulica,
                    "KodPocztowy": postal_code,
                    "Kraj": country,
                    "Miejscowosc": city,
                    "Email": email
                }
    }