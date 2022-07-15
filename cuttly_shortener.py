from aiohttp import Payload
import requests
import sys

def shorten_link(full_link, link_name):
    API_KEY = '725e9074938c6c23a058f873407195e496cae'
    BASE_URL = 'https://cutt.ly/api/api.php'
    
    Payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=Payload)
    data = request.json()
    
    print('')
    
    try:
        shortened_date = data['url']['date']
        original_link = data['url']['fullLink']
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('Date:', shortened_date)
        print('Original:', original_link)
        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)
        
link = input('Enter original link: ')
# API for premium clients to create URL with custom name (url/<custom>)
# If client won't write name, the program will create URL with random short name 
name = input('Give your link a name: ') 


# Checking input url validation, that it is a correct url and size must be below 250 character
if len(link) > 249:
    sys.exit("Link is very long!")
    
shorten_link(link, name)
        
    
