#testing
import os, randomImageMaker, transformations, filters


path = 'images'
if(os.path.exists(path) == False):
	os.mkdir(path)
	print("images Directory Created Successfully")

width = height = 100
#randomized pixels
randomImageMaker.r1(width,height)
randomImageMaker.r2(width,height)
randomImageMaker.r3(width,height)
randomImageMaker.r4(width,height)
randomImageMaker.r5(width,height)
randomImageMaker.r6(width,height)
randomImageMaker.r7(width,height)
randomImageMaker.r8(width,height)
randomImageMaker.r9(width,height)
randomImageMaker.r10(width,height)
randomImageMaker.r11(width,height)
#plaid
randomImageMaker.p1(width,height)
randomImageMaker.p2(width,height)
randomImageMaker.rSquare(width,height,'p')
randomImageMaker.repeated(width,height,'p')
#transformations
transformations.randFlipYGif('r8.bmp',path)
transformations.randFlipXGif('r8.bmp',path)
#filters
filters.monochrome('r11.bmp',path)
filters.redFilter('r11.bmp',path)
filters.greenFilter('r11.bmp',path)
filters.blueFilter('r11.bmp',path)
filters.colorInvert('r11.bmp',path)
filters.test('r11.bmp',path)
#add photos
transformations.addSameDimPhotos('r11_RF.bmp','r11_GF.bmp',path,path)
transformations.addSameDimPhotos('r11_BF.bmp','r11_RF_plus_r11_GF.bmp',path,path)
transformations.addPhotos('p.bmp','r11.bmp',path,path)