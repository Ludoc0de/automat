import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import schedule
import time
from email_utils import send_email

# Charger les variables d'environnement
load_dotenv()

# Obtenir les variables d'environnement
USERNAME = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD_EMAIL = os.getenv("PASSWORD_EMAIL")


def send_daily_report():
    # Script proncipal pour se logger and accéder au tableau de bord
    login_url = "https://frontendmasters.com/login/"
    dashboard_url = "https://frontendmasters.com/dashboard/"

    # # Création d'une session pour conserver les cookies
    session = requests.session()

    # # Obtenir la page de connexion pour récupérer les cookies et éventuellement des tokens CSRF
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # # Rechercher le token CSRF (le nom du champ peut varier en fonction du site)
    # csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

    headers = {
        "Referer": login_url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }

    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        # "csrfmiddlewaretoken": csrf_token
    }

    login_response = session.post(login_url, data=payload, headers=headers)
    # Vérifier si responses ok
    if login_response.status_code == 200:
        login_message = "Response 200, réponse ok"

    else:
        login_message = "Error in response:", login_response.status_code

    print(login_message)

    dashboard_response = session.get(dashboard_url)
    print(dashboard_response.text[:5000])

    # Vérifier si vous êtes redirigé vers la page de connexion ou si le tableau de bord est affiché
    if "Logout" in dashboard_response.text or "My Home" in dashboard_response.text:
        result_message = "Connexion réussie, accès au tableau de bord"
    else:
        result_message = "Échec de la connexion, redirection vers la page de connexion"

    print(result_message)

    # Preparartion du contenu de l'email
    email_subject = "Login Status Report"
    email_body = f"Login Response:\n\n{login_response.text[:1000]}\n\n{login_message}\n\n{result_message}"

    # Envois de l'email
    send_email(email_subject, email_body, SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD_EMAIL)


# Schedule the job to run every day at 8 AM
schedule.every().day.at("16:00").do(send_daily_report)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
