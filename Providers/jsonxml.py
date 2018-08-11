from src.json2xml import Json2xml
import xmltodict,os,dict2xml,ctypes

def convert(data):
	data_object = Json2xml(data)

	dicxml = xmltodict.parse(data_object.json2xml())

	dicxml["movie"] = dicxml.pop("all")
	newdicktxml = dict()
	for k,v in dicxml["movie"].items():
		newdicktxml[k.lower()]=v
		pass
	finaldic = dict()
	finaldic["movie"]=newdicktxml
	newxml = dict2xml.dict2xml(finaldic)
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