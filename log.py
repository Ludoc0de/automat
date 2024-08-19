import requests
from bs4 import BeautifulSoup

login_url = ("https://frontendmasters.com/login/")

# # Création d'une session pour conserver les cookies
session = requests.Session()

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
    "email": "config.EMAIL",
    "password": "config.PASSWORD"
}

login_response = session.post(login_url, data=payload, headers=headers)
# print(login_response.text)

dashboard_url = ("https://frontendmasters.com/dashboard/")
dashboard_response = session.get(dashboard_url)
print("dashboard")
print(dashboard_response.text)

# # Vérifier si un cookie spécifique est présent après la connexion
# if "sessionid" in session.cookies:
#     print("Connexion réussie, session active")
# else:
#     print("Échec de la connexion, aucun cookie de session trouvé")

# # Vérifier si vous êtes redirigé vers la page de connexion ou si le tableau de bord est affiché
# if "Log out" in dashboard_response.text or "Tableau de bord" in dashboard_response.text:
#     print("Connexion réussie, accès au tableau de bord")
# else:
#     print("Échec de la connexion, redirection vers la page de connexion")