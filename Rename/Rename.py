import os, re
ripQuality = ["4320p", "2160p", "1440p", "1080p", "1080i", "720p", "720i", "480p", "480i", "360p", "240p"]
ripQualityWidth = ["7680", "3840", "2560", "1920", "1920", "1280", "1280", "858", "858", "480", "352"]
pirateRelease=['CAMRip','CAM',
'TS','HDTS','TELESYNC','PDVD',
'WP','WORKPRINT',
'TC','TELECINE',
'PPV','PPVRip',
'SCR','SCREENER','DVDSCR','DVDSCREENER','BDSCR',
'DDC',
'R5','R5.LINE','R5.AC3.5.1.HQ',
'DVDRip',
'DVDR','DVD-Full','Full-Rip','ISO rip','DVD-5','DVD-9',
'DSR','DSRip','SATRip','DTHRip','DVBRip','HDTV','PDTV','TVRip','HDTVRip',
'VODRip','VODR',
'WEBDL','WEB-DL','WEB','HDRip',
'WEB-Rip','WEBRip','HDRip',
'WEB-Cap','WEBCAP',
'BDRip','BRRip','Blu-Ray','BluRay','BDR','BD5','BD9','BD25','BD50'];

def getAttribute(OriginalName='',arrfile='',mode=1):
	movieYearIndex=0;
	movieYear='';

	movieQualityIndex=0;
	movieQuality='';

	moviePirateReleaseIndex=0
	moviePirateRelease=''

	movieTitle=''
	movieTitleEnd=''
	if ']' in OriginalName and '[' in OriginalName:
		inSquare = OriginalName.split("]")[0].split("[")[1].strip()

		# replace delete bracket
		OriginalName = re.sub(r'\[[^)]*\]', '', OriginalName).strip()
		if inSquare !="":
			OriginalName+=" "+inSquare
			pass

	if '(' in OriginalName: OriginalName = re.sub(r'\(', '', OriginalName)
	if ')' in OriginalName: OriginalName = re.sub(r'\)', '', OriginalName)
	if "_" in OriginalName: OriginalName = OriginalName.replace("_"," ")

	if mode==0: fileAttr = OriginalName.split(' ')

	else:fileAttr = OriginalName.replace('.',' ').split(' ')

	for x in range(0,len(fileAttr)):
		i =len(fileAttr)-1-x
		# check for 4 digit and it will be year
		if len(fileAttr[i]) == 4 and fileAttr[i].isdigit():
			movieYear=fileAttr[i];
			movieYearIndex=i
			break

	for x in range(movieYearIndex+1,len(fileAttr)):
		if fileAttr[x].lower() in ripQuality:
			movieQuality=fileAttr[x].lower()
			movieQualityIndex=x;
		if fileAttr[x].lower() in [item.lower() for item in pirateRelease]:
			moviePirateRelease=pirateRelease[[item.lower() for item in pirateRelease].index(fileAttr[x].lower())]
			moviePirateReleaseIndex=x;

	arrAtrx =[s for s in [movieYearIndex,movieQualityIndex,moviePirateReleaseIndex] if s!=0];
	for x in range(0,len(fileAttr)):
		if not arrAtrx:
			movieTitle = OriginalName;
			break
		else:
			if x not in arrAtrx and x < min(arrAtrx):
				movieTitle +=' '+fileAttr[x];
			if x not in arrAtrx and x > max(arrAtrx):
				movieTitleEnd +=' '+fileAttr[x];
	ftg=[]
	if os.path.isfile('./'+arrfile):
		for ghj in os.listdir("./"+arrfile):
			if ghj.lower().endswith(".srt") or ghj.lower().endswith(".ass"):
				ftg.append(ghj);
				pass
			pass
		pass
	checksbttle = len(ftg)>0
	checkposter = os.path.isfile('./'+arrfile+'/poster.jpg') 
	return [movieTitle.strip(),movieYear,moviePirateRelease,movieQuality,movieTitleEnd.strip(),('Y' if checksbttle else 'N'),('Y' if checkposter else 'N'),('2' if '' in [movieYear,moviePirateRelease,movieQuality] else '3'),arrfile]
def rename(path, format="{} ({}) {} {} {}"):
	extension=""
	if path.endswith(".mkv") or path.endswith(".mp4") or path.endswith(".avi") or path.endswith(".flv"):
		path = path.rsplit('.',1)[0]
		pass

	property = getAttribute(path,mode=1);
	new_name = format.format(property[0],property[1],property[2],property[3],property[4]).strip()
	return re.sub(' +',' ',new_name)
	pass
def getExtension(path):
	extension = "."+path.rsplit('.',1)[1]
	return extension;
	pass