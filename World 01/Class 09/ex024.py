'''
    Get the city a person borns and show if the city name starts with 'Santo'
'''
city = input('Which city do you born? ').strip()
print(f'Starts with Santo? {"santo" in city.lower().split()[0]}')
