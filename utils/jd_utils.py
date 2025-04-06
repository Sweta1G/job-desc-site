import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return '\n'.join([p.get_text() for p in paragraphs])
    except Exception as e:
        return f"Error extracting text: {e}"
