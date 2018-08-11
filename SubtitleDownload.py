# coding: utf-8
import sys, os, re, zipfile, ctypes
import requests
from Providers import rename, subscene

if len(sys.argv)>1:
	file_path = sys.argv[1]
	pass
else:
	file_path = "C:\\Users\\Fadz\\Documents\\Movie\\Deadpool 2 (2018) WEBRip 1080p"
	pass

if len(sys.argv)>2:
	sub_lang = sys.argv[2]
	pass
else:
	sub_lang = "MA"
	pass

def zip_extractor(name, new_name, path, lang="MA"):
	'''
	Extracts zip file obtained from the Subscene site (which contains subtitles).
	'''
	with zipfile.ZipFile(name, "r") as z:
		# srt += [i for i in ZipFile.namelist() if i.endswith('.srt')][0]
		# z.extractall(".")
		zfile_list = z.namelist()
		if not os.path.isdir(path):
			path = os.path.dirname(path)
			pass
		if len(zfile_list)!=0:
			if len(zfile_list)>1:
				for index in range(len(zfile_list)):
					print("({}): {}".format(index,zfile_list[index]))

				file_ind = int(input("Which one?:"))
				target_name = zfile_list[file_ind]
				ext = rename.getExtension(target_name)
				z.extract(target_name,path)
			else:
				target_name = zfile_list[0]
				ext = rename.getExtension(target_name)
				print(target_name,path)
				z.extract(target_name,path)
				pass
			new_path = os.path.join(path,new_name+"."+subscene.LANGUAGE[lang]+ext)
			if os.path.exists(new_path):
				os.remove(new_path)
				print("-________________REMOVE OLD SUBTITLE________________-")
				pass
			os.rename(os.path.join(path, target_name),new_path)

			FILE_ATTRIBUTE_HIDDEN = 0x02
			ctypes.windll.kernel32.SetFileAttributesW(new_path,FILE_ATTRIBUTE_HIDDEN)
			pass
	os.remove(name)
	print("Done.\n");
	pass


def dl_sub(page, name, path="./", lang="MA"):
	'''
	Download subtitles obtained from the select_subtitle
	function i.e., movie subtitles links.
	'''
	# start_time = time.time()
	soup = subscene.scrape_page(page)
	div = soup.find('div', {'class': 'download'})
	down_link = 'https://subscene.com' + div.find('a').get('href')
	r = requests.get(down_link, stream=True)
	for found_sub in re.findall("filename=(.+)", r.headers['content-disposition']):
		with open(found_sub.replace('-', ' '), 'wb') as f:
			for chunk in r.iter_content(chunk_size=150):
				if chunk:
					f.write(chunk)
		zip_extractor(found_sub.replace('-', ' '), name, path, lang=lang)
	print("Subtitle ({}) - Downloaded\n".format(found_sub.replace('-', ' ').capitalize()))
	# print("--- download_sub took %s seconds ---" % (time.time() - start_time))


basename_ori = os.path.basename(file_path)
file_name = rename.getNameOnly(basename_ori)

file_parent = os.path.dirname(file_path)
find_path = os.path.join(file_parent, basename_ori);

if os.path.isdir(basename_ori):
	find_path = os.path.join(file_parent, basename_ori);
	movie_name_ori = file_name
	for file in os.listdir(find_path):
		if file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".flv") or file.endswith(".rmvb"):
			movie_name_ori = file
			break
		pass
	movie_name_ori = movie_name_ori.rsplit('.',1)[0]
	movie_name = rename.rename(movie_name_ori, format="{}")
	target_path = os.path.join(file_parent,basename_ori,movie_name_ori)
	pass
else:
	movie_name_ori = basename_ori.rsplit('.',1)[0]
	movie_name = rename.rename(movie_name_ori, format="{}")
	target_path = os.path.join(file_parent,movie_name_ori)
	pass

print(movie_name)
	# Searches for the specified movie.
movie_name = movie_name
print("Searching For: {}".format(movie_name))
sub_link = subscene.sel_title(name=movie_name,lang=sub_lang)
print("Subtitle Link for {} : {}".format(movie_name, sub_link))
print("{} Subtitle List:".format(subscene.LANGUAGE[sub_lang]))
if sub_link:
	subtitle_list = subscene.sel_sub(page=sub_link, name=movie_name_ori, lang=sub_lang)
	count = 0;
	for link in subtitle_list:
		print("({}): {}".format(count,link["name"].decode('utf-8')))
		count+=1;
		pass
	if len(subtitle_list)>0:
		sub_ind = int(input("Choose the number: "))
		dl_sub(subtitle_list[sub_ind]["url"], movie_name_ori, basename_ori, lang=sub_lang)
	else:
		print("not found")
		pass
# film = subscene.sel_title(movie_name);
# print(film)
# for subtitle in film.subtitles:
# 	print("({}): {} - {}".format(count, subtitle.title, subtitle.language))
# 	count+=1;
# 	pass

print("target_path:",target_path)
print("file_name:",file_name)
print("find_path:",find_path)
print("basename_ori:",basename_ori)
print("file_parent:",file_parent)