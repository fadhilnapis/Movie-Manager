import requests
import Providers.jsonxml as json2xml

OMDB_HOST = "http://www.omdbapi.com/"
OMDB_KEY = '9990d5d8'
OMDB_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
OMDB_WITH_KEY = OMDB_HOST + "?apikey=" + OMDB_KEY;

def getFrom(parameter,value):
	url = OMDB_WITH_KEY + "&"+parameter+"=" + value
	result = requests.get(url)
	return {"json":result.json(), "xml":json2xml.convert(result.json())}
	pass


# import tmdbsimple as tmdb
# import jsonxml as jsonxml
# tmdb.API_KEY = '35ab048926236313bb053ec3c64d5116'
# search = tmdb.Search()
# # response = search.movie(query='Black Panther')
# # for s in search.results:
# # 	print(jsonxml.convert({"result":s}))
# # 	pass

# movie = tmdb.Movies(284054)
# print(jsonxml.convert(movie.info()))