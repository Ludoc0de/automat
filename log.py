import requests

login_url = ("https://b12.io/accounts/login/?next=/dashboard/")
# dashboard_url = ("")

payload = {
    "username": "config.EMAIL",
    "password": "config.PASSWORD"
}

requests_post = requests.post(login_url, data=payload)
print(requests_post.text)
# requests_get = requests.get(dashboard_url)
# print(requests_get.text)