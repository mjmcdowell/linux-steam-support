
from urllib import FancyURLopener
import json
import unicodedata

class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

key = "<apikey>"
player = "<playerid>"
url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json&include_appinfo=1" %(key,player)

dbinfo = 'https://steamdb.info/linux/'

myopener = MyOpener()

data1 = myopener.open(url).read()
r1 = json.loads(data1)
l = 0
i = 0
info = myopener.open(dbinfo).read()
for game in r1['response']['games']:
	try:
		nix = str(game['appid']) in info
		print game['name'] +' : ' + str(nix)
		if nix == True:
			l += 1
	except UnicodeEncodeError:
		nix = str(game['appid']) in info
		unicodedata.normalize('NFKD', game['name']).encode('ascii','ignore') +' : ' + str(nix)
		if nix == True:
			l += 1
	i += 1
print "%s of %s games are supported on Linux!" %(l,i)