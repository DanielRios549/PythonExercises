'''
    Get the city a person born and show if the city name starts with 'Santo'
'''
city = input('Which city do you born? ').strip()
print(f'Starts with Santo? \033[34m{"santo" in city.lower().split()[0]}\033[m')
