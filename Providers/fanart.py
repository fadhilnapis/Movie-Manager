import requests

FANART_HOST = "http://webservice.fanart.tv/v3/movies/"
FANART_KEY = 'd6f98d85f14c9b32c8779542d4de7684'

def getArt(id):
	res = requests.get(FANART_HOST+"{0}?api_key={1}".format(id,FANART_KEY))
	return res.json()
	pass