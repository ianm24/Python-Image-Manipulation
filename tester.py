#testing
import os, randomColors, transformImage


path = 'images'
testPath = 'test'
# if(os.path.exists(path) == False):
# 	os.mkdir(path)
# 	print("images Directory Created Successfully")
# if(os.path.exists(testPath) == False):
# 	os.mkdir(testPath)
# 	print("test Directory Created Successfully")

width = height = 100
#randomized pixels
randomColors.r1(width,height)
randomColors.r2(width,height)
randomColors.r3(width,height)
randomColors.r4(width,height)
randomColors.r5(width,height)
randomColors.r6(width,height)
randomColors.r7(width,height)
randomColors.r8(width,height)
randomColors.r9(width,height)
randomColors.r10(width,height)
randomColors.r11(width,height)
# #plaid
randomColors.p1(width,height)
randomColors.p2(width,height)
randomColors.rSquare(width,height,'p')
randomColors.repeated(width,height,'p')
#transformations
transformImage.randFlipYGif('r8.bmp',path)
transformImage.randFlipXGif('r8.bmp',path)
# #filters
transformImage.monochrome('r11.bmp',path)
transformImage.redFilter('r11.bmp',path)
transformImage.greenFilter('r11.bmp',path)
transformImage.blueFilter('r11.bmp',path)
transformImage.colorInvert('r11.bmp', path)
# #add photos
transformImage.addPhotos('r11_RF.bmp','r11_GF.bmp',path,path)
transformImage.addPhotos('r11_BF.bmp','r11_RF_plus_r11_GF.bmp',path,path)