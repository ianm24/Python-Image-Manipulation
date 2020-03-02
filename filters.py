# Program Made By: Ian McDowell
# Started 1 March 2020

from PIL import Image
import glob, os, imageio, random

#turns photo into monochrome colors
def monochrome(fileName, path):
	im = Image.open(path + '/' + fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			color = pixels[x,y][0] + pixels[x,y][1] + pixels[x,y][2]
			color = int(color/3) % 255
			img.putpixel((x,y),(color,color,color,255))
	img.save(path + "/" + fileName[:fileName.find('.')] + '_MC.bmp')
	print("Monochrome file has been created")

#takes all colors but red out of a picture
def redFilter(fileName, path):
	im = Image.open(path + '/' + fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			color = pixels[x,y][0] 
			img.putpixel((x,y),(color,0,0,255))
	img.save(path + "/" + fileName[:fileName.find('.')] + '_RF.bmp')
	print("Red Filtered file has been created")

#takes all colors but green out of a picture
def greenFilter(fileName, path):
	im = Image.open(path + '/' + fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			color = pixels[x,y][1] 
			img.putpixel((x,y),(0,color,0,255))
	img.save(path + "/" + fileName[:fileName.find('.')] + '_GF.bmp')
	print("Green Filtered file has been created")

#takes all colors but blue out of a picture
def blueFilter(fileName, path):
	im = Image.open(path + '/' + fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			color = pixels[x,y][2] 
			img.putpixel((x,y),(0,0,color,255))
	img.save(path + "/" + fileName[:fileName.find('.')] + '_BF.bmp')
	print("Blue Filtered file has been created")

#inverts colors of images
def colorInvert(fileName, path):
	im = Image.open(path + '/' + fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			R = pixels[x,y][0]
			G = pixels[x,y][1]
			B = pixels[x,y][2]
			img.putpixel((x,y),(-R % 255,-G % 255,-B % 255,255))
	img.save(path + "/" + fileName[:fileName.find('.')] + '_inverted.bmp')
	print("Inverted file has been created")

#idk
def test(fileName, path):
	im = Image.open(path + '/' + fileName)
	pixels = im.load()
	width = im.size[0];
	height = im.size[1];
	global img
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	for x in range(width):
		for y in range(height):
			R = pixels[x,y][0]
			G = pixels[x,y][1]
			B = pixels[x,y][2]
			img.putpixel((x,y),(2*R % 255,int(G/2) % 255,int(B/2) % 255,255))
	img.save(path + "/" + fileName[:fileName.find('.')] + '_test.bmp')
	print("Test file has been created")