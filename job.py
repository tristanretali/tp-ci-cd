import os

a = 2
print("coucou", a)

secret_api_token = os.environ.get("SECRET_API_TOKEN")
print("secret token recupere :", secret_api_token)
