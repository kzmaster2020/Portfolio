import requests

from bs4 import BeautifulSoup

year = 2011


url = 'https://worldradiohistory.com/Archive-Billboard/00s/' + str(year) + '/'

response = requests.get(url, verify=False)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')

for link in links:
    href= link.get('href')
    with open('links.txt', 'a' ) as file:
        file.write('https://worldradiohistory.com/Archive-Billboard/00s/' + str(year) + '/'+ href +  '\n')