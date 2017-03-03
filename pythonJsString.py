#python code to javascript string converter 21.02.2017
#run this script in the .py files directory
#just put the results into < pre>...<.pre> tags in javascript file
import os

def pythonJsString(fileName, newDir):
	#get the script path
	os.chdir(os.path.dirname(__file__))
	pathAbs = os.getcwd()
	#uncomment the following line or make some changes for abs path
	#pathAbs = r'D:\Games\programming\python'
	path = os.path.join(pathAbs, fileName)	
	file = open(path, "r")		#file to encode
	code = file.readlines()		#it gives a list
	file.close()
	code2 = []									
	for x in range(len(code)):
		#remove '\n' and double quotes
		spam = code[x].replace('\n', '')				 
		spam = spam.replace('\\n', '')					 
		spam = spam.replace('"', "'") + "\\n\\\n"		 
		spam.encode("utf8")		#encode all signs
		code2.append(spam)		#add to list
	path = os.path.join(pathAbs, newDir)
	newFile = fileName[:len(fileName)-3] + "Encoded.txt"
	path = os.path.join(path, newFile )
	if not os.path.exists(os.path.dirname(path)):
		try:
			os.makedirs(os.path.dirname(path))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise	
	file = open(path, "w")
	for x in range(len(code2)):
		file.writelines(code2[x])
	file.close()
	
def autoJsString():
	os.chdir(os.path.dirname(__file__))
	pathAbs = os.getcwd()
	files = os.listdir()
	filesPy = []
	for x in range(len(files)):
		if (files[x][-3:] == ".py"): filesPy.append(files[x])
	#specify the directory here
	newDir = "converted"
	for x in range(len(filesPy)):
		pythonJsString(filesPy[x], newDir)
	print("Konwersja zakonczona")	
	
#auto script finds .py files and converts to specified dir	
autoJsString()
