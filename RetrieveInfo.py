import sys, os
from Rename import Rename

import Providers.omdb as omdb

if len(sys.argv)>1:
	file_path = sys.argv[1]
	pass
else:
	file_path = "C:\\Users\\Fadz\\Documents\\Movie\\Deadpool 2 (2018) WEBRip 1080p"
	# +"\\Deadpool 2 (2018) WEBRip 1080p akoam net.mkv"
	pass
file_path_parent = os.path.dirname(file_path)
file_name_ori = os.path.basename(file_path)
file_name = Rename.rename(file_name_ori, "{}")

movie_result = omdb.getFrom("s", file_name)

movies = []
if "Search" in movie_result["json"]:
	print("Search result for '{}':".format(file_name))
	count=0
	movies = movie_result["json"]["Search"]
	for movie in movies:
		print(" ({}): {}".format(count, movie["Title"]))
		count+=1
	pass
	if len(movies)>0:
		movie_index = 1
		movie_index = int(input("Insert movie index number: "))

		movie_info = omdb.getFrom("i", movies[movie_index]["imdbID"])
		movie_nfo = movie_info["xml"]

		target_path = file_path+".nfo"
		if os.path.isdir(file_path):
			target_path = os.path.join(file_path,"movie.nfo")
		else:
			target_path = os.path.join(file_path_parent,Rename.getNameOnly(file_name_ori)+".nfo")
			pass

		Rename.writeTo(target_path, movie_nfo, True)
		print("Done!")
		pass
	else:
		print("No movies available")
else:
	print("Cant find result")

# print(movie_result)