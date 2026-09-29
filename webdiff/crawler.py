import requests


class FetchError(Exception):
    pass


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        return response
    except requests.RequestException as error:
        raise FetchError(f"Unable to fetch {url}") from error
