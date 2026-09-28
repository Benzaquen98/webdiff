import requests



def fetch_page(url):
    response = requests.get(url, timeout=10)
    return response
