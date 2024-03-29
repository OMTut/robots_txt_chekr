import requests

# get url
BASE_URL = input("Enter the URL: ")

# check if the url starts with http or https
if not BASE_URL.startswith('https'):
   BASE_URL = 'https://' + BASE_URL
if not BASE_URL.endswith('/'):
   BASE_URL += '/'

url = BASE_URL + 'robots.txt'
response = requests.get(url)

if response.status_code == 200:
   print(response.text)
else:
   print(f"Error: {response.status_code}")
   print(f"Failed to retrieve robots.txt from {url}")