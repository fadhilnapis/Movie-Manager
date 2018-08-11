from Providers import jsonxml, rename, movieCollection as msets
import sys, os, datetime, xmltodict, ctypes

has_arg = len(sys.argv)>1
if has_arg:
	file_path = sys.argv[1]
	pass
else:
	file_path = "C:\\Users\\Fadz\\Documents\\Movie\\Deadpool 2 (2018) WEBRip 1080p"\
	+"\\Deadpool 2 (2018) WEBRip 1080p akoam net.mkv"
	pass

now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p");
movieSets = msets.movieSets

arg_dir = os.path.isdir(file_path)
nfo_file = False
if arg_dir:
	for dir_file in os.listdir(file_path):
		if dir_file.endswith(".nfo"):
			nfo_file = os.path.join(file_path,dir_file)
			break
			pass
		pass
	pass
else:
	full_nfo = os.path.join(os.path.dirname(file_path), rename.getNameOnly(file_path)+".nfo")
	if os.path.exists(full_nfo):
		nfo_file = full_nfo
		pass
	if os.path.exists(os.path.join(os.path.dirname(file_path), "movie.nfo")):
		nfo_file = os.path.join(os.path.dirname(file_path), "movie.nfo")
		pass


print(now_time)

def dprint(msg, val):
	if has_arg:
		return input(msg)
	else:
		print(msg, val)
		return val
		pass

def listSet():
	print("List of Movie Sets:")
	for count in range(len(movieSets)):
		print(" ({0}): {2} - {1}".format(count, movieSets[count]["datetime"], movieSets[count]["name"]))
		pass
	pass

def getInfo():
	xml = rename.getFileContent(nfo_file)
	xml_dict = xmltodict.parse(xml)
	return xml_dict
	pass
def assignSet(movie_set):
	xml_dict = getInfo()
	xml_dict["movie"]["set"]=movie_set
	xml_text = "\n".join(xmltodict.unparse(xml_dict, pretty=True).split("\n")[1:])
	print(nfo_file)

	FILE_ATTRIBUTE_NORMAL = 0x80
	ctypes.windll.kernel32.SetFileAttributesW(nfo_file,FILE_ATTRIBUTE_NORMAL)

	rename.writeTo(nfo_file, xml_text, hidden=True)
	print("assigned!")
	pass

def runCLI():
	if len(movieSets)>0:
		movie_info = getInfo()["movie"]
		if "set" in movie_info:
			print("\nAssigned as '{}', you can still override it.".format(movie_info["set"]["name"]))
		else:
			print("You have not assigned the movie set yet.")
			pass
		listSet()
		print(" (x): choose other action")
		selection = dprint("Asign this movie to set number:", "x")
		if selection=="x":
			print("List of Action:")
			print(" (0): add new set")
			print(" (1): delete set")
			print(" (2): clear set on this movie")
			action = dprint("Choose your action:", "2")
			if int(action)==1:
				listSet()
				delete = int(dprint("Choose set to delete:","0"))
				confirm_delete = dprint("Are you sure want to delete this? (y/N)","y")
				if confirm_delete=="y":
					msets.removeSets(movieSets[delete]["name"])
					print(movieSets)
					print("deleted.")
					msets.save()
					pass
			elif int(action)==0:
				new_set = {}
				new_set["name"] = dprint("Name?:","Harry Potter")
				new_set["overview"] = dprint("Overview?:","Harry Potter Franchise")
				new_set["datetime"] = now_time
				print("-----------------------------")
				print("New set named '{}' will be created:".format(new_set["name"]))
				print(" Name:",new_set["name"])
				print(" Overview:",new_set["overview"])
				print(" Datetime:",new_set["datetime"])
				loking_good = dprint("Looking Good? (Y/n):", "y")
				if not loking_good.lower()=="n":
					msets.addSets(new_set)
					pass
				print("New set named '{}' has been created!".format(new_set["name"]))
				assign = dprint("Asign to this movie? (Y/n)", "y") 
				if not assign.lower()=="n":
					assignSet(new_set)
					pass
				msets.save()
			elif int(action) == 2:
				clear = dprint("Clear sets on this movie? (Y/n)", "y") 
				if not (clear.lower()=='n'):
					print("cleared!")
					pass
				pass
		else:
			try:
				selection = int(selection)
				confirm = dprint("Asigning '{} - {}' to this movie? (y/N):".format(movieSets[selection]["name"],movieSets[selection]["overview"]), "y")
				assignSet(movieSets[selection])
			except Exception as e:
				print(e)
				print("invalid:",selection)
			pass
		pass
		# msets.save()
	pass

if nfo_file:
	runCLI()
	# assignSet({"dada":"opop"})
	pass
else:
	print("File '.nfo' not found. Please retrieve info first.")
	pass