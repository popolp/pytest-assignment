import requests
def call_api(param, name):
    return requests.get(f"https://api.{param}.io?name={name}")
