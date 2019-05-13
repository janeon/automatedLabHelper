





import picture2
import math
import random

def MakeCopy(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    copy = picture2.Picture(width,height)
    for x in range(0, width - 1):
        for y in range (0, height - 1):
            (R,G,B) = pic.getPixelColor(x,y)
            copy.setPixelColor(x,y,R,G,B)
    return copy
    
def Greyscale(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for x in range(0, width - 1):
        for y in range (0, height - 1):
            R = pic.getPixelRed(x,y)
            G = pic.getPixelGreen(x,y)
            B = pic.getPixelBlue(x,y)
            avg = (R + G + B)/3
            pic.setPixelRed(x,y,avg)
            pic.setPixelGreen(x,y,avg)
            pic.setPixelBlue(x,y,avg)
    pic.display()
    input()

def Posterize(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for x in range(0, width - 1):
        for y in range (0, height - 1):
            R = pic.getPixelRed(x,y)
            G = pic.getPixelGreen(x,y)
            B = pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,((R+16)//32) * 32)
            pic.setPixelGreen(x,y,((G+16)//32) * 32)
            pic.setPixelBlue(x,y,((B+16)//32) * 32)
                
    pic.display()
    input()

def setCol(R ,G ,B):
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return (R, G, B)
    
def ChangeBrightness(pic):
    n = input("Enter an integer: ")
    width = pic.getWidth()
    height = pic.getHeight()
    for x in range(0, width - 1):
        for y in range (0, height - 1):
            (R,G,B) = pic.getPixelColor(x,y)
            (R, G, B) = setCol(R + n, G + n, B + n)
            pic.setPixelColor(x,y,R, G, B)
    pic.display()
    input()
    
def IncreaseContrast(pic):
    n = input("Enter an integer: ")
    width = pic.getWidth()
    height = pic.getHeight()
    for x in range(0, width - 1):
        for y in range (0, height - 1):
            (R,G,B) = pic.getPixelColor(x,y)
            (R, G, B) = setCol(R+((R-128)*2), G+((G-128)*2), B+((B-128)*2))
            pic.setPixelColor(x,y,R, G, B)
    pic.display()
    input()
    
def MirrorHorizontally(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for y in range (0, height - 1):
        for x in range(0, width/2):
            (R,G,B) = pic.getPixelColor(x,y)
            pic.setPixelColor(width -x -1,y,R, G, B)
    pic.display()
    input()

def ScrollHorizontally(pic):
    n = input("Enter a number: ")
    copy = MakeCopy(pic)
    width = pic.getWidth()
    height = pic.getHeight()
    for y in range (0, height - 1):
        for x in range(0, width - 1):
            (R,G,B) = copy.getPixelColor(x,y)
            pic.setPixelColor((x+n)%width,y,R, G, B)
    pic.display()
    input()
    
def MysteryEffect1(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for y in range (0, height - 1):
        for x in range(0, width/2):
            (R,G,B) = pic.getPixelColor(x,y)
            pic.setPixelColor(width -x -1,y,R, G, B)
    for y in range (0, height):
        for x in range(0, width):
            (R,G,B) = pic.getPixelColor(x,y)
            pic.setPixelColor(x,height - y -1,R, G, B)
    pic.display()
    input()
    
def Flip(pic):
    copy = MakeCopy(pic)
    width = pic.getWidth()
    height = pic.getHeight()
    for y in range (0, height - 1):
        for x in range(0, width - 1):
            (R,G,B) = copy.getPixelColor(x,y)
            pic.setPixelColor(width-x-1,y,R, G, B)
    pic.display()
    input()
    
def Rotate180(pic):
    copy = MakeCopy(pic)
    width = pic.getWidth()
    height = pic.getHeight()
    for y in range (0, height):
        for x in range(0, width):
            (R,G,B) = copy.getPixelColor(x,y)
            pic.setPixelColor(width-x -1,height - y -1,R, G, B)
    pic.display()
    input()
    
def Zoom(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    copy = MakeCopy(pic)
    for y in range (0, height):
        for x in range(0, width):
            (R,G,B) = copy.getPixelColor((x/2)+width/4,(y/2)+height/4)
            pic.setPixelColor(x,y,R,G,B)
    pic.display()
    input()
    
def Negate(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for i in range(0,width-1):
        for j in range (0,height-1):
            r, g, b =pic.getPixelColor(i,j)
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    input()
    

def MysteryEffect2(pic):
    copyp = MakeCopy(pic)
    width = pic.getWidth()
    height = pic.getHeight()
    for x in range (0,width-1,2):
        for y in range (0,height-1,2):
            R = random.randint(0,255)
            G = random.randint(0,255)
            B = random.randint(0,255)
            pic.setPixelColor(x,y,R,G,B)
    pic.display()
    input()
    
def ColorChannel(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for i in range(0,width-1):
        for j in range (0,height-1):
            r, g, b = pic.getPixelColor(i,j)
            b = g
            g = r
            r = b
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    input()
    
def Blur(pic):
    copyp = MakeCopy(pic)
    width = pic.getWidth()
    height = pic.getHeight()
    for x in range (1,width-1):
        for y in range (1,height-1):
            r=0
            b=0
            g=0
            for xc in range (x-1,x+2):
                for yc in range (y-1,y+2):
                    r = copyp.getPixelRed(xc,yc) + r
                    g = copyp.getPixelGreen(xc,yc) + g
                    b = copyp.getPixelBlue(xc,yc) + b
            avgR = r/9
            avgB = b/9
            avgG = g/9
            pic.setPixelColor(x,y,avgR,avgG,avgB)
    pic.display()
    input()
    
def main():
    try:
        print "Welcome to our amazing  picture editer!"
        pic = raw_input("Enter a file name: ")
    except:
        pic = raw_input("Oops that didn't work. Enter a file name: ")
    pic = picture2.Picture(pic)
    done = False
    while not done:
        options = "Scroll Horizontally, Flip Horizontally, Mirror Horizontally, Negative, Greyscale, Cycle Color Channels, Zoom, Posterize, Change Brightness, Increase Contrast, Blur, Rotate 180, Mystery Effect1 or Mystery Effect2"
        print options
        choice = raw_input("Choose an effect from the options above or quit to exit: ")
        if choice == "quit":
            done = True
        elif choice == "Greyscale":
            Greyscale(pic)
        elif choice == "Posterize":
            Posterize(pic)
        elif choice == "Change Brightness":
            ChangeBrightness(pic)
        elif choice == "Increase Contrast":
            IncreaseContrast(pic)
        elif choice == "Mirror Horizontally":
            MirrorHorizontally(pic)
        elif choice == "Scroll Horizontally":
            ScrollHorizontally(pic)
        elif choice == "Mystery Effect1":
            MysteryEffect1(pic)
        elif choice == "Flip Horizontally":
            Flip(pic)
        elif choice == "Rotate 180":
            Rotate180(pic)
        elif choice == "Zoom":
            Zoom(pic)
        elif choice == "Mystery Effect2":
            MysteryEffect2(pic)
        elif choice == "Negative":
            Negate(pic)
        elif choice == "Cycle Color Channels":
            ColorChannel(pic)
        elif choice == "Blur":
            Blur(pic)
                   
main()
            
    