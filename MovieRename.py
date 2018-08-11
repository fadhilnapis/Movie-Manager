import sys, os
from Providers import rename

if len(sys.argv)>1:
	file_path = sys.argv[1]
	pass
else:
	file_path = "C:\\dasdqwe\\dasd\\Deadpool.2.2018.Super.Duper.Cut.UNRATED.1080p. WEBRip.akoam.net.mkv"
	pass

print("file_path:",file_path)

file_name_ori = os.path.basename(file_path)
file_name = rename.rename(file_name_ori)

file_folder = os.path.dirname(file_path)
file_new_folder = rename.rename(file_name_ori)

if os.path.isfile(file_path):
	new_path = os.path.join(file_folder,file_new_folder+"\\"+file_name+rename.getExtension(file_name_ori))
	if not os.path.exists(file_new_folder):
	    os.makedirs(file_new_folder)
	    pass
else:
	new_path = os.path.join(file_folder,file_name+rename.getExtension(file_name_ori))
	pass

os.rename(file_path, new_path);

print("new_path:",new_path)

print("file_folder:",file_folder)
print("file_name:",file_name)
print("Rename:",rename.getExtension(file_name_ori))

