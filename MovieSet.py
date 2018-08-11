from Providers import movieCollection as msets
import datetime

now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p");
movieSets = msets.movieSets
if len(movieSets)>0:
	print("List of Movie Sets:")
	for count in range(len(movieSets)):
		print(" ({}): {} - {}".format(count, movieSets[count]["name"], movieSets[count]["datetime"]))
		pass
	pass