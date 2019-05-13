











import picture2

def intro():
    print 
    print "Welcome to the reasonably functional (but still cheap) image editting genie"
    print "This program can perform the following functions:"
    print
    print "Change Contrast, and Brightness"
    print "Make the picture Negative, Grayscale, Posterize or Cycle the colors."
    print "Flip, Rotate, Blur, Zoom, Scroll or Mirror the image."
    print
    print"I also have two surprises. Aptly titled", """, "surprise1", """, "and", """, "surprise2", """
    print "If you would like to revert to the original image. Enter", """, "revert", """

def main():     
    picture = raw_input("Enter the image file you wish to change or otherwise manipulate: ")
    try:
        moredata = "yes"
        
        pic = picture2.Picture(picture)
        h = pic.getHeight()
        w = pic.getWidth() 
    
        copy = picture2.Picture(w,h)
        m = copy.getHeight
        p = copy.getWidth
        
        intro()
        while moredata[0] == "y":
            
            pic = pic
            
            n = raw_input("What would you like to do to your image?: ")
            if n == "1":
                contrast(h, w, pic)
            elif n == "2":
                pic = picture2.Picture(picture)
                pic.display()
                raw_input
                print
            elif n == "3":
                brightness(h, w, pic)
            elif n == "4":
                negative(h, w, pic)
            elif n == "5":
                grayscale(h, w, pic)
            elif n == "6":
                posterize(h, w, pic)
            elif n == "7":
                cycle(h, w, pic)
            elif n == "8":
                flip(h, w, pic, copy)
            elif n == "9":
                rotate(h, w, pic, copy)
            elif n == "10":
                blur(h, w, pic, copy)
            elif n == "11":
                zoom(h, w, pic, copy)
            elif n == "12":
                scrolling(h, w, pic, copy)
            elif n == "13":
                mirror(h, w, pic, copy)
            elif n == "14":
                homebrew2(h, w, pic, copy)
            elif n =="15":
                homebrew1(h, w, pic, copy)
            else:
                print
                print "I am fickle. You must command me properly"
                print
                print "Be sure to use lowercase letters (I despise upper case)"
                print "and be sure to use a proper command"
                print "(negative, grayscale, posterize, cycle, flip, rotate, zoom, blur)"
                
            moredata = raw_input("Would you like to change the picture more (Y/N)?: ")
        print
        print "Have a nice day"
    except IndexError:
        print
        print "...So is that a yes or a no?"
        print "I am quite impatient. Goodbye"
    except IOError:
        print
        print "Apparently that file does not exist. Be sure the file you want is in the proper directory, so that I may utilize it"

    

    
    
    

def negative(h, w, pic):
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            negr = abs(255 - r)
            negg = abs(255 - g)
            negb = abs(255 - b)
            pic.setPixelColor(x, y, negr, negg, negb)
    pic = pic
    pic.display()
    raw_input()
    print

def grayscale(h, w, pic):
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            GrayR = (r + g + b)/3
            GrayG = (r + g + b)/3
            GrayB = (r + g + b)/3
            pic.setPixelColor(x, y, GrayR, GrayG, GrayB)
    pic = pic
    pic.display()
    raw_input()
    print

def cycle(h, w, pic):
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, b, r, g)
    pic = pic
    pic.display()
    raw_input()
    print

def brightness(h, w, pic):
    change = eval(raw_input("Change the brightness. Positive or Negative integers: "))
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            r2 = r + change
            if r2 > 255:
                r2 = 255
            elif r2 < 0:
                r2 = 0
            g2 = g + change
            if g2 > 255:
                g2 = 255
            elif g2 < 0:
                g2 = 0
            b2 = b + change
            if b2 > 255:
                b2 = 255
            elif b2 < 0:
                b2 = 0
            pic.setPixelColor(x, y, r2, g2, b2)
    pic = pic
    pic.display()
    raw_input()
    print

def contrast(h, w, pic):
    contrast = 0
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            if r != 128:
                contrast = (r - 128) * 2
                r2 = r + contrast
                if r2 < 0:
                    r2 = 0
                elif r2 > 255:
                    r2 = 255
            if g != 128:
                contrast = (g - 128) *2
                g2 = g + contrast
                if g2 < 0:
                    g2 = 0
                if g2 > 255:
                    g2 = 255
            if b != 128:
                contrast = (g - 128) *2
                b2 = b + contrast
                if b2 < 0:
                    b2 = 0
                elif b2 > 255:
                    b2 = 255
            pic.setPixelColor(x, y, r2, g2, b2)
    pic = pic
    pic.display()
    raw_input()
    print


def scrolling(h, w, pic, copy):       
    scroll = eval(raw_input("How far will you scroll the image?: "))
    try:
        for x in range(0, w):
            for y in range(0, h):
                r, g, b = pic.getPixelColor(x, y)
                scrollX = x + scroll
                if scrollX > w-1:
                    scrollX = (scrollX - w)
                copy.setPixelColor(scrollX, y, r, g, b)
        for x in range(0, w):
            for y in range(0, h):
                r2, g2, b2 = copy.getPixelColor(x, y)
                pic.setPixelColor(x, y, r2, g2, b2)
        pic.display()
        raw_input()
        print
    except IndexError:
        print
        print "You have scrolled too far. My magic is not capable of handling such vast scrolling"

def rounding(x, base = 32):
    return int(base * round(float(x)/base))
def posterize(h, w, pic):
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, rounding(r), rounding(g), rounding(b))
    pic = pic
    pic.display()
    raw_input()
    print

def mirror(h, w, pic, copy):
    for x in range(0, (w/2)):
        for y in range(0, h):
            r, b, g = pic.getPixelColor(x, y)
            d = (w-1) - x
            copy.setPixelColor(x, y, r, g, b)
            copy.setPixelColor(d, y, r, g, b)
    for x in range(0, w):
        for y in range(0, h):
            r2, b2, g2 = copy.getPixelColor(x, y)
            pic.setPixelColor(x, y, r2, g2, b2)
    pic.display()
    raw_input()
    print

def flip(h, w, pic, copy):
    for x in range(0, w):
        for y in range(0, h):
            r, b, g = pic.getPixelColor(x, y)
            d = (h-1) - y
            copy.setPixelColor(x, d, r, g, b)
    for x in range(0, w):
        for y in range(0, h):
            r2, b2, g2 = copy.getPixelColor(x, y)
            pic.setPixelColor(x, y, r2, g2, b2)
    pic.display()
    raw_input()
    print

def rotate(h, w, pic, copy):
    for x in range(0, w):
        w2 = (w-1) - x
        for y in range(0, h):
            r, b, g = pic.getPixelColor(x, y)
            d = (h-1) - y
            copy.setPixelColor(w2, d, r, g, b)
    for x in range(0, w):
        for y in range(0, h):
            r2, b2, g2 = copy.getPixelColor(x, y)
            pic.setPixelColor(x, y, r2, g2, b2)
    pic.display()
    raw_input()
    print

def zoom(h, w, pic, copy):
    for x in range(0, (w)):
        for y in range(0, (h)):
            r, g, b = pic.getPixelColor(w/4+x//2, h/4+y//2)
            copy.setPixelColor(x, y, r, g, b)
    for x in range(0, w):
        for y in range(0, h):
            r2 = copy.getPixelRed(x, y)
            g2 = copy.getPixelGreen(x, y)
            b2 = copy.getPixelBlue(x, y)
            pic.setPixelColor(x, y, r2, g2, b2)
    pic.display()
    raw_input()
    print

def blur(h, w, pic, copy):
    pic2 = copy
    for x in range(0,(w)):
        for y in range(0,(h)):
            r, g, b = pic.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    for x in range(0,w):
        for y in range(0,h):
            
            
            
            
            
            
            
            
            
            if x==0 and y==0:
                c1=pic2.getPixelColor(x,y)
                c2=pic2.getPixelColor(x+1,y)
                c3=pic2.getPixelColor(x,y+1)
                c4=pic2.getPixelColor(x+1,y+1)
                R=(c1[0]+c2[0]+c3[0]+c4[0])/4
                G=(c1[1]+c2[1]+c3[1]+c4[1])/4
                B=(c1[2]+c2[2]+c3[2]+c4[2])/4
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif x==w-1 and y==0:
                c1=pic2.getPixelColor(x,y)
                c3=pic2.getPixelColor(x,y+1)
                c5=pic2.getPixelColor(x-1,y)
                c9=pic2.getPixelColor(x-1,y+1)
                R=(c1[0]+c3[0]+c5[0]+c9[0])/4
                G=(c1[1]+c3[1]+c5[1]+c9[1])/4
                B=(c1[2]+c3[2]+c5[2]+c9[2])/4
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif x==0 and y==h-1:
                c1=pic2.getPixelColor(x,y)
                c2=pic2.getPixelColor(x+1,y)
                c6=pic2.getPixelColor(x,y-1)
                c8=pic2.getPixelColor(x+1,y-1)
                R=(c1[0]+c2[0]+c6[0]+c8[0])/4
                G=(c1[1]+c2[1]+c6[1]+c8[1])/4
                B=(c1[2]+c2[2]+c6[2]+c8[2])/4
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif x==w-1 and y==h-1:
                c1=pic2.getPixelColor(x,y)
                c5=pic2.getPixelColor(x-1,y)
                c6=pic2.getPixelColor(x,y-1)
                c7=pic2.getPixelColor(x-1,y-1)
                R=(c1[0]+c5[0]+c6[0]+c7[0])/4
                G=(c1[1]+c5[1]+c6[1]+c7[1])/4
                B=(c1[2]+c5[2]+c6[2]+c7[2])/4
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif x==0:
                c1=pic2.getPixelColor(x,y)
                c2=pic2.getPixelColor(x+1,y)
                c3=pic2.getPixelColor(x,y+1)
                c4=pic2.getPixelColor(x+1,y+1)
                c6=pic2.getPixelColor(x,y-1)
                R=(c1[0]+c2[0]+c3[0]+c4[0]+c6[0])/5
                G=(c1[1]+c2[1]+c3[1]+c4[1]+c6[1])/5
                B=(c1[2]+c2[2]+c3[2]+c4[2]+c6[2])/5
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif y==0:
                c1=pic2.getPixelColor(x,y)
                c2=pic2.getPixelColor(x+1,y)
                c3=pic2.getPixelColor(x,y+1)
                c4=pic2.getPixelColor(x+1,y+1)
                c5=pic2.getPixelColor(x-1,y)
                R=(c1[0]+c2[0]+c3[0]+c4[0]+c5[0])/5
                G=(c1[1]+c2[1]+c3[1]+c4[1]+c5[1])/5
                B=(c1[2]+c2[2]+c3[2]+c4[2]+c5[2])/5
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif x==w-1:
                c1=pic2.getPixelColor(x,y)
                c3=pic2.getPixelColor(x,y+1)
                c5=pic2.getPixelColor(x-1,y)
                c6=pic2.getPixelColor(x,y-1)
                c7=pic2.getPixelColor(x-1,y-1)
                c9=pic2.getPixelColor(x-1,y+1)
                R=(c1[0]+c3[0]+c5[0]+c6[0]+c7[0]+c9[0])/6
                G=(c1[1]+c3[1]+c5[1]+c6[1]+c7[1]+c9[1])/6
                B=(c1[2]+c3[2]+c5[2]+c6[2]+c7[2]+c9[2])/6
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            elif y==h-1:
                c1=pic2.getPixelColor(x,y)
                c2=pic2.getPixelColor(x+1,y)
                c5=pic2.getPixelColor(x-1,y)
                c6=pic2.getPixelColor(x,y-1)
                c7=pic2.getPixelColor(x-1,y-1)
                c8=pic2.getPixelColor(x+1,y-1)
                R=(c1[0]+c2[0]+c5[0]+c6[0]+c7[0]+c8[0])/6
                G=(c1[1]+c2[1]+c5[1]+c6[1]+c7[1]+c8[1])/6
                B=(c1[2]+c2[2]+c5[2]+c6[2]+c7[2]+c8[2])/6
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
            else:
                c1=pic2.getPixelColor(x,y)
                c2=pic2.getPixelColor(x+1,y)
                c3=pic2.getPixelColor(x,y+1)
                c4=pic2.getPixelColor(x+1,y+1)
                c5=pic2.getPixelColor(x-1,y)
                c6=pic2.getPixelColor(x,y-1)
                c7=pic2.getPixelColor(x-1,y-1)
                c8=pic2.getPixelColor(x+1,y-1)
                c9=pic2.getPixelColor(x-1,y+1)
                R=(c1[0]+c2[0]+c3[0]+c4[0]+c5[0]+c6[0]+c7[0]+c8[0]+c9[0])/9
                G=(c1[1]+c2[1]+c3[1]+c4[1]+c5[1]+c6[1]+c7[1]+c8[1]+c9[1])/9
                B=(c1[2]+c2[2]+c3[2]+c4[2]+c5[2]+c6[2]+c7[2]+c8[2]+c9[2])/9
                pic2.setPixelRed(x,y,R)
                pic2.setPixelGreen(x,y,G)
                pic2.setPixelBlue(x,y,B)
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic2.getPixelColor(x, y)
            pic.setPixelColor(x, y, r, g, b)
    pic.display()
    raw_input
    print

def homebrew1(h, w, pic, copy):
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pic.getPixelColor(x, y)
            copy.setPixelColor(x/5, y/5, r, g, b)
            copy.setPixelColor(x/3, y/3, r, g, b)
            copy.setPixelColor(x/2, y/2, r, g, b)
            copy.setPixelColor(x/1.5, y/1.5, r, g, b)
            copy.setPixelColor(x/1.25, y/1.25, r, g, b)
            copy.setPixelColor(x, y, r, g, b)
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = copy.getPixelColor(x, y)
            pic.setPixelColor(x, y, r, g, b)
    pic.display()
    raw_input()
    print

def homebrew2(h, w, pic, copy):
    for x in range(0, w/2):
        for y in range(0, h):
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            dx = (w-1) - x
            copy.setPixelColor(x, y, r, g, b)
            copy.setPixelColor(dx, y, r, g, b)
    for x in range(0, w):
        for y in range(0, h/2):
            r2 = copy.getPixelRed(x, y)
            g2 = copy.getPixelGreen(x, y)
            b2 = copy.getPixelBlue(x, y)
            dy = (h-1) - y
            pic.setPixelColor(x, y, r2, g2, b2)
            pic.setPixelColor(x, dy, r2, g2, b2)
    pic.display()
    raw_input()
    print


main()
