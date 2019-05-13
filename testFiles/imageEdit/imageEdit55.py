



import picture2
import math

pic = picture2.Picture("crayons.bmp")

edit = raw_input("Please enter the image file you would like to choose")
h = pic.getHeight()
w = pic.getWidth()

pic2 = picture2.Picture(w,h)

for i in range(w):
    for j in range(h):
        copyPix=pic.getPixelColor(i,j)
        pic2.setPixelColor(i,j,copyPix[0], copyPix[1], copyPix[2])

def flip():
    
    
   
    for i in range(0, w-1):
        for j in range(0, (h-1)):
            temp = pic.getPixelColor(i, j)
            pic2.setPixelColor(w-i-1,j,temp[0],temp[1],temp[2])
        
flip()

def scroll():
    for i in range(0, w-1):
        for j in range(0, (h-1)):
            temp = pic.getPixelColor(i, j)
            pic.setPixelColor(w-)
        




pic2.display()
raw_input()

