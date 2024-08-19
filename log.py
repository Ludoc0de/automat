import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Charger les variables d'environnement
load_dotenv()

# Obtenir les variables d'environnement
USERNAME = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
PASSWORD_EMAIL = os.getenv('PASSWORD_EMAIL')

# Définir la fonction pour envoyer un email
def send_email(subject, body):
    sender_email = SENDER_EMAIL
    receiver_email =  RECEIVER_EMAIL
    password_email = PASSWORD_EMAIL

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Send the email via SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email,password_email)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Main script for logging in and checking dashboard
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
# Vérifier si responses ok
print(login_response)

dashboard_response = session.get(dashboard_url)
print(dashboard_response.text[:5000])

# Vérifier si vous êtes redirigé vers la page de connexion ou si le tableau de bord est affiché
if "Logout" in dashboard_response.text or "My Home" in dashboard_response.text:
    print("Connexion réussie, accès au tableau de bord")
else:
    print("Échec de la connexion, redirection vers la page de connexion")