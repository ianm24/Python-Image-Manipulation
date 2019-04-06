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
	for x in xrange(width):
		for y in xrange(height):
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
	for x in xrange(width):
		for y in xrange(height):
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
	for x in xrange(width):
		for y in xrange(height):
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
	for x in xrange(width):
		for y in xrange(height):
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
	for i in xrange(10):
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
	for i in xrange(10):
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
	for x in xrange(width):
		for y in xrange(height):
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
def addPhotos(f1,f2):
	im1 = Image.open(f1)
	im2 = Image.open(f2)
	p1 = im1.load()
	p2 = im2.load()
	if im1.size[0] == im2.size[0] and im2.size[0] == im2.size[1]:
		width = im1.size[0]
		height = im1.size[1]
		img = Image.new("RGBA",(width, height),(0,0,0,0))
		for x in xrange(width):
			for y in xrange(height):
				R=(p1[x,y][0]+p2[x,y][0]) % 255
				G=(p1[x,y][1]+p2[x,y][1]) % 255
				B=(p1[x,y][2]+p2[x,y][2]) % 255
				A=(p1[x,y][3]+p2[x,y][3]) % 255
				img.putpixel((x,y),(R,G,B,A))
	img.save('images/photos_added.bmp')
	print("Files added")