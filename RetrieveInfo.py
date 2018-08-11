import sys, os
from Providers import rename, omdb

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
		poster_target_path_name = file_path
		if os.path.isdir(file_path):
			nfo_target_path = os.path.join(file_path,"movie.nfo")
			poster_target_path_name = os.path.join(file_path,"poster")
		else:
			nfo_target_path = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori)+".nfo")
			poster_target_path_name = os.path.join(file_path_parent,rename.getNameOnly(file_name_ori))
			pass

		rename.downloadTo(poster_target_path_name, movie_json["Poster"])
		rename.writeTo(nfo_target_path, movie_xml, True)
		print("Done!")
		pass
	else:
		print("No movies available")
else:
	print("Cant find result")

# print(movie_result)