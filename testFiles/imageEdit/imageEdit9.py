





import picture2
from random import randint


def copy(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            r,g,b = pic.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    return pic2

def neg(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w):
        for y in range(h):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,255-r,255-g,255-b)
    pic.display()
    try:
        input()
    except:
        print

def gray(pic) :
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w):
        for y in range(h):
            r,g,b = pic.getPixelColor(x,y)
            ave = (r+g+b)/3
            pic.setPixelColor(x,y,ave,ave,ave)
    pic.display()
    try:
        input()
    except:
        print

def cycle(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w):
        for y in range(h):
            r,g,b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,b,r,g)
    pic.display()
    try:
        input()
    except:
        print

def bright(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    goodInput = False
    while not goodInput:
        try:
            change = input("How much do you want to change? ")
            
            
            for x in range(w):
                for y in range(h):
                    r,g,b = pic.getPixelColor(x,y)
                    pic.setPixelColor(x,y,r+change,g+change,b+change)
            goodInput = True
        except Exception as e:
            print e
    pic.display()
    try:
        input()
    except:
        print

def con(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w):
        for y in range(h):
            r,g,b = pic.getPixelColor(x,y)
            r = (r-128)*2+r
            g = (g-128)*2+g
            b = (b-128)*2+b
            pic.setPixelColor(x,y,r,g,b)
    pic.display()
    try:
        input()
    except:
        print

def pos(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    posCon = 32
    for x in range(w):
        for y in range(h):
            r,g,b = pic.getPixelColor(x,y)
            if r%posCon > (posCon/2):
                r = ((r//posCon)) * posCon
            else:
                r = (r//posCon) * posCon
            if g%posCon > (posCon/2):
                g = ((g//posCon)) * posCon
            else:
                g = (g//posCon) * posCon
            if b%posCon > (posCon/2):
                b = ((b//posCon)) * posCon
            else:
                b = (b//posCon) * posCon
            pic.setPixelColor(x,y,r,g,b)
            
    pic.display()
    try:
        input()
    except:
        print

def flip(pic):
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w):
        for y in range(h):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(w-x-1,y,r,g,b)
    pic.display()
    try:
        input()
    except:
        print

def mirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w/2, w):
        for y in range(h):
            r,g,b = pic.getPixelColor(w-x,y)
            pic.setPixelColor(x,y,r,g,b)
    pic.display()
    try:
        input()
    except:
        print

def scroll(pic):
    
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    goodInput = False
    while not goodInput:
        try:
            d = input("What's the distance do you want to move the picture to right? ")
            for x in range(w):
                for y in range(h):
                    r,g,b = pic2.getPixelColor(x,y)
                    pic.setPixelColor((x+d)%w,y,r,g,b)
            goodInput = True
        except Exception as e:
            print e
    pic.display()
    try:
        input()
    except:
        print

def zoom(pic):
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w/4, 3*w/4):
        for y in range(h/4, 3*h/4):
            r,g,b = pic2.getPixelColor(x,y)
            for i in range(2):
                for j in range(2):
                    pic.setPixelColor((x-w/4)*2+i,(y-h/4)*2+j,r,g,b)
    pic.display()
    try:
        input()
    except:
        print

def rotate(pic):
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w):
        for y in range(h):
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x,h-y-1,r,g,b)
    pic.display()
    try:
        input()
    except:
        print

def blur(pic):
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    
    
    for x in range(1,w-1):
        for y in range(1,h-1):
            rsum,gsum,bsum = 0,0,0
            ra,ga,ba = 0,0,0
            for i in range(-1,2):
                for j in range(-1,2):
                    rsum = rsum + pic2.getPixelRed(x+i,y+j)
                    gsum = gsum + pic2.getPixelGreen(x+i,y+j)
                    bsum = bsum + pic2.getPixelBlue(x+i,y+j)
            ra = rsum/9
            ga = gsum/9
            ba = bsum/9
            pic.setPixelColor(x,y,ra,ga,ba)
    pic.display()
    try:
        input()
    except:
        print

def random(pic):
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    goodInput = False
    while not goodInput:
        try:
            n = input("What degree you want to mess up the picture?(a number)")
            for x in range(3,w-3):
                for y in range(3,h-3):
                    randx = randint(-3,3)
                    randy = randint(-3,3)
                    r,g,b = pic2.getPixelColor(x,y)
                    pic.setPixelColor(x,y,r+randx*n,g+randy*n,b+randx*n)
            goodInput = True
        except Exception as e:
            print e
    pic.display()
    try:
        input()
    except:
        print

def dot(pic):
    pic2 = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    n = 5
    for x in range(w):
        for y in range(h):
            pic.setPixelColor(x,y,0,0,0)
            r,g,b = pic2.getPixelColor(x,y)
            for i in range(n):
                pic.setPixelColor(i*(x/n/0.8),i*(y/n/0.8),r,g,b)
    pic.display()
    try:
        input()
    except:
        print



def main():
    print
    print "Welcome to this great image editor!!"
    
    goodInput = False
    while not goodInput :
        try:          
            fileName = raw_input("Please enter the image file you'd like loaded: ")
            pic = picture2.Picture(fileName)
            pic.display()
            raw_input ()
            w = pic.getWidth()
            h = pic.getHeight()
            goodInput = True
        except Exception as e:
            print e
    
    goodInput = False
    while not goodInput:
        try:
            print "There are 14 way to edit your picture:"
            print "Flip(flip)"
            print "Mirror(mirror)"
            print "Scroll(scroll)"
            print "Make Negative(neg)"
            print "Make Grayscale(gray)"
            print "CycleColorChannels(ccc)"
            print "Zoom(zoom)"
            print "Posterize(post)"
            print "ChangeBrightness(bri)"
            print "IncreaseContrast(con)"
            print "BlurRotate180Degrees(rotate)"
            print "mess up the picture(random)"
            print "dot the picture(dot)"
            print
            print "Please enter the words in the parenthesis."
            ed = raw_input("What effect do you want to choose?")
            if ed == "flip":
                goodInput = True
                flip(pic)
            elif ed == "mirror":
                goodInput = True
                mirror(pic)
            elif ed == "scroll":
                goodInput = True
                scroll(pic)
            elif ed == "neg":
                neg(pic)
                goodInput = True
            elif ed == "gray":
                gray(pic)
                goodInput = True
            elif ed == "ccc":
                cycle(pic)
                goodInput = True
            elif ed == "zoom":
                zoom(pic)
                goodInput = True
            elif ed == "post":
                pos(pic)
                goodInput = True
            elif ed == "bri":
                bright(pic)
                goodInput = True
            elif ed == "con":
                con(pic)
                goodInput = True
            elif ed == "rotate":
                rotate(pic)
                goodInput = True
            elif ed == "random":
                random(pic)
                goodInput = True
            elif ed == "dot":
                dot(pic)
                goodInput = True
            else:
                print
                print "      Please enter the correct name in the parenthesis."
                print
            while goodInput is True:
                again = raw_input("Do you want to continue editing?(yes/no)")
                if again == "yes":
                    goodInput = False
                if again == "no":
                    print "Thanks for using my Image Editor!"
                    exit()
        except Exception as e:
            print e
main()


