import sys, os
from Rename import Rename

import Providers.omdb as omdb

if len(sys.argv)>1:
	file_path = sys.argv[1]
	pass
else:
	file_path = "C:\\Users\\Fadz\\Documents\\Movie\\Deadpool 2 (2018) WEBRip 1080p"
	pass
file_name_ori = os.path.basename(file_path)
file_name = Rename.rename(file_name_ori, "{}")
movie_result = omdb.getFrom("s", file_name)
print("Search result for '{}':".format(file_name))
movies = []
if "Search" in movie_result["json"]:
	count=0
	movies = movie_result["json"]["Search"]
	for movie in movies:
		print(" ({}): {}".format(count, movie["Title"]))
		count+=1
	pass
	# movie_index = int(input("Insert movie index number: "))
	movie_index = 1
	movie_info = omdb.getFrom("i", movies[movie_index]["imdbID"])
print(movie_info["xml"])
print("")
# print(movie_result)