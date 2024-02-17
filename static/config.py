
class Config:
    def __init__(self):
        self.api_pipedrive_token = "7519a95a31dc3cbc342b55d742201075c38f533b"
        self.api_ifirma_country_token = "0FB0456A7BD7B3A4"
        self.api_ifirma_in_foreign_currency = "49311F4D221B0E63"

    def get_pipedrive_key(self) -> str:
        return self.api_pipedrive_token

    def get_ifirma_key_country(self) -> str:
        return "0FB0456A7BD7B3A4"

    def get_ifirma_key_in_foreign_currency(self) -> str:
        return self.api_ifirma_in_foreign_currency
