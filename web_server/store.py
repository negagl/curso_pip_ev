import requests


def get_categories(url):
    r = requests.get(url)
    print(r.status_code)

    categories = r.json()
    for category in categories:
        print(category['name'])
