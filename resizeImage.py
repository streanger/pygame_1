#image resizing script
#image filter options BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE i SHARPEN. 
#save the same format e.g. png or jpg
#resize with scaling

from PIL import Image
from resizeimage import resizeimage
import os
import math	
from PIL import ImageFilter
	
def resizing(fileName, newDir, width):
	#get the current path
	os.chdir(os.path.dirname(__file__))
	pathAbs = os.getcwd()
	path = os.path.join(pathAbs, fileName)
	
	#deal with the file resize
	with open(fileName, "r+b") as f:
		with Image.open(f) as image:
			image = image.filter(ImageFilter.SHARPEN)
			height = math.trunc((width/image.size[0])*image.size[1])
			#height = math.trunc(height)
			if (width >= image.size[0]):
				width = image.size[0]
				height = image.size[1]	
			cover = resizeimage.resize_cover(image, [width,height])

	#make new path		
	path = os.path.join(pathAbs, newDir)	
	dot = fileName.find('.')
	newFile = fileName[:dot] + "" + fileName[dot:]
	path = os.path.join(path, newFile )
	
	#make new dir
	if not os.path.exists(os.path.dirname(path)):
		try:
			os.makedirs(os.path.dirname(path))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise	
	#save resized image
	cover.save(path, image.format)	
	#closing files, images; f.close() is required
	f.close()
	
def autoResize(width=400):
	os.chdir(os.path.dirname(__file__))
	pathAbs = os.getcwd()
	files = os.listdir()
	imageFiles = []
	#define more types as you wish
	correctTypes = ('png','jpg','jpeg','bmp')
	for x in range(len(files)):
		dot = files[x].find('.')
		types = files[x][dot+1:]
		if (types in correctTypes):
			imageFiles.append(files[x])
	#specify the directory here
	newDir = "converted"
	for x in range(len(imageFiles)):
		resizing(imageFiles[x], newDir, width)
	print("Konwersja zakonczona")	

#single photo resizing	
#resizing('another.jpg', 'resized', 600)

#all photos resizing
autoResize(600)
	

