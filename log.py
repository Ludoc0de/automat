import requests
import config
from bs4 import BeautifulSoup

login_url = ("https://frontendmasters.com/login/")
dashboard_url = ("https://frontendmasters.com/dashboard/")

# # Création d'une session pour conserver les cookies
session = requests.session()

# # Obtenir la page de connexion pour récupérer les cookies et éventuellement des tokens CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

# # Rechercher le token CSRF (le nom du champ peut varier en fonction du site)
# csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

headers = {
    "Referer": login_url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

payload = {
    "username": config.USERNAME,
    "password": config.PASSWORD,
    # "csrfmiddlewaretoken": csrf_token
}

login_response = session.post(login_url, data=payload, headers=headers)
# print(login_response.text)

dashboard_response = session.get(dashboard_url)
print(dashboard_response.text[:5000])

# Vérifier si vous êtes redirigé vers la page de connexion ou si le tableau de bord est affiché
if "Logout" in dashboard_response.text or "My Home" in dashboard_response.text:
    print("Connexion réussie, accès au tableau de bord")
else:
    print("Échec de la connexion, redirection vers la page de connexion")