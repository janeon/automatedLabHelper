







import picture2

import random

def main():

    
    print ""
    print "Hello there!"
    print "Today is your lucky day! You have found an image manipulation program"
    
    try:
        fileName = raw_input("Please enter the image file you'd like loaded: ")
        pic = picture2.Picture(fileName)
        pic.display()
    except IOError:
        print "That's not an acceptable file!"
        return
    
    try:
        xStr = 0
        while xStr != "":  
            print ""
            print "Here are your image manipulation options: "
            print "1. Flip Horizontally"
            print "2. Mirror Horizontally"
            print "3. Scroll Horizontally"
            print "4. Make Negative"
            print "5. Make Grayscale"
            print "6. Color Cycle Channels"
            print "7. Zoom"
            print "8. Posterize"
            print "9. Change Brightness"
            print "10. Increase Contrast"
            print "11. Blur"
            print "12. Rotate 180 degrees"
            print "13. Old TV Look"
            print "14. Lose Red Color"
            xStr = eval(raw_input("Enter the number of the manipulation you would like done (Enter if none): "))
            
            if xStr == 1:
                flip(pic)
                pic.display()
            if xStr == 2:
                mirror(pic)
                pic.display()
            if xStr == 3:
                scroll(pic)
                pic.display()
            if xStr == 4:
                negative(pic)
                pic.display()
            if xStr == 5:
                gray(pic)
                pic.display()
            if xStr == 6:
                colorcycle(pic)
                pic.display()
            if xStr == 7:
                zoom(pic)
                pic.display()
            if xStr == 8:
                poster(pic)
                pic.display()
            if xStr == 9:
                brightness(pic)
                pic.display()
            if xStr == 10:
                contrast(pic)
                pic.display()
            if xStr == 11:
                blur(pic)
                pic.display()
            if xStr == 12:
                rotate(pic)
                pic.display()
            if xStr == 13:
                pixly(pic)
                pic.display()
            if xStr == 14:
                nored(pic)
                pic.display()
            if xStr < 1 or xStr > 14:
                print "That's not an option"
    except SyntaxError:
        print ""
        print "Thanks for using this program!"
        print ""
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def copy(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    picCopy = picture2.Picture(w,h)
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            picCopy.setPixelColor(x,y,red1,green1,blue1)
    return picCopy
    
def flip(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,(w)/2):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            
            red2 = pic.getPixelRed((w-1)-x,y)
            green2 = pic.getPixelGreen((w-1)-x,y)
            blue2 = pic.getPixelBlue((w-1)-x,y)
            pic.setPixelColor((w-1)-x,y,red1,green1,blue1)
            pic.setPixelColor(x,y,red2,green2,blue2)

def mirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,(w)/2):
        for y in range(0,h-1):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            pic.setPixelColor((w-1)-x,y,red1,green1,blue1)

def scroll(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    picCopy = copy(pic)
    n = eval(raw_input("Enter the number of pixels: "))
    for x in range(0,w):
        for y in range(0,h):
            red1 = picCopy.getPixelRed(x,y)
            green1 = picCopy.getPixelGreen(x,y)
            blue1 = picCopy.getPixelBlue(x,y)
            pic.setPixelColor((x+n)%w,y,red1,green1,blue1)

def negative(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            pic.setPixelColor(x,y,255-red1,255-green1,255-blue1)

def gray(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            avg = (red1 + green1 + blue1)/3
            pic.setPixelColor(x,y,avg,avg,avg)

def colorcycle(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            green1 = pic.getPixelRed(x,y)
            blue1 = pic.getPixelGreen(x,y)
            red1 = pic.getPixelGreen(x,y)
            pic.setPixelColor(x,y,red1,green1,blue1)

def zoom(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = copy(pic)
    for x in range(0,w):
        for y in range(0,h):
            r,g,b = pic2.getPixelColor(w//4 + x//2, h//4 + y//2)
            pic.setPixelColor(x,y,r,g,b)

def poster(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            red2 = red1 - red1%32
            green1 = pic.getPixelGreen(x,y)
            green2 = green1 - green1%32
            blue1 = pic.getPixelBlue(x,y)
            blue2 = blue1 - blue1%32
            pic.setPixelColor(x,y,red2,green2,blue2)

def brightness(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    n = eval(raw_input("Enter the change in brightness you so desire: "))
    for x in range(0,w-1):
        for y in range(0,h-1):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            pic.setPixelColor(x,y,red1+n,green1+n,blue1+n)

def contrast(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            if red1 > 128:
                red2 = red1 + (red1-128)*2
            if red1 < 128:
                red2 = red1 - (128-red1)*2
                
            if green1 > 128:
                green2 = green1 + (green1-128)*2
            if green1 < 128:
                green2 = green1 - (128-green1)*2
                
            if blue1 > 128:
                blue2 = blue1 + (blue1-128)*2
            if blue1 < 128:
                blue2 = blue1 - (128-blue1)*2
                
            pic.setPixelColor(x,y,red2,green2,blue2)

def blur(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    picCopy = copy(pic)
    for x in range(0,w):
        for y in range(0,h):                  
            if x == 0 and y != 0 and y != h-1:
                r2,g2,b2 = picCopy.getPixelColor(x,y-1)
                r3,g3,b3 = picCopy.getPixelColor(x+1,y-1)
                r5,g5,b5 = picCopy.getPixelColor(x,y)
                r6,g6,b6 = picCopy.getPixelColor(x+1,y)
                r8,g8,b8 = picCopy.getPixelColor(x,y+1)
                r9,g9,b9 = picCopy.getPixelColor(x+1,y+1)
                r = (r2+r3+r5+r6+r8+r9)/6
                g = (g2+g3+g5+g6+g8+g9)/6
                b = (b2+b3+b5+b6+b8+b9)/6
                pic.setPixelColor(x,y,r,g,b)
            if y == 0 and x != 0 and x != w-1:
                r4,g4,b4 = picCopy.getPixelColor(x-1,y)
                r5,g5,b5 = picCopy.getPixelColor(x,y)
                r6,g6,b6 = picCopy.getPixelColor(x+1,y)
                r7,g7,b7 = picCopy.getPixelColor(x-1,y+1)
                r8,g8,b8 = picCopy.getPixelColor(x,y+1)
                r9,g9,b9 = picCopy.getPixelColor(x+1,y+1)
                r = (r4+r5+r6+r7+r8+r9)/6
                g = (g4+g5+g6+g7+g8+g9)/6
                b = (b4+b5+b6+b7+b8+b9)/6
                pic.setPixelColor(x,y,r,g,b)
            if x == w-1 and y != 0 and y != h-1:
                r1,g1,b1 = picCopy.getPixelColor(x-1,y-1)
                r2,g2,b2 = picCopy.getPixelColor(x,y-1)
                r4,g4,b4 = picCopy.getPixelColor(x-1,y)
                r5,g5,b5 = picCopy.getPixelColor(x,y)
                r7,g7,b7 = picCopy.getPixelColor(x-1,y+1)
                r8,g8,b8 = picCopy.getPixelColor(x,y+1)
                r = (r1+r2+r4+r5+r7+r8)/6
                g = (g1+g2+g4+g5+g7+g8)/6
                b = (b1+b2+b4+b5+b7+b8)/6
                pic.setPixelColor(x,y,r,g,b)
            if y == w-1 and x != w-1 and x != 0:
                r1,g1,b1 = picCopy.getPixelColor(x-1,y-1)
                r2,g2,b2 = picCopy.getPixelColor(x,y-1)
                r3,g3,b3 = picCopy.getPixelColor(x+1,y-1)
                r4,g4,b4 = picCopy.getPixelColor(x-1,y)
                r5,g5,b5 = picCopy.getPixelColor(x,y)
                r6,g6,b6 = picCopy.getPixelColor(x+1,y)
                r = (r1+r2+r3+r4+r5+r6)/6
                g = (g1+g2+g3+g4+g5+g6)/6
                b = (b1+b2+b3+b4+b5+b6)/6
                pic.setPixelColor(x,y,r,g,b)
            if x != 0 and x != w-1 and y != 0 and y != h-1:
                r1,g1,b1 = picCopy.getPixelColor(x-1,y-1)
                r2,g2,b2 = picCopy.getPixelColor(x,y-1)
                r3,g3,b3 = picCopy.getPixelColor(x+1,y-1)
                r4,g4,b4 = picCopy.getPixelColor(x-1,y)
                r5,g5,b5 = picCopy.getPixelColor(x,y)
                r6,g6,b6 = picCopy.getPixelColor(x+1,y)
                r7,g7,b7 = picCopy.getPixelColor(x-1,y+1)
                r8,g8,b8 = picCopy.getPixelColor(x,y+1)
                r9,g9,b9 = picCopy.getPixelColor(x+1,y+1)
                r = (r1+r2+r3+r4+r5+r6+r7+r8+r9)/9
                g = (g1+g2+g3+g4+g5+g6+g7+g8+g9)/9
                b = (b1+b2+b3+b4+b5+b6+b7+b8+b9)/9
                pic.setPixelColor(x,y,r,g,b)
    
def rotate(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    picCopy = copy(pic)
    for x in range(0,w):
        for y in range(0,h):
            red1 = picCopy.getPixelRed(x,y)
            green1 = picCopy.getPixelGreen(x,y)
            blue1 = picCopy.getPixelBlue(x,y)
            pic.setPixelColor((w-1)-x,(h-1)-y,red1,green1,blue1)

def pixly(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            pic.setPixelColor(x,y,red1 + random.randint(-60,60),green1 + random.randint(-60,60),blue1 + random.randint(-60,60))

def nored(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w):
        for y in range(0,h):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            
            pic.setPixelColor(x,y,0,green1,blue1)

main()
