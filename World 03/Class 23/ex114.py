'''
    Create a test that verify if a website is available in the computer.
'''

import urllib
import urllib.error
import urllib.request

site = input('Choose a Website: \033[34mhttps://\033[m')

try:
    urllib.request.urlopen(f'https://{site}')

except urllib.error.URLError:
    print(f'The website {site} is \033[31m not accessible.\033[m')

else:
    print(f'The website {site} is \033[32maccessible.\033[m')
