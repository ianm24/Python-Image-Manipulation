# Program Made By: Ian McDowell
# Started 4 March 2019

from PIL import Image
import glob, os, imageio, random

#flips each pixel's y-coordinate
def flipY(fileName):
	im = Image.open(fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			img.putpixel((x,y),pixels[x,abs(y-height)-1])
	img.save(fileName[:fileName.find('.')] + '_FlipY.bmp')
	print("Flipped-Y file has been created")

#flips each pixel's x-coordinate
def flipX(fileName):
	im = Image.open(fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			img.putpixel((x,y),pixels[abs(x-width)-1,y])
	img.save(fileName[:fileName.find('.')] + '_FlipX.bmp')
	print("Flipped-X file has been created")

#randomly flips each pixel's x-coordinate
def randFlipX(fileName, saveName):
	im = Image.open(fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			if(random.randint(1,2) == 1):
				img.putpixel((x,y),pixels[abs(x-width)-1,y])
			else:
				img.putpixel((x,y),pixels[x,y])
	img.save(saveName[:saveName.find('.')] + '_RandFlipX.bmp')
	print("Randomly Flipped-X file has been created")

#randomly flips each pixel's y-coordinate
def randFlipY(fileName, saveName):
	im = Image.open(fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			if(random.randint(1,2) == 1):
				img.putpixel((x,y),pixels[x,abs(y-height)-1])
			else:
				img.putpixel((x,y),pixels[x,y])
	img.save(saveName[:saveName.find('.')] + '_RandFlipY.bmp')
	print("Randomly Flipped-Y file has been created")

#randomly flips X and adds them all into a .gif
def randFlipXGif(fileName,path):
	images = []
	iList = []
	for i in range(10):
		randFlipX(path+'/'+fileName, path+'/'+str(i)+fileName)
		images.append(imageio.imread(path+'/'+str(i)+fileName.split('.')[0]+'_RandFlipX.bmp'))
		iList.append(path+'/'+str(i)+fileName.split('.')[0]+'_RandFlipX.bmp')
	imageio.mimsave(path+'/'+fileName.split('.')[0]+'_RandFlipX.gif', images)
	for file in iList:
		os.remove(file)

#randomly flips Y and adds them all into a .gif
def randFlipYGif(fileName,path):
	images = []
	iList = []
	for i in range(10):
		randFlipY(path+'/'+fileName, path+'/'+str(i)+fileName)
		images.append(imageio.imread(path+'/'+str(i)+fileName.split('.')[0]+'_RandFlipY.bmp'))
		iList.append(path+'/'+str(i)+fileName.split('.')[0]+'_RandFlipY.bmp')
	imageio.mimsave(path+'/'+fileName.split('.')[0]+'_RandFlipY.gif', images)
	for file in iList:
		os.remove(file)

#takes 4 images and makes them into 1
def square(f1,f2,f3,f4,saveName):
	#TL;TR;BL;BR;saveName
	im1 = Image.open(f1)
	im2 = Image.open(f2)
	im3 = Image.open(f3)
	im4 = Image.open(f4)
	p1 = im1.load()
	p2 = im2.load()
	p3 = im3.load()
	p4 = im4.load()
	width = im1.size[0]+im2.size[0]
	height = im1.size[1]+im3.size[1]
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			if(x < im1.size[0] and y < im1.size[1]):
				img.putpixel((x,y),p1[x,y])
			elif(x >= im1.size[0] and y < im1.size[1]):
				img.putpixel((x,y),p2[x-im1.size[0],y])
			elif(x < im1.size[0] and y >= im1.size[1]):
				img.putpixel((x,y),p3[x,y-im1.size[1]])
			elif(x >= im1.size[0] and y >= im1.size[1]):
				img.putpixel((x,y),p4[x-im1.size[0],y-im1.size[1]])
	img.save(saveName[:saveName.find('.')] + '_square.bmp')
	print(saveName+" file has been created")

#takes one image, gets all the flips to make it into a square
def squareStitch(fileName):
	#fileName is bottom right
	flipX(fileName)
	flipY(fileName)
	flipX(fileName[:fileName.find('.')] + '_FlipY.bmp')
	square(fileName[:fileName.find('.')] + '_FlipY_FlipX.bmp',
		fileName[:fileName.find('.')] + '_FlipY.bmp',
		fileName[:fileName.find('.')] + '_FlipX.bmp',
		fileName,fileName)

#adds pixels of 2 photos
def addSameDimPhotos(f1,f2,path1,path2):
	im1 = Image.open(path1 + "/" + f1)
	im2 = Image.open(path2 + "/" + f2)
	p1 = im1.load()
	p2 = im2.load()
	if im1.size[0] == im2.size[0] and im1.size[1] == im2.size[1]:
		width = im1.size[0]
		height = im1.size[1]
		img = Image.new("RGBA",(width, height),(0,0,0,0))
		for x in range(width):
			for y in range(height):
				R = (p1[x,y][0]+p2[x,y][0])
				G = (p1[x,y][1]+p2[x,y][1])
				B = (p1[x,y][2]+p2[x,y][2])
				img.putpixel((x,y),(R,G,B,255))
	img.save('images/' + f1[:f1.find('.')] + '_plus_' + f2[:f2.find('.')] + '.bmp')
	print("Files added")

#adds pixels of 2 photos
def addPhotos(f1,f2,path1,path2):
	im1 = Image.open(path1 + "/" + f1)
	im2 = Image.open(path2 + "/" + f2)
	p1 = im1.load()
	p2 = im2.load()
	width = im1.size[0] if im1.size[0] > im2.size[0] else im2.size[0]
	height = im1.size[1] if im1.size[1] > im2.size[1] else im2.size[1]
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			fileOnePixel = p1[x,y] if x < im1.size[0] and y < im1.size[1] else [0,0,0]
			fileTwoPixel = p2[x,y] if x < im2.size[0] and y < im2.size[1] else [0,0,0]
			R = int((fileOnePixel[0]+fileTwoPixel[0]))
			G = int((fileOnePixel[1]+fileTwoPixel[1]))
			B = int((fileOnePixel[2]+fileTwoPixel[2]))
			img.putpixel((x,y),(R,G,B,255))
	img.save('images/' + f1[:f1.find('.')] + '_plus_' + f2[:f2.find('.')] + '.bmp')
	print("Files added")