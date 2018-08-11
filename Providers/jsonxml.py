from src.json2xml import Json2xml
import xmltodict,os,dict2xml,ctypes

KODI_HEADER = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'

def convert(data,parent="movie"):
	data_object = Json2xml(data)

	dicxml = xmltodict.parse(data_object.json2xml())

	dicxml[parent] = dicxml.pop("all")
	newdicktxml = dict()
	for k,v in dicxml[parent].items():
		newdicktxml[k.lower()]=v
		pass
	finaldic = dict()
	finaldic[parent]=newdicktxml
	newxml = KODI_HEADER+dict2xml.dict2xml(finaldic)
	return newxml

# 	pass
# for x in os.listdir("./"):
# 	if os.path.isdir("./"+x):
# 		if os.path.exists("./"+x+"/movieinfo.json") and not os.path.exists("./"+x+"/movie.nfo"):
# 			writeNFO("./"+x)
# 			print("./"+x)
# 			pass
# 		pass
# 	pass