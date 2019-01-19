from Providers import rename
import json,os

MOVIE_SETS_PATH = os.path.abspath("Storage/MovieSets.json")
movieSets_str = rename.getFileContent(MOVIE_SETS_PATH)
movie_json = json.loads(movieSets_str)
movieSets = movie_json["Sets"]

def addSets(sets):
	movieSets.append(sets)
	pass

def removeSets(name):
	for set_index in range(len(movieSets)):
		if movieSets[set_index]["name"] == name:
			del movieSets[set_index]
			pass
		pass
		
def getSets(name):
	for set_index in range(len(movieSets)):
		if movieSets[set_index]["name"] == name:
			return movieSets[set_index]
			break;
			pass
	return
	pass
def save():
	movie_json["Sets"] = movieSets;
	rename.writeTo(MOVIE_SETS_PATH,json.dumps(movie_json))
	pass