# Program Made By: Ian McDowell
# Started 3 March 2019

from PIL import Image
import glob, os, imageio, random, math, transformImage
path = 'images'
testPath = 'test'

#complete random static
def r1(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r1.bmp')
	for x in xrange(width):
		for y in xrange(height):
			r1 = random.randint(0,255)
			r2 = random.randint(0,255)
			r3 = random.randint(0,255)
			r4 = random.randint(0,255)
			img.putpixel((x,y),(r1,r2,r3,r4))
	print("r1 Pixels Placed")
	img.save(path+'/r1.bmp')

#spottier static
def r2(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r2.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			if(random.randint(1,2) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			img.putpixel((x,y),(r1,r2,r3,r4))
		if(random.randint(1,2) == 1):
			r1 = random.randint(0,255)
			r2 = random.randint(0,255)
			r3 = random.randint(0,255)
			r4 = random.randint(0,255)
	print("r2 Pixels Placed")
	img.save(path+'/r2.bmp')

#small lines static
def r3(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r3.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			if(random.randint(1,25) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			img.putpixel((x,y),(r1,r2,r3,r4))
		if(random.randint(1,25) == 1):
			r1 = random.randint(0,255)
			r2 = random.randint(0,255)
			r3 = random.randint(0,255)
			r4 = random.randint(0,255)
	print("r3 Pixels Placed")
	img.save(path+'/r3.bmp')

#straight vertical lines
def r4(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r4.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			if(random.randint(1,height) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			img.putpixel((x,y),(r1,r2,r3,r4))
		if(random.randint(1,height) == 1):
			r1 = random.randint(0,255)
			r2 = random.randint(0,255)
			r3 = random.randint(0,255)
			r4 = random.randint(0,255)
	print("r4 Pixels Placed")
	img.save(path+'/r4.bmp')

#square-like pattern
def r5(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r5.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			# print(str(x)+" "+str(y))
			if(random.randint(1,height/2) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			where = random.randint(0,1)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
		if(random.randint(1,height/2) == 1):
			r1 = random.randint(0,255)
			r2 = random.randint(0,255)
			r3 = random.randint(0,255)
			r4 = random.randint(0,255)
	print("r5 Pixels Placed")
	img.save(path+'/r5.bmp')

#slightly different square-like patterns
def r6(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r6.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			if(random.randint(1,height/2) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			where = random.randint(0,3)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
			elif(where == 1):
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
			elif(where == 2):
				img.putpixel((x/2,y/2),(r1,r2,r3,r4))
			else:
				img.putpixel((((y*width)/height)/2,((x*height)/width)/2),(r1,r2,r3,r4))
		if(random.randint(1,height/2) == 1):
			r1 = random.randint(0,255)
			r2 = random.randint(0,255)
			r3 = random.randint(0,255)
			r4 = random.randint(0,255)
	print("r6 Pixels Placed")
	img.save(path+'/r6.bmp')

#division of colors based on position
def r7(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r7.bmp')
	r1 = random.randint(100,200)
	r2 = random.randint(100,200)
	r3 = random.randint(100,200)
	r4 = random.randint(100,200)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			if(random.randint(1,height/2) == 1):
				r1 = random.randint(100,200)
				r2 = random.randint(100,200)
				r3 = random.randint(100,200)
				r4 = random.randint(100,200)
			where = random.randint(0,5)
			if(where == 0):
				img.putpixel((x,y),(255,r2,r3,r4))
			elif(where == 1):
				img.putpixel(((y*width)/height,(x*height)/width),(r1,255,r3,r4))
			elif(where == 2):
				img.putpixel((x/2,y/2),(r1,r2,255,r4))
			elif(where == 3):
				img.putpixel((((y*width)/height)/2,((x*height)/width)/2),(r1,r2,r3,255))
			elif(where == 4):
				img.putpixel((x/3,y/3),(255,r2,r3,r4))
			else:
				img.putpixel((((y*width)/height)/3,((x*height)/width)/3),(r1,255,r3,r4))
		if(random.randint(1,height/2) == 1):
			r1 = random.randint(100,200)
			r2 = random.randint(100,200)
			r3 = random.randint(100,200)
			r4 = random.randint(100,200)
	print("r7 Pixels Placed")
	img.save(path+'/r7.bmp')

#further division of colors based on position
def r8(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r8.bmp')
	r1 = random.randint(100,200)
	r2 = random.randint(100,200)
	r3 = random.randint(100,200)
	r4 = random.randint(100,200)
	for x in xrange(width):
		for y in xrange(height):
			# color of loaded bar
			if(random.randint(1,height/2) == 1):
				r1 = random.randint(100,200)
				r2 = random.randint(100,200)
				r3 = random.randint(100,200)
				r4 = random.randint(100,200)
			where = random.randint(0,7)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
			elif(where == 1):
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
			elif(where == 2):
				img.putpixel((x/2,y/2),(r1,255,255,r4))
			elif(where == 3):
				img.putpixel((((y*width)/height)/2,((x*height)/width)/2),(255,r2,255,r4))
			elif(where == 4):
				img.putpixel((3*(x/2)/2,3*(y/2)/2),(255,r2,255,r4))
			elif(where == 5):
				img.putpixel((3*(((y*width)/height)/2)/2,3*(((x*height)/width)/2)/2),(255,255,r3,r4))
			elif(where == 6):
				img.putpixel((x/3,y/3),(255,r2,r3,r4))
			elif(where == 7):
				img.putpixel((((y*width)/height)/3,((x*height)/width)/3),(r1,255,r3,r4))
		if(random.randint(1,height/2) == 1):
			r1 = random.randint(100,200)
			r2 = random.randint(100,200)
			r3 = random.randint(100,200)
			r4 = random.randint(100,200)
	print("r8 Pixels Placed")
	img.save(path+'/r8.bmp')

#more defined r5 square-like patterns
def r9(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r9.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	where = 0
	for x in xrange(width):
		for y in xrange(height):
			if(random.randint(1,height/2) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
				where = 1
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
				where = 0
	print("r9 Pixels Placed")
	img.save(path+'/r9.bmp')

#horizontal lines with slight pattens when x&y are equal or 2 parts of a pixel color are equal
def r10(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r10.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	where = 0
	for x in xrange(width):
		for y in xrange(height):
			if(random.randint(1,height/2) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
			if(r1 == r2 or r1 == r3 or r1 == r4 or r2 == r3 or r2 == r4 or r3 == r4 or x == y):
				where = 0
			else:
				where = 1
	print("r10 Pixels Placed")
	img.save(path+'/r10.bmp')

#random thicknesses of horizontal lines
def r11(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/r11.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	where = 0
	for x in xrange(width):
		for y in xrange(height):
			if(random.randint(1,(height*width)/5) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
			if(r1 == r2 or r1 == r3 or r1 == r4 or r2 == r3 or r2 == r4 or r3 == r4):
				where = 0
			else:
				where = 1
	print("r11 Pixels Placed")
	img.save(path+'/r11.bmp')

#plaid pattern generator
def p1(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(path+'/p1.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	where = 0
	for x in xrange(width):
		for y in xrange(height):
			if(random.randint(1,(height*width)/5) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
				where = 1
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
				where = 0
	print("p1 Pixels Placed")
	img.save(path+'/p1.bmp')

#more intricate plaid
def p2(width,height):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(testPath+'/p2.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	where = 0
	for x in xrange(width):
		for y in xrange(height):
			if(random.randint(1,5*height) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
				where = 1
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
				where = 0
	print("p2 Pixels Placed")
	img.save(path+'/p2.bmp')

def misc(width,height,savename):
	img = Image.new("RGBA",(width, height),(0,0,0,0))
	img.save(testPath+'/'+savename+'.bmp')
	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)
	r4 = random.randint(0,255)
	where = 0
	for x in xrange(width):
		for y in xrange(height):
			if(random.randint(1,(height*width)/5) == 1):
				r1 = random.randint(0,255)
				r2 = random.randint(0,255)
				r3 = random.randint(0,255)
				r4 = random.randint(0,255)
			if(where == 0):
				img.putpixel((x,y),(r1,r2,r3,r4))
				where = 1
			else:
				img.putpixel(((y*width)/height,(x*height)/width),(r1,r2,r3,r4))
				where = 0
	img.save(testPath+'/'+savename+'.bmp')

def rSquare(width,height,savename):
	misc(width/2,height/2,savename)
	transformImage.squareStitch(testPath+'/'+savename+'.bmp')

def repeated(width,height,savename):
	sn = 0
	for x in xrange(10):
		rSquare(width,height,savename+str(sn))
		os.remove(testPath+'/'+savename+str(sn)+'.bmp')
		os.remove(testPath+'/'+savename+str(sn)+'_FlipX.bmp')
		os.remove(testPath+'/'+savename+str(sn)+'_FlipY.bmp')
		os.remove(testPath+'/'+savename+str(sn)+'_FlipY_FlipX.bmp')
		sn += 1