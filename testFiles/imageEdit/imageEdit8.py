





import picture2
import random

def main():
    print "Welcome to my image editor!"
    x = 1
    while x == 1: 
        print
        print "Please choose from one of the following files:"
        print "(1) Flip Horizontally"
        print "(2) Mirror Horizontally"
        print "(3) Scroll Horizontally"
        print "(4) Negative"
        print "(5) Grayscale"
        print "(6) Cycle Color Channels"
        print "(7) Zoom"
        print "(8) Posterize"
        print "(9) Change Brightness"
        print "(10) Increase Contrast"
        print "(11) Blur"
        print "(12) Pretty! (sort of randomize colors)"
        print "(13) Tiled(4)"
        
        try :
            fileName = eval(raw_input("Please enter the number corresponding to the operation you wish to complete: "))
            if fileName >= 1 and fileName <= 13:
                x = 2
            else:
                5 / 0
            
        except Exception:
            print
            print
            print "Please enter a valid number from the list."
    pic = picture2.Picture("crayons.bmp")
    w = pic.getWidth()
    h = pic.getHeight()

    if fileName == 1: 
        pic = flip(w, h, pic)
        pic.display()
        input()
    if fileName == 2:
        pic = mirror(w, h, pic)
        pic.display()
        input()
    if fileName == 3:
        d = eval(raw_input("How many pixels would you like to shift the image? "))
        pic = scroll(w, h, d, pic)
        pic.display()
        input()
    if fileName == 4:
        pic = negative(w, h, pic)
        pic.display()
        input()
    if fileName == 5:
        pic = grayscale(w, h, pic)
        pic.display()
        input()
    if fileName == 6:
        pic = cycle(w, h, pic)
        pic.display()
        input()
    if fileName == 7:
        d = eval(raw_input("By what factor would you like to zoom the image? "))
        print "I'm a computer! I can do what I want! I think I'll zoom by... 2!"
        pic = zoom(w, h, pic)
        pic.display()
        input()
    if fileName == 8:
        pic = posterize(w, h, pic)
        pic.display()
        input()
    if fileName == 9:
        d = eval(raw_input("How much do you want to increase the brightness? Negative numbers work too! "))
        pic = brightness(w, h, d, pic)
        pic.display()
        input()
    if fileName == 10:
        pic = contrast(w, h, pic)
        pic.display()
        input()
    if fileName == 11:
        pic = blur(w, h, pic)
        pic.display()
        input()
    if fileName == 12:
        d = eval(raw_input("Put in a value for the amount of pixel color randomization: "))
        pic = pretty(w, h, d, pic)
        pic.display()
        input()
    if fileName == 13:
        pic = tiled(w , h, pic)
        pic.display()
        input()
        
    
       
def picCopy(w, h, pic) :
    pic2 = picture2.Picture(w, h)
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            pic2.setPixelColor(x, y, r1, g1, b1)
    return pic2
    
    
    

def flip(w, h, pic) : 
    for y in range(h-1) :
        for x in range (w//2) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            r2, g2, b2 = pic.getPixelColor((w - 1) - x, y)
            pic.setPixelColor(x, y, r2, g2, b2) 
            pic.setPixelColor((w - 1) - x, y, r1, g1, b1) 
    return(pic)

def mirror(w, h, pic) :
    for y in range(h-1) :
        for x in range (w//2, 0, -1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            pic.setPixelColor((w - 1) - x, y, r1, g1, b1)
    return(pic)

def scroll(w, h, d, pic) :
    pic2 = picCopy(w, h, pic)
    for y in range(h-1) :
        for x in range (w-1) :
            newColor = (x+d)
            while newColor > w - 1:
                newColor = newColor - w
            r1, g1, b1 = pic2.getPixelColor(newColor, y)
            pic.setPixelColor(x, y, r1, g1, b1)
    return(pic)

def negative(w, h, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, 255-r1, 255-g1, 255-b1)
    return(pic)
                
def grayscale(w, h, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            average = (r1 + g1 + b1)/3
            pic.setPixelColor(x, y, average, average, average)
    return(pic)

def cycle(w, h, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, b1, r1, g1)
    return pic

def zoom(w, h, pic) :
    pic2 = picCopy(w, h, pic)
    counterY = 0
    for y in range(0, h-1, 2) :
        counterX = 0
        for x in range (0, w-1, 2) :
            r1, g1, b1 = pic2.getPixelColor((w - 3*w/4) + counterX, (h - 3*h/4) + counterY)
            pic.setPixelColor(x, y, r1, g1, b1)
            pic.setPixelColor(x + 1, y, r1, g1, b1)
            pic.setPixelColor(x, y + 1, r1, g1, b1)
            pic.setPixelColor(x + 1, y + 1, r1, g1, b1)
            counterX = counterX + 1
        counterY = counterY + 1
    return pic

def posterize(w, h, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            r1 = round(r1/32.0)*32
            g1 = round(g1/32.0)*32
            b1 = round(b1/32.0)*32
            r1 = (int)(r1)
            g1 = (int)(g1)
            b1 = (int)(b1)
            pic.setPixelColor(x, y, r1, g1, b1)
    return pic

def brightness(w, h, d, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            r1 = r1 + d
            if r1 > 255:
                r1 = 255
            if r1 < 0:
                r1 = 0
            g1 = g1 + d
            if g1 > 255:
                g1 = 255
            if g1 < 0:
                g1 = 0
            b1 = b1 + d
            if b1 > 255:
                b1 = 255
            if b1 < 0:
                b1 = 0
            pic.setPixelColor(x, y, r1, g1, b1)
    return pic

def contrast(w, h, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            if r1 >= 128:
                r1 = 128 + (r1 - 128)*2
            if r1 < 128:
                r1 = 128 - (128 -r1)*2
            if g1 >= 128:
                g1 = 128 + (g1 - 128)*2
            if g1 < 128:
                g1 = 128 - (128 -g1)*2
            if b1 >= 128:
                b1 = 128 + (b1 - 128)*2
            if b1 < 128:
                b1 = 128 - (128 -b1)*2
            pic.setPixelColor(x, y, r1, g1, b1)
    return pic

def blur(w, h, pic) :
    pic2 = picCopy(w, h, pic)
    
    for x in range (w - 1) :
        for y in range(h - 1):
            
            redAverage = 0
            greenAverage = 0
            blueAverage = 0
                
            for y2 in range(y - 1, y + 2) :
                for x2 in range (x - 1, x +2) :
                    x3 = x2
                    y3 = y2
                    if x2 < 0 :
                        x3 = 0
                    if y2 < 0 :
                        y3 = 0
                    if x2 > w - 1:
                        x3 = w - 1
                    if y2 > h - 1:
                        y3 = h - 1
                    r2, g2, b2 = pic2.getPixelColor(x3, y3)
                    redAverage = redAverage + r2
                    greenAverage = greenAverage + g2
                    blueAverage = blueAverage + b2
            
            redAverage = redAverage/9
            greenAverage = greenAverage/9
            blueAverage = blueAverage/9
            
        
                
            pic.setPixelColor(x, y, redAverage, greenAverage, blueAverage)
         
                    
    
    return pic

def pretty(w, h, d, pic) :
    for y in range(h-1) :
        for x in range (w-1) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            r1 = r1 + random.randrange(-d, d)
            g1 = g1 + random.randrange(-d, d)
            b1 = b1 + random.randrange(-d, d)
            pic.setPixelColor(x, y, r1, g1, b1)
    return pic

def tiled(w, h, pic) :
    pic2 = picCopy(w,h, pic)
    for y in range(h-1) :
        for x in range (w-1) :
            if x > w//2 and y > h//2:
                r1, g1, b1 = pic2.getPixelColor((x-w//2)*2, (y-h//2)*2)
            if x > w//2 and y < h//2:
                r1, g1, b1 = pic2.getPixelColor((x-w//2)*2, y*2)
            if x < w//2 and y > h//2:
                r1, g1, b1 = pic2.getPixelColor(x*2, (y-h//2)*2)
            if x < w//2 and y < h//2:
                r1, g1, b1 = pic2.getPixelColor(x*2, y*2)
            pic.setPixelColor(x, y, r1, g1, b1)
    return pic
            
            
    
        
    
main()