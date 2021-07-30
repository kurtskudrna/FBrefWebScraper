from bs4 import BeautifulSoup
import requests

url = requests.get('https://fbref.com/en/players/b9fbae28/NGolo-Kante')
html = url.text

soup = BeautifulSoup(html, features ='html.parser')

player_name = soup.body.h1.span.text
birth_date = soup.find('span', {'id': 'necro-birth'}).text
birth_place = soup.find('span', {'itemprop': 'birthPlace'}).text
height = soup.find('span', {'itemprop': 'height'}).text
weight = soup.find('span', {'itemprop': 'weight'}).text
awards = soup.find('ul', {'id': 'bling'}).findChildren('li')
print(player_name)
print('Born:', (birth_date).strip(), (birth_place).strip())
print('Height:', height)
print('Weight:', weight)
print('\n')
for i in awards:
	print(i.a.text)