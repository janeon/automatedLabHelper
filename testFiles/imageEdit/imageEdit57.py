





import picture2
import random
pic=picture2.Picture("crayons.bmp")
w=pic.getWidth()
h=pic.getHeight()

picCopy=picture2.Picture(w,h)
for i in range(0, w):
    for j in range(0, h):
        temp = pic.getPixelColor(i,j)
        picCopy.setPixelColor(i,j,temp[0],temp[1],temp[2])

def flipHorizontally(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(0, w):
        for j in range(0, h):
            r, g, b=pic.getPixelColor(i, j)
            picCopy.setPixelColor(w-1-i, j, r, g, b)
    picCopy.display()
    input()

def makeGreyscale(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            average=((r+g+b))/3
            picCopy.setPixelColor(i, j, average, average, average)
            
def makeScroll(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    n=input("Please input the number of pixels you would like the image to scroll:")
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            if i+n>=w:
                picCopy.setPixelColor(i+n-w, j, r, g, b)
            else:
                picCopy.setPixelColor(i+n, j, r, g, b)
    picCopy.display()
    input()
    
def makeNegative(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            picCopy.setPixelColor(i, j, (255-r), (255-g), (255-b))
    picCopy.display()
    input()
    
def makeMirror(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(w/2):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            picCopy.setPixelColor((w-1-i), j, r, g, b)
    picCopy.display()
    input()
    
def cycleColors(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            picCopy.setPixelColor(i, j, g, b, r)
    picCopy.display()
    input()
    
def makeZoom(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(0, w-1, 2):
        for j in range(0, h-1, 2):
            r, g, b=pic.getPixelColor(w/4-1+i/4, h/4-1+j/4)
            picCopy.setPixelColor(i, j, r, g, b)
            picCopy.setPixelColor(i+1, j, r, g, b)
            picCopy.setPixelColor(i, j+1, r, g, b)
            picCopy.setPixelColor(i+1, j+1, r, g, b)
    picCopy.display()
    input()
    
def makePosterize(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            picCopy.setPixelColor(i, j, (r//32)*32, (g//32)*32, (b//32)*32)
    picCopy.display()
    input()
    
def changeBrightness(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    n=input("Please input a number you would like to change the brightness by:")
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            if r+n>=255:
                r=255
            if r+n<=0:
                r=0
            if g+n>=255:
                g=255
            if g+n<=0:
                g=0
            if b+n>=255:
                b=255
            if b+n<=0:
                b=0
            picCopy.setPixelColor(i, j, r+n, g+n, b+n)
    picCopy.display()
    input()
    
def increaseContrast(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
            if r>=255:
                r=255
            if r<=0:
                r=0
            if g>=255:
                g=255
            if g<=0:
                g=0
            if b>=255:
                b=255
            if b<=0:
                b=0
            picCopy.setPixelColor(i, j, ((r-128)*2)+128, ((g-128)*2)+128, ((b-128)*2)+128)
    picCopy.display()
    input()
    
def makeBlur(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(0, w-1):
        for j in range(0, h-1):
            numInBounds = 0
            totalR=0
            totalG=0
            totalB = 0

            for x in range(-1,2):
                for y in range(-1,2):
                    if ((i+x) in range(0, w)) and ((j+y) in range(0, h)):
                        numInBounds +=1
                        r, g, b=pic.getPixelColor(i+x, j+y)
                        totalR += r
                        totalG += g
                        totalB += b
            picCopy.setPixelColor(i, j, totalR//numInBounds, totalG//numInBounds, totalB//numInBounds)
    picCopy.display()
    input()
    
def flipHorizontally(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(0, w):
        for j in range(0, h):
            r, g, b=pic.getPixelColor(i, j)
            picCopy.setPixelColor(w-1-i, h-1-j, r, g, b)
    picCopy.display()
    input()
    
def makeAwesome(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(0, w-1, 2):
        for j in range(0, h-1, 2):
            r, g, b=pic.getPixelColor(w/4-1+i/4, h/4-1)
            picCopy.setPixelColor(i, j, r, g, b)
            picCopy.setPixelColor(i+1, j, r, g, b)
            picCopy.setPixelColor(i, j+1, r, g, b)
            picCopy.setPixelColor(i+1, j+1, r, g, b)
    picCopy.display()
    input()
    
def makeAwesomer(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for i in range(w):
        for j in range(0, h-1):
            r, g, b=pic.getPixelColor(i, j)
        
    
    
def main():
    print "Hello! Welcome to my image editor."
    fileName=raw_input("Please pick a file to load in:")
    pic=picture2.Picture(fileName)
    x=True
    while x:
        print("1. Flip horizontally  2. Mirror horizontally  3. Scroll horizontally  4. Make negative  5. Make greyscale  6. Cycle color channels  7. Zoom  8. Posterize  9. Change brightness  10. Increase contrast  11. Blur  12. Rotate 180 degrees  13. Make the picture AWESOME!  14. exit program")
        choice=input("Select the number of the change you would like to apply:")
        if choice=="1":
            flipHorizontally(pic)
        if choice=="2":
            makeMirror(pic)
        if choice=="3":
            makeScroll(pic)
        if choice=="4":
            makeNegative(pic)
        if choice=="5":
            makeGreyscale(pic)
        if choice=="6":
            cycleColors(pic)
        if choice=="7":
            makeZoom(pic)
        if choice=="8":
            makePosterize(pic)
        if choice=="9":
            changeBrightness(pic)
        if choice=="10":
            increaseContrast(pic)
        if choice=="11":
            makeBlur(pic)
        if choice=="12":
            rotate180(pic)
        if choice=="13":
            makeAwesome(pic)
        if choice=="14":
            return
        else:
            print("You suck.  Also, please input number in quotation marks.r")      

main()