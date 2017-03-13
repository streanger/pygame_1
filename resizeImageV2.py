#this script rename or/and resize photos

from PIL import Image
from resizeimage import resizeimage
import os
import math	
	
def resizing(fileName, newDir, width, number, newName, toResize):
	#get the current path
	os.chdir(os.path.dirname(__file__))
	pathAbs = os.getcwd()
	path = os.path.join(pathAbs, fileName)
	
	#deal with the file resizing
	with open(fileName, "r+b") as f:
		with Image.open(f) as image:
			height = math.trunc((width/image.size[0])*image.size[1])
			if (width >= image.size[0]) or (toResize == False):
				width = image.size[0]
				height = image.size[1]	
			cover = resizeimage.resize_cover(image, [width,height])

	#make new path		
	path = os.path.join(pathAbs, newDir)	
	dot = fileName.find('.')
	newFile = newName + number + fileName[dot:]
	path = os.path.join(path, newFile )
	
	#make new dir
	if not os.path.exists(os.path.dirname(path)):
		try:
			os.makedirs(os.path.dirname(path))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise	
	#save image
	cover.save(path, image.format)	
	cover.close()
	image.close()
	f.close()
	
def autoResize(width=400, newName="photo", toResize=True):
	os.chdir(os.path.dirname(__file__))
	pathAbs = os.getcwd()
	files = os.listdir()
	imageFiles = []
	for x in range(len(files)):
		dot = files[x].find('.')
		types = files[x][dot+1:]
		trueTypes = "png","jpg","jpeg"
		#if (types == "png") or (types == "jpg") or (types == "jpeg"):
		if (types in trueTypes):
			imageFiles.append(files[x])
	#specify the directory here
	newDir = "converted"
	for x in range(len(imageFiles)):
		if (x < 10):
			number = "0" + str(x)
		else:
			number = str(x)
		resizing(imageFiles[x], newDir, width, number, newName, toResize)
	if (x == 0):
		print("Brak plikow do konwersji.")
	else: 
		print("Konwersja zakonczona.")	

#single photo	
#resizing('another.jpg', 'resized', 300)			
autoResize(1920, "photo", True)
	

