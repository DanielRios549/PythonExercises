import urllib
import urllib.error
import urllib.request


def verify(site: str):
    try:
        urllib.request.urlopen(f'https://{site}')

    except urllib.error.URLError:
        print(f'The website {site} is \033[31m not accessible.\033[m')

    else:
        print(f'The website {site} is \033[32maccessible.\033[m')
