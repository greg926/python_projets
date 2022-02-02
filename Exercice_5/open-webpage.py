import urllib.request, urllib.parse

url = 'https://www.odoo.com/fr_FR'

reponse = urllib.request.urlopen(url)
contenu_web = reponse.read().decode('UTF-8')

print(contenu_web[0:300])