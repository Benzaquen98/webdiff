from urllib.parse import urljoin

from bs4 import BeautifulSoup


def extract_scripts(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script", src=True)

    sources = []

    for script in scripts:
        source = urljoin(base_url, script["src"])
        sources.append(source)

    return sources


def extract_stylesheets(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    stylesheets = soup.find_all("link", rel="stylesheet", href=True)

    sources = []

    for stylesheet in stylesheets:
        source = urljoin(base_url, stylesheet["href"])
        sources.append(source)

    return sources

def extract_assets(html, base_url):
    return {
        "javascript": extract_scripts(html, base_url),
        "css": extract_stylesheets(html, base_url),
    }
