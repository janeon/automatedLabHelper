





import picture2
import random




def getPic() :
    goodpic = False
    while not goodpic :
        fileLoc = raw_input("enter the filename of the image, or \"quit\" to quit: ")
        
        
        
        try:
            pic = picture2.Picture(fileLoc)
            goodpic=True
        except Exception as e:
            if fileLoc=="quit" :
                return 0
            else :
                print "error; try again"
                print e
    return pic


def shell(pic) :
    invar = ""
    while invar != "15" :
        pic.display()
        
        print("choose from the following options:")
        print("1: flip horizontally")
        print("2: mirror horizontally")
        print("3: scroll horizontally")
        print("4: make negative")
        print("5: make grayscale")
        print("6: cycle color channels")
        print("7: zoom")
        print("8: posterize")
        print("9: change brightness")
        print("10: increase contrast")
        print("11: blur")
        print("12: rotate 180 degrees")
        print("13: mystery effect 01")
        print("14: mystery effect 02")
        print("15: quit")
        
        invar = raw_input("what's your pick?")
        
        if invar == "1" :
            flip(pic)
        elif invar == "2" :
            mirror(pic)
        elif invar == "3" :
            scroll(pic)
        elif invar == "4" :
            negative(pic)
        elif invar == "5" :
            grayscale(pic)
        elif invar == "6" :
            cycleColors(pic)
        elif invar == "7" :
            zoom(pic)
        elif invar == "8" :
            posterize(pic)
        elif invar == "9" :
            brighten(pic)
        elif invar == "10" :
            contrast(pic)
        elif invar == "11" :
            blur(pic)
        elif invar == "12" :
            rotate(pic)
        elif invar == "13" :
            mystery01(pic)
        elif invar == "14" :
            mystery02(pic)
        elif invar != "15" :
            print "i don't know what you mean. please just enter a number between 1 and 15"


def copy(pic1, pic2) :
    w, h = pic1.getWidth(),pic1.getHeight()
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = pic1.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    

def flip(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    
    pic2 = picture2.Picture(w,h)
    
    copy(pic, pic2)
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = pic2.getPixelColor(x,y)
            pic.setPixelColor(w-1-x,y,r,g,b)


def mirror(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    for x in range(w//2) : 
        for y in range(h) :
            r, g, b = pic.getPixelColor(x,y)
            pic.setPixelColor(w-1-x,y,r,g,b) 


def scroll(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    try:
        amt = int(eval(raw_input("how many pixels to scroll by: ")))
        
        
        pic2 = picture2.Picture(w,h)
    
        copy(pic, pic2)
        
        for x in range(w) :
            for y in range(h) :
                r, g, b = pic2.getPixelColor(x,y)
                pic.setPixelColor((x+amt)%w,y,r,g,b)
    except Exception as e:
        print "the input is invalid. please enter an integer"
        print type(e)
        print e


def negative(pic) :
    for x in range(pic.getWidth()) :
        for y in range(pic.getHeight()) :
            r, g, b = pic.getPixelColor(x,y)
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pic.setPixelColor(x,y,r,g,b)


def grayscale(pic) :
    for x in range(pic.getWidth()) :
        for y in range(pic.getHeight()) :
            avg = round((pic.getPixelRed(x,y)+pic.getPixelGreen(x,y)+pic.getPixelBlue(x,y))/3)
            pic.setPixelColor(x,y,int(avg),int(avg),int(avg))


def cycleColors(pic) :
    for x in range(pic.getWidth()) :
        for y in range(pic.getHeight()) :
            r, g, b = pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,b,r,g)


def zoom(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    
    zoomie = picture2.Picture(w*2,h*2)
    
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = pic.getPixelColor(x,y)
            zoomie.setPixelColor(x*2,y*2,r,g,b)
            zoomie.setPixelColor(x*2,(y*2)+1,r,g,b)
            zoomie.setPixelColor((x*2)+1,(y*2),r,g,b)
            zoomie.setPixelColor((x*2)+1,(y*2)+1,r,g,b)
            
    
    
    
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = zoomie.getPixelColor(x+w//4,y+w//4)
            pic.setPixelColor(x,y,r,g,b)


def posterize(pic) :
    for x in range(pic.getWidth()) :
        for y in range(pic.getHeight()) :
            r, g, b = pic.getPixelColor(x,y)
            r = (r // 32) * 32
            g = (g // 32) * 32
            b = (b // 32) * 32
            pic.setPixelColor(x,y,r,g,b)


def brighten(pic) :
    try:
        d = eval(raw_input("enter an integer to alter the brightness: "))
        for x in range(pic.getWidth()) :
            for y in range(pic.getHeight()) :
                r, g, b = pic.getPixelColor(x,y)
                r = max(0,min(255,r + d))   
                g = max(0,min(255,g + d))
                b = max(0,min(255,b + d))
                pic.setPixelColor(x,y,r,g,b)
    except Exception as e:
        print "the input is invalid. please enter an integer"
        print type(e)
        print e


def contrast(pic) :
    for x in range(pic.getWidth()) :
        for y in range(pic.getHeight()) :
            r, g, b = pic.getPixelColor(x,y)
            r = min(255,(125 + (r-125)*2))
            g = min(255,(125 + (g-125)*2))
            b = min(255,(125 + (b-125)*2))
            pic.setPixelColor(x,y,r,g,b)
            

def blur(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    
    pic2 = picture2.Picture(w,h)
    
    copy(pic, pic2)
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = blurAvg(pic2,x,y)
            pic.setPixelColor(x,y,r,g,b)


def blurAvg(pic,x,y) :
    w, h = pic.getWidth(),pic.getHeight()
    
    r,g,b = 0,0,0
    
    
    cnt = 0
    
    for i in range(3) :
        for j in range(3) :
            if ((x+i-1) >= 0) and ((x+i-1) < w) and ((y+j-1) >= 0) and ((y+j-1) < h) :
                cnt = cnt + 1
                r = r + pic.getPixelRed(x+i-1,y+j-1)
                g = g + pic.getPixelGreen(x+i-1,y+j-1)
                b = b + pic.getPixelBlue(x+i-1,y+j-1)
    
    r = r // cnt
    g = g // cnt
    b = b // cnt
    
    return r,g,b



def rotate(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    
    pic2 = picture2.Picture(w,h)
    copy(pic, pic2)
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = pic2.getPixelColor(x,y)
            pic.setPixelColor(w-1-x,h-1-y,r,g,b)


def mystery01(pic) :
    w, h = pic.getWidth(),pic.getHeight()
    
    
    pic2 = picture2.Picture(w,h)
    copy(pic, pic2)
    
    for x in range(w) :
        for y in range(h) :
            r, g, b = pic2.getPixelColor(x,y)
            r1, r2 = random.randint(0,10), random.randint(0,10)
            pic.setPixelColor((x+r1-5)%w,(y+r2-5)%h,r,g,b)


def mystery02(pic) :
     w, h = pic.getWidth(),pic.getHeight()
     
     for x in range(w) :
        for y in range(h) :
            r, g, b = pic.getPixelColor(x,y)
            r = max(0,min(255,(r + random.randint(0,40)-20)))
            g = max(0,min(255,(g + random.randint(0,40)-20)))
            b = max(0,min(255,(b + random.randint(0,40)-20)))
            pic.setPixelColor(x,y,r,g,b)

def main() :
    print "time to change some images"
    
    pic = getPic()
    
    if pic != 0 : 
        shell(pic)
        
    
main()
    
