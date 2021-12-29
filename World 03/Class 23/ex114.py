'''
    Create a test that verify if a website is available in the computer.
'''
from utils.site import verify


site = input('Choose a Website: \033[34mhttps://\033[m')
verify(site)
