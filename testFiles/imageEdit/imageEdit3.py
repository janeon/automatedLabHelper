






import picture2
import math

def main():
    print "Welcome to the image editor"
    goodInput = False
    while not goodInput:
        try:
            File = raw_input("Enter file name: ")
            pic = picture2.Picture(File)
            goodInput = True
        except:
            print "Please enter the file name exactly"
    H = pic.getHeight()
    W = pic.getWidth()
    Exit = False
    effects = ["Flip Horizontally","Mirror Horizontally","Scroll Horizontally","Negative","Grayscale","Cycle Color Channels","Zoom","Posterize","Brightness","Contrast","Blur","Rotate 180 Degrees","Recursion","Quarter Rotation","Exit"]

    while not Exit:
        i = 0
        goodInput = False
        while not goodInput:
            pic.display()
            print
            print "Your options are: \n1.", effects[0],"\n2.", effects[1], "\n3.",effects[2], "\n4.", effects[3],"\n5.", effects[4], "\n6.", effects[5], "\n7.", effects[6], "\n8.", effects[7], "\n9.", effects[8], "\n10.", effects[9], "\n11.", effects[10], "\n12.", effects[11], "\n13.", effects[12], "\n14.", effects[13],"\n15.", effects[14]
            try:
                i = input("Please enter the number of your choice: ")
                print i,effects[i-1]
                goodInput = True
            except:
                print
                print "Please enter a whole number from 1 to 15"
        if i == 1:
            flip(pic,W,H)
        if i == 2:
            mirror(pic,W,H)
        if i == 3:
            scroll(pic,W,H)
        if i == 4:
            negative(pic,W,H)
        if i == 5:
            grayscale(pic,W,H)
        if i == 6:
            cycle(pic,W,H)
        if i == 7:
            zoom(pic,W,H)
        if i == 8:
            posterize(pic,W,H)
        if i == 9:
            brightness(pic,W,H)
        if i == 10:
            contrast(pic,W,H)
        if i == 11:
            blur(pic,W,H)
        if i == 12:
            rotate(pic,W,H)
        if i == 13:
            recursion(pic,W,H)
        if i == 14:
            quarters(pic,W,H)
        if i == 15:
            Exit = True

def flip(pic,W,H):
    pic2 = copy(pic,W,H)
    for y in range(H):
        for x in range(W):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(W-1-x,y,r,g,b)
    pic.display()

def mirror(pic,W,H):
    for y in range(H):
        for x in range(W/2):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(W-1-x,y,r,g,b)
    pic.display()

def scroll(pic,W,H):
    pic2 = copy(pic,W,H)
    d = eval(raw_input("input scroll amount: "))
    for y in range(H):
        for x in range(W):
            r,g,b = pic2.getPixelColor(x,y)
            if -1 < x+d < W:
                pic.setPixelColor(x+d,y,r,g,b)
            elif d > -1:
                pic.setPixelColor(x+d-W,y,r,g,b)
            elif d < 0:
                pic.setPixelColor(x+d+W,y,r,g,b)
    pic.display()

def negative(pic,W,H):
    for y in range(H):
        for x in range(W):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,255-r,255-g,255-b)
    pic.display()

def grayscale(pic,W,H):
    for y in range(H):
        for x in range(W):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,(r+g+b)/3,(r+g+b)/3,(r+g+b)/3)
    pic.display()

def cycle(pic,W,H):
    for y in range(H):
        for x in range(W):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,b,r,g)
    pic.display()

def zoom(pic,W,H):
    pic2 = copy(pic,W,H)
    for y in range(H/4,3*H/4):
        for x in range(W/4,3*W/4):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(2*(x-W/4),2*(y-H/4),r,g,b)
            pic.setPixelColor(2*(x-W/4)+1,2*(y-H/4),r,g,b)
            pic.setPixelColor(2*(x-W/4),2*(y-H/4)+1,r,g,b)
            pic.setPixelColor(2*(x-W/4)+1,2*(y-H/4)+1,r,g,b)
    pic.display()

def posterize(pic,W,H):
    for y in range(H):
        for x in range(W):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,r/32*32,g/32*32,b/32*32)
    pic.display()

def brightness(pic,W,H):
    amt = eval(raw_input("enter integer: "))
    for y in range(H):
        for x in range(W):
            r,g,b = pic.getPixelRed(x,y)+amt,pic.getPixelGreen(x,y)+amt,pic.getPixelBlue(x,y)+amt
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            pic.setPixelColor(x,y,r,g,b)
    pic.display()

def contrast(pic,W,H):
    for y in range(H):
        for x in range(W):
            r,g,b = ((pic.getPixelRed(x,y)-128)*2+128,(pic.getPixelGreen(x,y)-128)*2+128,(pic.getPixelBlue(x,y)-128)*2+128)
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            pic.setPixelColor(x,y,r,g,b)
    pic.display()

def blur(pic,W,H):
    pic2 = copy(pic,W,H)
    for y in range(H):
        for x in range(W):
            d = 1
            if x > 0 and y > 0:
                r1,g1,b1 = pic2.getPixelColor(x-1,y-1)
                d = d+1
            else:
                r1,g1,b1 = 0,0,0
            if y > 0:
                r2,g2,b2 = pic2.getPixelColor(x,y-1)
                d = d+1
            else:
                r2,g2,b2 = 0,0,0
            if x < W-1 and y > 0:
                r3,g3,b3 = pic2.getPixelColor(x+1,y-1)
                d = d+1
            else:
                r3,g3,b3 = 0,0,0
            if x > 0:
                r4,g4,b4 = pic2.getPixelColor(x-1,y)
                d = d+1
            else:
                r4,g4,b4 = 0,0,0
            r5,g5,b5 = pic2.getPixelColor(x,y)
            if x < W-1:
                r6,g6,b6 = pic2.getPixelColor(x+1,y)
                d = d+1
            else:
                r6,g6,b6 = 0,0,0
            if x > 0 and y < H-1:
                r7,g7,b7 = pic2.getPixelColor(x-1,y+1)
                d = d+1
            else:
                r7,g7,b7 = 0,0,0
            if y < H-1:
                r8,g8,b8 = pic2.getPixelColor(x,y+1)
                d = d+1
            else:
                r8,g8,b8 = 0,0,0
            if x < W-1 and y < H-1:
                r9,g9,b9 = pic2.getPixelColor(x+1,y+1)
                d = d+1
            else:
                r9,g9,b9 = 0,0,0
            r,g,b = (r1+r2+r3+r4+r5+r6+r7+r8+r9)/d,(g1+g2+g3+g4+g5+g6+g7+g8+g9)/d,(b1+b2+b3+b4+b5+b6+b7+b8+b9)/d
            pic.setPixelColor(x,y,r,g,b)
    pic.display()

def rotate(pic,W,H):
    pic2 = copy(pic,W,H)
    for y in range(H):
        for x in range(W):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(W-1-x,H-1-y,r,g,b)
    pic.display()

def recursion(pic,W,H):
    i = eval(raw_input("enter number of iterations: "))
    while i > 0:
        pic2 = copy(pic,W,H)
        for y in range(H/2):
            for x in range(W/2):
                r,g,b = pic2.getPixelColor(2*x,2*y)
                pic.setPixelColor(x+W/4,y+H/4,r,g,b)
        i = i-1
    pic.display()

def quarters(pic,W,H):
    pic2 = copy(pic,W,H)
    for y in range(H/2):
        for x in range(W/2):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x+W/2,y,r,g,b)
    for y in range(H/2,H):
        for x in range(W/2,W):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x-W/2,y,r,g,b)
    for y in range(H/2,H):
        for x in range(W/2):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x,y-H/2,r,g,b)
    for y in range(H/2):
        for x in range(W/2,W):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x,y+H/2,r,g,b)
    pic.display()

def copy(pic,W,H):
    pic2 = picture2.Picture(W,H)
    for y in range(H):
        for x in range(W):
            r,g,b = pic.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    return pic2




main()