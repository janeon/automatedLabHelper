







import picture2

def copy(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            r,g,b=pic.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    return pic2

def Negative(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):
        for y in range(h):
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,255-r)
            pic.setPixelGreen(x,y,255-g)
            pic.setPixelBlue(x,y,255-b)
    pic.display()
    
def GrayScale(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):
        for y in range(h):
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,(r+g+b)/3)
            pic.setPixelGreen(x,y,(r+g+b)/3)
            pic.setPixelBlue(x,y,(r+g+b)/3)
    pic.display()

def Mirror(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range((w-1)//2,w):
        for y in range(h):
            r,g,b=pic.getPixelColor(w-1-x,y)
            pic.setPixelColor(x,y,r,g,b) 
    pic.display()
    
def FlipHorizontally(pic):
    pic2=copy(pic)
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w/2):
        for y in range(h):
            r,g,b=pic.getPixelColor(w-1-x,y)      
            pic.setPixelColor(x,y,r,g,b)
    for x in range(w/2,w):
        for y in range(h):
            r,g,b=pic2.getPixelColor(w-1-x,y)
            pic.setPixelColor(x,y,r,g,b)
    pic.display()
    
def ScrollHorizontally(pic):
    pic2=copy(pic)
    Goodinput=False
    while not Goodinput:
        try:
            d=input("Please enter number d: ")
            w=pic.getWidth()
            h=pic.getHeight()
            for x in range(d, w):
                for y in range(h):
                    r,g,b=pic2.getPixelColor(x-d,y)
                    pic.setPixelColor(x,y,r,g,b)
            for x in range(d):
                for y in range(h):
                    r,g,b=pic2.getPixelColor(x+w-d,y)
                    pic.setPixelColor(x,y,r,g,b)
            Goodinput=True
        except IndexError:
            print"You cannot scroll the image by a number of pixels greater than the width, or by a negative number of pixels."
    pic.display()

def CycleColorChannels(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):
        for y in range(h):
            r=pic.getPixelBlue(x,y)
            g=pic.getPixelRed(x,y)
            b=pic.getPixelGreen(x,y)       
            pic.setPixelRed(x,y,r)
            pic.setPixelGreen(x,y,g)
            pic.setPixelBlue(x,y,b)
    pic.display()

def ChangeBrightness(pic):
    goodinput=False
    while not goodinput:
        n=input("Please enter an integer from -255 to 255 (positive for increase, negative for decrease): ")
        if n>-255 and n<255:
            goodinput=True
        else:
            print"Invalid input. Please enter a number in the specified range"
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):
        for y in range(h):
            r=pic.getPixelRed(x,y)+n
            g=pic.getPixelGreen(x,y)+n
            b=pic.getPixelBlue(x,y)+n
            pic.setPixelRed(x,y,r)
            pic.setPixelGreen(x,y,g)
            pic.setPixelBlue(x,y,b)
    pic.display()

def IncreaseContrast(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):
        for y in range(h):
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            r=r+(r-128)*2
            g=g+(g-128)*2
            b=b+(b-128)*2
            pic.setPixelRed(x,y,r)
            pic.setPixelGreen(x,y,g)
            pic.setPixelBlue(x,y,b)
    pic.display()

def Posterize(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):
        for y in range(h):
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            r=(r//32)*32
            g=(g//32)*32
            b=(b//32)*32
            pic.setPixelRed(x,y,r)
            pic.setPixelGreen(x,y,g)
            pic.setPixelBlue(x,y,b)
    pic.display()
    
def Rotate180Degrees(pic):
    pic2=copy(pic)
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w/2):
        for y in range(h/2):
            r,g,b=pic.getPixelColor(w-1-x,h-1-y)
            pic.setPixelColor(x,y,r,g,b)
    for x in range(w/2,w):
        for y in range(h/2):
            r,g,b=pic.getPixelColor(w-1-x,h-1-y)
            pic.setPixelColor(x,y,r,g,b)
    for x in range(w/2):
        for y in range(h/2,h):
            r,g,b=pic2.getPixelColor(w-1-x,h-1-y)
            pic.setPixelColor(x,y,r,g,b)
    for x in range(w/2,w):
        for y in range(h/2,h):
            r,g,b=pic2.getPixelColor(w-1-x,h-1-y)
            pic.setPixelColor(x,y,r,g,b)
    pic.display()

def Blur(pic):
    pic2=copy(pic)
    w=pic.getWidth()
    h=pic.getHeight()
    for x in [0]:
        for y in [0]:
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x+1,y)
            r3,g3,b3=pic2.getPixelColor(x,y+1)
            r4,g4,b4=pic2.getPixelColor(x+1,y+1)         
            r=(r1+r2+r3+r4)/4
            g=(g1+g2+g3+g4)/4
            b=(b1+b2+b3+b4)/4
            pic.setPixelColor(x,y,r,g,b)
    for x in [0]:
        for y in [h-1]:
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x+1,y)
            r3,g3,b3=pic2.getPixelColor(x,y-1)
            r4,g4,b4=pic2.getPixelColor(x+1,y-1)
            r=(r1+r2+r3+r4)/4
            g=(g1+g2+g3+g4)/4
            b=(b1+b2+b3+b4)/4
            pic.setPixelColor(x,y,r,g,b)
    for x in [w-1]:
        for y in [0]:
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x,y+1)
            r3,g3,b3=pic2.getPixelColor(x-1,y)
            r4,g4,b4=pic2.getPixelColor(x-1,y+1)
            r=(r1+r2+r3+r4)/4
            g=(g1+g2+g3+g4)/4
            b=(b1+b2+b3+b4)/4
            pic.setPixelColor(x,y,r,g,b)
    for x in [w-1]:
        for y in [h-1]:
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x,y-1)
            r3,g3,b3=pic2.getPixelColor(x-1,y)
            r4,g4,b4=pic2.getPixelColor(x-1,y-1)
            r=(r1+r2+r3+r4)/4
            g=(g1+g2+g3+g4)/4
            b=(b1+b2+b3+b4)/4
            pic.setPixelColor(x,y,r,g,b)
    for x in range(1,w-1):
        for y in [0]:
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x,y+1)
            r3,g3,b3=pic2.getPixelColor(x+1,y)
            r4,g4,b4=pic2.getPixelColor(x-1,y+1)
            r5,g5,b5=pic2.getPixelColor(x+1,y)
            r6,g6,b6=pic2.getPixelColor(x-1,y+1)
            r=(r1+r2+r3+r4+r5+r6)/6
            g=(g1+g2+g3+g4+g5+g6)/6
            b=(b1+b2+b3+b4+b5+b6)/6
            pic.setPixelColor(x,y,r,g,b)
    for x in range(1,w-1):
        for y in [h-1]:
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x,y-1)
            r3,g3,b3=pic2.getPixelColor(x+1,y)
            r4,g4,b4=pic2.getPixelColor(x-1,y-1)
            r5,g5,b5=pic2.getPixelColor(x+1,y)
            r6,g6,b6=pic2.getPixelColor(x-1,y-1)
            r=(r1+r2+r3+r4+r5+r6)/6
            g=(g1+g2+g3+g4+g5+g6)/6
            b=(b1+b2+b3+b4+b5+b6)/6
            pic.setPixelColor(x,y,r,g,b)
    for x in [0]:
        for y in range(1,h-1):
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x+1,y)
            r3,g3,b3=pic2.getPixelColor(x,y-1)
            r4,g4,b4=pic2.getPixelColor(x+1,y-1)
            r5,g5,b5=pic2.getPixelColor(x,y+1)
            r6,g6,b6=pic2.getPixelColor(x+1,y+1)
            r=(r1+r2+r3+r4+r5+r6)/6
            g=(g1+g2+g3+g4+g5+g6)/6
            b=(b1+b2+b3+b4+b5+b6)/6
            pic.setPixelColor(x,y,r,g,b)
    for x in [w-1]:
        for y in range(1,h-1):
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x-1,y)
            r3,g3,b3=pic2.getPixelColor(x,y-1)
            r4,g4,b4=pic2.getPixelColor(x-1,y-1)
            r5,g5,b5=pic2.getPixelColor(x,y+1)
            r6,g6,b6=pic2.getPixelColor(x-1,y+1)
            r=(r1+r2+r3+r4+r5+r6)/6
            g=(g1+g2+g3+g4+g5+g6)/6
            b=(b1+b2+b3+b4+b5+b6)/6
            pic.setPixelColor(x,y,r,g,b)
    for x in range(1,w-1):
        for y in range(1,h-1):
            r1,g1,b1=pic2.getPixelColor(x,y)
            r2,g2,b2=pic2.getPixelColor(x,y+1)
            r3,g3,b3=pic2.getPixelColor(x,y-1)
            r4,g4,b4=pic2.getPixelColor(x-1,y)
            r5,g5,b5=pic2.getPixelColor(x-1,y+1)
            r6,g6,b6=pic2.getPixelColor(x-1,y-1)
            r7,g7,b7=pic2.getPixelColor(x+1,y)
            r8,g8,b8=pic2.getPixelColor(x+1,y+1)
            r9,g9,b9=pic2.getPixelColor(x+1,y-1)
            r=(r1+r2+r3+r4+r5+r6+r7+r8+r9)/9
            g=(g1+g2+g3+g4+g5+g6+g7+g8+g9)/9
            b=(b1+b2+b3+b4+b5+b6+b7+b8+b9)/9
            pic.setPixelColor(x,y,r,g,b)
    pic.display()

def Zoom(pic):
    pic2=copy(pic)
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(0,w,2):
        for y in range(0,h,2):
            r,g,b=pic2.getPixelColor((w-1)/4+x/2,(h-1)/4+y/2)
            pic.setPixelColor(x,y,r,g,b)
            pic.setPixelColor(x,y+1,r,g,b)
            pic.setPixelColor(x+1,y,r,g,b)
            pic.setPixelColor(x+1,y+1,r,g,b)
    pic.display()

def InsideOut(pic):
    pic2=copy(pic)
    w=pic.getWidth()
    h=pic.getHeight()     
    for x in range((w-1)/2):
        for y in range((h-1)/2-(h-1)*x/(w-1)):
            r,g,b=pic2.getPixelColor((w-1)/2-x,(h-1)/2-y)      
            pic.setPixelColor(x,y,r,g,b)
    for x in range((w-1)/2,w):
        for y in range(-(h-1)/2+(h-1)*x/(w-1)):
            r,g,b=pic2.getPixelColor((w-1)/2+w-1-x,(h-1)/2-y)      
            pic.setPixelColor(x,y,r,g,b)
    for x in range((w-1)/2):
        for y in range((h-1)/2+(h-1)*x/(w-1),h):
            r,g,b=pic2.getPixelColor((w-1)/2-x,(h-1)/2+h-1-y)      
            pic.setPixelColor(x,y,r,g,b)
    for x in range((w-1)/2,w):
        for y in range((h-1)*3/2-(h-1)*x/(w-1),h):
            r,g,b=pic2.getPixelColor((w-1)/2+w-1-x,(h-1)/2+h-1-y)      
            pic.setPixelColor(x,y,r,g,b)
    pic.display()
    
def FadeToGrayScale(pic):
    pic2=copy(pic)
    w=pic.getWidth()
    h=pic.getHeight()
    for x in range(w):  
        for y in range(h):
            r=pic2.getPixelRed(x,y)
            g=pic2.getPixelGreen(x,y)
            b=pic2.getPixelBlue(x,y)
            av=(r+g+b)/3
            if r>av:
                r=r-(r-av)*x/w
            if r==av:
                r=av
            if r<av:
                r=r+(av-r)*x/w
            if g>av:
                g=g-(g-av)*x/w
            if g==av:
                g=av
            if g<av:
                g=g+(av-g)*x/w
            if b>av:
                b=b-(b-av)*x/w
            if b==av:
                b=av
            if b<av:
                b=b+(av-b)*x/w   
            pic.setPixelRed(x,y,r)
            pic.setPixelGreen(x,y,g)
            pic.setPixelBlue(x,y,b)
    pic.display()

def main():
    print 'Welcome to the Awesome Image Editor!'
    goodInput = False
    while not goodInput:
        try:
            fileName=raw_input("Please enter the image file you'd like loaded: ")
            pic=picture2.Picture(fileName)
            goodInput=True
            pic.display()
        except IOError:
            print "Invalid input. Please don't forget to include file type as well."
    quitPro = False
    invalid = False
    while not quitPro:
        print "This editor has 14 operations corresponding to 14 numbers listed as follows:"
        print "1 - Flips the image horizontally"
        print "2 - Mirrors the image horizontally"
        print "3 - Scrolls the image horizontally by d pixels"
        print "4 - Turns the image negative"
        print "5 - Cycles the image's color channels"
        print "6 - Zooms into the image"
        print "7 - Posterizes the image"
        print "8 - Turns the image into grayscale"
        print "9 - Changes the image's brightness"
        print "10 - Increases the image's contrast"
        print "11 - Blurs the image"
        print "12 - Rotates the image 180 degrees"
        print "13 - Reflects the image across 4 diagonal lines"
        print "14 - Makes the image fade to grayscale gradually"
        print "15 - Exits the editor"
        if invalid:
            command=input("Invalid input. Please type in one of the specified numbers: ")
        else:
            command=input("Type in the number corresponding to the operation you wish to make: ")
        if command==1:
            FlipHorizontally(pic)
            invalid = False
        if command==2:
            Mirror(pic)
            invalid = False
        if command==3:
            ScrollHorizontally(pic)
            invalid = False
        if command==4:
            Negative(pic)
            invalid = False
        if command==5:
            CycleColorChannels(pic)
            invalid = False
        if command==6:
            Zoom(pic)
            invalid = False
        if command==7:
            Posterize(pic)
            invalid = False
        if command==8:
            GrayScale(pic)
            invalid = False
        if command==9:
            ChangeBrightness(pic)
            invalid = False
        if command==10:
            IncreaseContrast(pic)
            invalid = False
        if command==11:
            Blur(pic)
            invalid = False
        if command==12:
            Rotate180Degrees(pic)
            invalid = False
        if command==13:
            InsideOut(pic)
            invalid = False
        if command==14:
            FadeToGrayScale(pic)
            invalid = False
        if command==15:
            quitPro=True
        if command<1 or command>15:
            invalid = True

main()
