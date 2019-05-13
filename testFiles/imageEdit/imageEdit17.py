








import random
import math
import picture2


def pict():
    while True:
        picChoice = raw_input("Welcome to the wonderful world of editing! Please  name a picture file that you would like to edit. ")
        try:
            return picture2.Picture(picChoice)
        except:
            print "The file you attempted to load does not seem to be accessible. Please try again. "
print""
pic = pict()


w = pic.getWidth()
h = pic.getHeight()
pic2 = picture2.Picture(w,h)



def pict2(pic):
    for i in range(w):
        for j in range(h):
            copyPix = pic.getPixelColor(i,j)
            pic2.setPixelColor(i,j,copyPix[0],copyPix[1],copyPix[2])
    return pic2
pic2 = pict2(pic)
pic1 = pict2(pic)

def main():
    print""    
    while True:
        edit = raw_input("What image manipulator would you like to run on your image? Your options are:   flip, mirror, scroll, negative, grayscale, color cycle, zoom, posterize, bright, contrast, blur, rotate, or you can go with one of my custom treats, ominously  labeled surprise and surprise2. Or, if you're done editing, just hit enter to   exit the editor. ")
        if edit == "flip" or edit == "Flip":
            pic = flip()
            pic2 = pict2(pic1)
        if edit == "mirror" or edit == "Mirror":
            pic = mirror()
            pic2 = pict2(pic1)
        if edit == "scroll" or edit == "Scroll":
            pic = scroll()
            pic2 = pict2(pic1)
        if edit == "negative" or edit == "Negative":
            pic = negative()
            pic2 = pic1
        if edit == "grayscale" or edit == "Grayscale" or edit == "greyscale" or edit == "Greyscale":
            pic = grayscale()
            pic2 = pic1
        if edit == "Color cycle" or edit == "color cycle" or edit == "Color Cycle":
            pic = colorCycle()
            pic2 = pic1
        if edit == "zoom" or edit == "Zoom":
            pic = zoom()
            pic2 = pic1
        if edit == "posterize" or edit == "Posterize":
            pic = posterize()
            pic2 = pic1
        if edit == "bright" or edit == "Bright":
            pic = bright()
            pic2 = pic1
        if edit == "contrast" or edit == "Contrast":
            pic = contrast()
            pic2 = pic1
        if edit == "blur" or edit == "Blur":
            pic = blur()
            pic2 = pic1
        if edit == "rotate" or edit == "Rotate":
            pic = rotate()
            pic2 = pic1  
        if edit == "surprise" or edit == "Surprise":
            pic = surprise()
            pic2 = pic1 
        if edit == "surprise2" or edit == "Surprise2" or edit == "surprise 2" or edit == "Surprise 2":
            pic = surprise2()
            pic2 = pic1  
        if edit == "":
            return
        else:
            print "Hmm. I'm sorry, it would seem that you've put in a command that, well, isn't    available. Try again, and maybe try entering one of the commands listed? kthx. "
    


def flip():
    for i in range(w-1):
        for j in range(h-1):
            temp = pic.getPixelColor(i, j)
            pic2.setPixelColor(w-i-1,j,temp[0],temp[1],temp[2])
    pic2.display()
    raw_input()
    return pic2


def mirror():
    for i in range(w/2):
        for j in range(h-1):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor(w-i-1,j,temp[0],temp[1],temp[2])
    pic2.display()
    raw_input()
    return pic2


def negative():
    for i in range(w-1):
        for j in range(h-1):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor(i,j,255-temp[0],255-temp[1],255-temp[2])
    pic2.display()
    raw_input()
    return pic2


def scroll():
    try:
       n = input("How many pixels to the right would you like to scroll your image? ")
    except:
        print "Try again if you like, but you need to enter a number between 0 and 255. "
        return
    for i in range(w):
        for j in range(h):
            temp = pic.getPixelColor(i,j)
            if i + n >= w:
                pic2.setPixelColor((i + n) - w, j, temp[0], temp[1], temp[2])
            else:
                pic2.setPixelColor(i + n, j, temp[0], temp[1], temp[2])
    pic2.display()
    raw_input()
    return pic2


def grayscale():
    for i in range(w):
        for j in range(h):
            temp = pic.getPixelColor(i,j)
            temp = ((int(temp[0])+int(temp[1])+int(temp[2]))/3)
            pic2.setPixelColor(i,j,temp,temp,temp)
    pic2.display()
    raw_input()
    return pic2


def colorCycle():
    for i in range(w):
        for j in range(h):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor(i,j,temp[2],temp[0],temp[1])
    pic2.display()
    raw_input()
    return pic2


def zoom():
    for i in range(w/4,((3*w)/4)):
        for j in range(h/4,((3*h)/4)):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor((i-(w/4))*2,((j-(h/4))*2),temp[0],temp[1],temp[2])
            pic2.setPixelColor(((i-(w/4))*2)+1,((j-(h/4))*2),temp[0],temp[1],temp[2])
            pic2.setPixelColor(((i-(w/4))*2),((j-(h/4))*2)+1,temp[0],temp[1],temp[2])
            pic2.setPixelColor(((i-(w/4))*2)+1,((j-(h/4))*2)+1,temp[0],temp[1],temp[2])
    pic2.display()
    raw_input()
    return pic2


def posterize():
    for i in range(w):
        for j in range(h):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor(i,j,32*(temp[0]//32),32*(temp[1]//32),32*(temp[2]//32))
    pic2.display()
    raw_input()
    return pic2


def bright():
    n = input("How much would you like to increase the brightness by? Please enter a value between 1 and 255. You could enter 0, but that would be stupid. ")
    if n > 255 or n < 0:
        print "... Seriously? Try again, but follow directions this time. "
        bright()
    else:
        for i in range(w):
            for j in range(h):
                r, g, b = pic.getPixelColor(i,j)
                if r+n > 255:
                    r = 255-n
                if g+n > 255:
                    g = 255-n
                if b+n > 255:
                    b = 255-n
                pic2.setPixelColor(i,j,r+n,g+n,b+n)
    pic2.display()
    raw_input()
    return pic2


def contrast():
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i,j)
            r = ((r-128)*2)+128
            if r < 0:
                r = 0
            if r > 255:
                r = 255
            g = ((g-128)*2)+128
            if g < 0:
                g = 0
            if g > 255:
                g = 255
            b = ((b-128)*2)+128
            if b < 0:
                b = 0
            if b > 255:
                b = 255
            pic2.setPixelColor(i,j,r,g,b)
    pic2.display()
    raw_input()
    return pic2


def blur():
    for i in range(w):
        for j in range(h):
            if i+1 >= w:
                i = i-1
            if i-1 < 0:
                i = i+1
            if j+1 >= h:
                j = j-1
            if j-1 < 0:
                j = j+1
            r0, g0, b0 = pic.getPixelColor(i,j)
            r1, g1, b1 = pic.getPixelColor(i+1,j)
            r2, g2, b2 = pic.getPixelColor(i-1,j)
            r3, g3, b3 = pic.getPixelColor(i,j+1)
            r4, g4, b4 = pic.getPixelColor(i,j-1)
            r5, g5, b5 = pic.getPixelColor(i+1,j+1)
            r6, g6, b6 = pic.getPixelColor(i+1,j-1)
            r7, g7, b7 = pic.getPixelColor(i-1,j+1)
            r8, g8, b8 = pic.getPixelColor(i-1,j-1)
            r = (r0+r1+r2+r3+r4+r5+r6+r7+r8)/9
            g = (g0+g1+g2+g3+g4+g5+g6+g7+g8)/9
            b = (b0+b1+b2+b3+b4+b5+b6+b7+b8)/9
            pic2.setPixelColor(i,j,r,g,b)
    pic2.display()
    raw_input()
    return pic2


def rotate():
    for i in range(w):
        for j in range(h):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor(w-1-i, h-1-j, temp[0], temp[1], temp[2])
    pic2.display()
    raw_input()
    return pic2


def surprise():
    for i in range(w):
        for j in range(h):
            temp = pic.getPixelColor(i,j)
            pic2.setPixelColor(w-1-i,h-1-j,255-(32*(temp[0]//32)),255-(32*(temp[1]//32)),255-(32*(temp[2]//32)))
    pic2.display()
    raw_input()
    return pic2

def surprise2():
    for i in range(0,w,2):
        for j in range(0,h,2):
            r, g, b = pic.getPixelColor(i,j)
            if r < 75:
                r = random.randint(200,255)
            if g < 75:
                g = random.randint(200,255)
            if b < 75:
                b = random.randint(200,255)
            pic2.setPixelColor(i,j,r,g,b)
    pic2.display()
    raw_input()
    return pic2

main()

raw_input("Thanks for using our incredible image editor! ")
