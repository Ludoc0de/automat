import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

login_url = ("https://b12.io/accounts/login/?next=/dashboard/")
# dashboard_url = ("")

# Création d'une session pour conserver les cookies
session = requests.Session()

# Obtenir la page de connexion pour récupérer les cookies et éventuellement des tokens CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

payload = {
    "username": "config.EMAIL",
    "password": "config.PASSWORD",
    "csrfmiddlewaretoken": "config.TOKENS"
}

login_response = session.post(login_url, data=payload)
print(login_response.text)
# requests_get = requests.get(dashboard_url)
# print(requests_get.text)