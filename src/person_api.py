import requests


def call_person_api(param, name):
    return requests.get(f"https://api.{param}.io?name={name}")
