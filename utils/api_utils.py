import requests


class APIUtils:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_products(self):
        response = requests.get(f"{self.base_url}/products")
        return response