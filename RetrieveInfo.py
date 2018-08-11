import sys, os
from Providers import rename, omdb, fanart

if len(sys.argv)>1:
	file_path = sys.argv[1]
	pass
else:
	file_path = "C:\\Users\\Fadz\\Documents\\Movie\\Deadpool 2 (2018) WEBRip 1080p"
	# +"\\Deadpool 2 (2018) WEBRip 1080p akoam net.mkv"
	pass
file_path_parent = os.path.dirname(file_path)
file_name_ori = os.path.basename(file_path)
file_name = rename.rename(file_name_ori, "{}")

movie_result = omdb.getFrom("s", file_name)

movies = []
if "Search" in movie_result["json"]:
	print("Search result for '{}':".format(file_name))
	count=0
	movies = movie_result["json"]["Search"]
	for movie in movies:
		print(" ({}): {} ({})".format(count, movie["Title"], movie["Year"]))
		count+=1
	pass
	if len(movies)>0:
		movie_index = 1
		movie_index = int(input("Insert movie index number: "))

		movie_info = omdb.getFrom("i", movies[movie_index]["imdbID"])
		movie_xml = movie_info["xml"]
		movie_json = movie_info["json"]

		nfo_target_path = file_path+".nfo"
		target_path=dict()

		fnart = fanart.getArt(movie_json['id'])

		target_path["poster"] = dict()
		target_path["fanart"] = dict()
		target_path["clearart"] = dict()
		target_path["clearlogo"] = dict()

		target_path["poster"]["name"] = file_path
		target_path["fanart"]["name"] = file_path
		target_path["clearart"]["name"] = file_path
		target_path["clearlogo"]["name"] = file_path

		target_path["poster"]["url"] = movie_json["Poster"]
		target_path["fanart"]["url"] = False
		target_path["clearart"]["url"] = False
		target_path["clearlogo"]["url"] = False

		if len(fnart["moviebackground"])>0:
			target_path["fanart"]["url"] = fnart["moviebackground"][0]["url"]
			pass
		if len(fnart["hdmovieclearart"])>0:
			target_path["clearart"]["url"] = fnart["hdmovieclearart"][0]["url"]
			pass
		if len(fnart["hdmovielogo"])>0:
			target_path["clearlogo"]["url"] = fnart["hdmovielogo"][0]["url"]
			pass

		if os.path.isdir(file_path):
			nfo_target_path = os.path.join(file_path,"movie.nfo")
			target_path["poster"]["name"] = os.path.join(file_path,"poster")
			target_path["fanart"]["name"] = os.path.join(file_path,"fanart")
			target_path["clearart"]["name"] = os.path.join(file_path,"clearart")
			target_path["clearlogo"]["name"] = os.path.join(file_path,"clearlogo")
		else:
			nfo_target_path = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori)+".nfo")
			target_path["poster"]["name"] = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori)+"-poster")
			target_path["fanart"]["name"] = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori)+"-fanart")
			target_path["clearart"]["name"] = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori)+"-clearart")
			target_path["clearlogo"]["name"] = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori)+"-clearlogo")
			pass

		rename.downloadTo(target_path["poster"]["name"], target_path["poster"]["url"])
		rename.downloadTo(target_path["fanart"]["name"], target_path["fanart"]["url"], hidden=True)
		rename.downloadTo(target_path["clearart"]["name"], target_path["clearart"]["url"], hidden=True)
		rename.downloadTo(target_path["clearlogo"]["name"], target_path["clearlogo"]["url"], hidden=True)

		rename.writeTo(nfo_target_path, movie_xml, True)
		print("Done!")
		pass
	else:
		print("No movies available")
else:
	print("Cant find result")

# print(movie_result)