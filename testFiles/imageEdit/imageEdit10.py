







import picture2
import math
import random


def main() :
    
    
    
    
    
    
    
    
    
    pic = picture2.Picture("crayons.bmp")
    
    w = pic.getWidth()
    h = pic.getHeight()
    
    
    
    exit = False
    
    while not exit :
        nextEdit = raw_input("What would you like to do? Options: grayscale, negative, flip, mirror, scroll, cycle colors, zoom, posterize, change brightness, increase contrast, blur, rotate 180, find brightness, stripes, weird, randomize... ")
        if nextEdit == "grayscale" :
            stay = grayscale(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "negative" :
            stay = negative(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "zoom" :
            stay = zoom(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "flip" :
            stay = flip(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "mirror" :
            stay = mirror(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "scroll" :
            stay = scroll(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "cycle colors" :
            stay = cycleColors(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "rotate 180" :
            stay = rotate(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return              
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "blur" :
            stay = blur(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "increase contrast" :
            stay = contrast(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "change brightness" :
            stay = brightness(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "posterize" :
            stay = posterize(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "find brightness" :
            stay = findbrightness(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "stripes" :
            stay = stripes(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "weird" :
            stay = weird(pic,w,h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        if nextEdit == "randomize" :
            stay = randomize(pic, w, h)
            if stay == "yes" :
                continue
            if stay == "no" :
                exit = True
                return
            nextEdit = nextEdit = raw_input("What effect would you like next? ")
        else :
            print "That's not an option. Try again"
  
    

def grayscale(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            avg = (r+g+b)/3
            pic.setPixelColor(x,y,avg,avg,avg)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def negative(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x,y,255-r,255-g,255-b)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
    
def rotate(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor((w-1)-x, (h-1)-y, r, g, b)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
    
def mirror(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w/2) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(w-1-x, y, r, g, b)           
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
    
def flip(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(w-1-x, y, r, g, b)              
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def cycleColors(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x, y, b, r, g)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
    
def scroll(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    d = raw_input("How far to the right would you like to scroll? ")
    d = eval(d)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor((x+d)%(w-1), y, r, g, b)                  
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def zoom(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(w//4, 3*w//4) :
        for y in range(h//4, 3*h//4) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(2*(x-w//4),2*(y-h//4),r,g,b)
            pic.setPixelColor(2*(x-w//4)+1,2*(y-h//4),r,g,b)
            pic.setPixelColor(2*(x-w//4),2*(y-h//4)+1,r,g,b)
            pic.setPixelColor(2*(x-w//4)+1,2*(y-h//4)+1,r,g,b)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
            
def posterize(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            pic.setPixelColor(x, y, ((r//32)*32), ((g//32)*32), ((b//32)*32))
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def brightness(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    goodInput = False
    while not goodInput:
        try:
            change = input("How much would you like to change the brightness? (Pos or Neg Int): ")
            for x in range(0, w) :
                for y in range(0, h) :
                    r,g,b = pic2.getPixelColor(x,y)
                    if r+change>255 :
                        r = 255
                    if r+change<0 :
                        r = 0
                    else :
                        r = r+change
                    if g+change>255 :
                        g = 255
                    if g+change<0 :
                        g = 0
                    else :
                        g = g+change
                    if b+change>255 :
                        b = 255
                    if b+change<0 :
                        b = 0
                    else :
                        b = b+change
                    pic.setPixelColor(x, y, r, g, b)
            goodInput = True
        except NameError:
            print "Uh oh. Try typing in a number!"
        
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def contrast(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            if r >= 128 :
                add = (r-128)*2
                if r+add > 255 :
                    pic.setPixelRed(x, y, 255)
                else :
                    pic.setPixelRed(x, y, r+add)
            if r < 128 :
                add = (128-r)*2
                if r-add < 0 :
                    pic.setPixelRed(x, y, 0)
                else :
                    pic.setPixelRed(x, y, r-add)
                    
            if g >= 128 :
                add = (g-128)*2
                if g+add > 255 :
                    pic.setPixelGreen(x, y, 255)
                else :
                    pic.setPixelGreen(x, y, g+add)
            if g < 128 :
                add = (128-g)*2
                if g-add < 0 :
                    pic.setPixelGreen(x, y, 0)
                else :
                    pic.setPixelGreen(x, y, g-add)
                    
            if b >= 128 :
                add = (b-128)*2
                if b+add > 255 :
                    pic.setPixelBlue(x, y, 255)
                else :
                    pic.setPixelBlue(x, y, b+add)
            if b < 128 :
                add = (128-b)*2
                if b-add < 0 :
                    pic.setPixelBlue(x, y, 0)
                else :
                    pic.setPixelBlue(x, y, b-add)
                
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def blur(pic, w, h) :           
    pic2 = picCopy(pic, w, h)
    for x in range(1, w-1) :
        for y in range(1, h-1) :            
            r,g,b = pic2.getPixelColor(x+1,y-1)
            r1,g1,b1 = pic2.getPixelColor(x,y)
            r2,g2,b2 = pic2.getPixelColor(x-1,y)
            r3,g3,b3 = pic2.getPixelColor(x+1,y)
            r4,g4,b4 = pic2.getPixelColor(x,y+1)
            r5,g5,b5 = pic2.getPixelColor(x,y-1)
            r6,g6,b6 = pic2.getPixelColor(x-1,y-1)
            r7,g7,b7 = pic2.getPixelColor(x+1,y+1)
            r8,g8,b8 = pic2.getPixelColor(x-1,y+1)
            avgR = ((r+r1+r2+r3+r4+r5+r6+r7+r8)//9)
            avgB = ((b+b1+b2+b3+b4+b5+b6+b7+b8)//9)
            avgG = ((g+g1+g2+g3+g4+g5+g6+g7+g8)//9)
            pic.setPixelColor(x, y, avgR, avgG, avgB)
            pic.setPixelColor(x+1, y, avgR, avgG, avgB)
            pic.setPixelColor(x, y+1, avgR, avgG, avgB)
            pic.setPixelColor(x+1, y+1, avgR, avgG, avgB)
            pic.setPixelColor(x-1, y-1, avgR, avgG, avgB)
            pic.setPixelColor(x+1, y-1, avgR, avgG, avgB)
            pic.setPixelColor(x, y-1, avgR, avgG, avgB)
            pic.setPixelColor(x-1, y, avgR, avgG, avgB)
            pic.setPixelColor(x-1, y+1, avgR, avgG, avgB)
            
            if x == 0 and y!=0 and y!=h:    
                r,g,b = pic2.getPixelColor(x+1,y-1)
                r1,g1,b1 = pic2.getPixelColor(x,y)
                r3,g3,b3 = pic2.getPixelColor(x+1,y)
                r4,g4,b4 = pic2.getPixelColor(x,y+1)
                r5,g5,b5 = pic2.getPixelColor(x,y-1)
                r7,g7,b7 = pic2.getPixelColor(x+1,y+1)
                avgR = ((r+r1+r3+r4+r5+r7)//6)
                avgB = ((b+b1+b3+b4+b5+b7)//6)
                avgG = ((g+g1+g3+g4+g5+g7)//6)
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y, avgR, avgG, avgB)
                pic.setPixelColor(x, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y-1, avgR, avgG, avgB)
                pic.setPixelColor(x, y-1, avgR, avgG, avgB)
          
            if x == w and y!=0 and y!=h:        
                r1,g1,b1 = pic2.getPixelColor(x,y)
                r2,g2,b2 = pic2.getPixelColor(x-1,y)
                r4,g4,b4 = pic2.getPixelColor(x,y+1)
                r5,g5,b5 = pic2.getPixelColor(x,y-1)
                r6,g6,b6 = pic2.getPixelColor(x-1,y-1)
                r8,g8,b8 = pic2.getPixelColor(x-1,y+1)
                avgR = ((r1+r2+r4+r5+r6+r8)//9)
                avgB = ((b1+b2+b4+b5+b6+b8)//9)
                avgG = ((g1+g2+g4+g5+g6+g8)//9)
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y+1, avgR, avgG, avgB)
                
            if y == 0 and x!=0 and x!=w :       
                r1,g1,b1 = pic2.getPixelColor(x,y)
                r2,g2,b2 = pic2.getPixelColor(x-1,y)
                r3,g3,b3 = pic2.getPixelColor(x+1,y)
                r4,g4,b4 = pic2.getPixelColor(x,y+1)
                r7,g7,b7 = pic2.getPixelColor(x+1,y+1)
                r8,g8,b8 = pic2.getPixelColor(x-1,y+1)
                avgR = ((r1+r2+r3+r4+r7+r8)//6)
                avgB = ((b1+b2+b3+b4+b7+b8)//6)
                avgG = ((g1+g2+g3+g4+g7+g8)//6)
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y, avgR, avgG, avgB)
                pic.setPixelColor(x, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y+1, avgR, avgG, avgB)
                
            if y == h and x!=0 and x!=w :       
                r,g,b = pic2.getPixelColor(x+1,y-1)
                r1,g1,b1 = pic2.getPixelColor(x,y)
                r2,g2,b2 = pic2.getPixelColor(x-1,y)
                r3,g3,b3 = pic2.getPixelColor(x+1,y)
                r5,g5,b5 = pic2.getPixelColor(x,y-1)
                r6,g6,b6 = pic2.getPixelColor(x-1,y-1)
                avgR = ((r+r1+r2+r3+r5+r6)//6)
                avgB = ((b+b1+b2+b3+b5+b6)//6)
                avgG = ((g+g1+g2+g3+g5+g6)//6)
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y-1, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y-1, avgR, avgG, avgB)
                pic.setPixelColor(x, y-1, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y, avgR, avgG, avgB)
                
            if y==0 and x==0 :              
                r,g,b = pic2.getPixelColor(x,y)
                r1,g1,b1 = pic2.getPixelColor(x+1,y+1)
                r2,g2,b2 = pic2.getPixelColor(x+1,y)
                r3,g3,b3 = pic2.getPixelColor(x,y+1)
                avgR = ((r+r1+r2+r3)//4)
                avgB = ((b+b1+b2+b3+b4)//4)
                avgG = ((g+g1+g2+g3+g4//4))
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x, y+1, avgR, avgG, avgB)
                
            if y==0 and x==w :          
                r,g,b = pic2.getPixelColor(x,y)
                r1,g1,b1 = pic2.getPixelColor(x-1,y+1)
                r2,g2,b2 = pic2.getPixelColor(x-1,y)
                r3,g3,b3 = pic2.getPixelColor(x,y+1)
                avgR = ((r+r1+r2+r3)//4)
                avgB = ((b+b1+b2+b3+b4)//4)
                avgG = ((g+g1+g2+g3+g4//4))
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y, avgR, avgG, avgB)
                
            if x==0 and y==h :      
                r,g,b = pic2.getPixelColor(x,y)
                r1,g1,b1 = pic2.getPixelColor(x,y-1)
                r2,g2,b2 = pic2.getPixelColor(x+1,y)
                r3,g3,b3 = pic2.getPixelColor(x+1,y-1)
                avgR = ((r+r1+r2+r3)//4)
                avgB = ((b+b1+b2+b3+b4)//4)
                avgG = ((g+g1+g2+g3+g4//4))
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y+1, avgR, avgG, avgB)
                pic.setPixelColor(x+1, y, avgR, avgG, avgB)
                
            if x==w and y==h :          
                r,g,b = pic2.getPixelColor(x,y)
                r1,g1,b1 = pic2.getPixelColor(x,y-1)
                r2,g2,b2 = pic2.getPixelColor(x-1,y-1)
                r3,g3,b3 = pic2.getPixelColor(x-1,y-1)
                avgR = ((r+r1+r2+r3)//4)
                avgB = ((b+b1+b2+b3+b4)//4)
                avgG = ((g+g1+g2+g3+g4//4))
                pic.setPixelColor(x, y, avgR, avgG, avgB)
                pic.setPixelColor(x, y-1, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y-1, avgR, avgG, avgB)
                pic.setPixelColor(x-1, y, avgR, avgG, avgB)
                    
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False

def weird(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            if r > 128 and ((r-128)*2+r)<=255 :
                pic.setPixelRed(x, y, (r-128)*2+r)
            if r <128 and ((128-r)*2+r)>=0 :
                pic.setPixelRed(x,y, (128-r)*2+r)
            if g > 128 and ((g-128)*2+g)<=255 :
                pic.setPixelGreen(x, y, (g-128)*2+g)
            if g <128 and ((128-g)*2+g)>=0 :
                pic.setPixelGreen(x,y, (128-g)*2+g)
            if b > 128 and ((b-128)*2+b)<=255 :
                pic.setPixelBlue(x, y, (b-128)*2+b)
            if b <128 and ((128-b)*2+b)>=0 :
                pic.setPixelBlue(x,y, (128-b)*2+b)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
                
def findbrightness(pic, w, h):
    pic2 = picCopy(pic,w,h)
    for i in range(2, w-2):
        for j in range(2,h-2):
            r,g,b = pic2.getPixelColor(i,j)
            for k in range(i-2,i+2):
                for l in range(j-2,j+2):
                    r1,g1,b1 = pic2.getPixelColor(k,l)
                if r1>r+22 or r1<r-23 or b1>b+23 or b1<b-23 or g1>g+23 or g1<g-23:
                    pic.setPixelColor(i,j,r+5,g+5,b+5)
                elif r-23<r1<r+23 or b-23<b1<b+23 or g-23<g1<g+23:
                    pic.setPixelColor(i,j,0,0,0)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
                    
def stripes(pic,w,h):
    pic2 = picCopy(pic,w,h)
    goodInput = False
    while not goodInput:
        try :
            orient = raw_input("Would you like horizontal or vertical stripes? ")
            size = eval(raw_input("How far apart would you like your stripes? "))
            if type(size) != int :
                goodInput = False
                return
            if orient =="horizontal" or orient =="vertical" :
                goodInput = True
            else :
                print "That's not an option!"
                goodInput=False
        except NameError :
            print "That's not an option!"
            goodInput = False
        except SyntaxError :
            print "That's not an option!"
            goodInput = False
        except ValueError :
            print "That's not an option!"
            goodInput = False
    if orient=="horizontal" :
        for x in range(0,w):
            for y in range(0,h,size):
                r,g,b = pic2.getPixelColor(x,y)
                pic.setPixelColor(x,y,0,0,0)
    elif orient=="vertical":
        for x in range(0,w,size):
            for y in range(0,h):
                r,g,b = pic2.getPixelColor(x,y)
                pic.setPixelColor(x,y,0,0,0)
        else:
            print "That's not an option!"
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
            
def randomize(pic, w, h) :
    pic2 = picCopy(pic, w, h)
    
    goodRand = False
    while not goodRand :
        try :
            rand = raw_input("How random would you like to make your image, on a scale of 0 to 255? ")
            rand = eval(rand)
            if rand < 0 or rand > 256 :
                print "Input a number between 0 and 255."
            else :
                goodRand = True
        except NameError :
            print "Input a number between 0 and 255."
        except SyntaxError :
            print "Input a number between 0 and 255."
            
    goodColor = False
    while not goodColor :
        try :
            color = raw_input("Which colors would you like to randomize? R, G, B, R and G, R and B, G and B, or all: ")
            if color == "R" or color == "G" or color == "B" or color == "R and G" or color == "R and B" or color == "G and B" or color == "all" :
                goodColor = True
            else :
                print "Return one of the options -- R, G, B, R and G, R and B, G and B, or all. "
        except NameError :
            print "Return one of the options -- R, G, B, R and G, R and B, G and B, or all. "
        except SyntaxError :
            print "Return one of the options -- R, G, B, R and G, R and B, G and B, or all. "
        except Exception:
            print "Return one of the options -- R, G, B, R and G, R and B, G and B, or all. "
            
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic2.getPixelColor(x,y)
            
            if color == "R" or color == "R and G" or color == "R and B" or color == "all" :
                if r + random.randint(-rand,rand) >= 255 :
                    r = 255
                elif r + random.randint(-rand,rand) <= 0 :
                    r = 0
                else :
                    r = r + random.randint(-rand,rand)
                    
            if color == "B" or color == "R and B" or color == "G and B" or color == "all" :        
                if b + random.randint(-rand,rand) >= 255 :
                    b = 255
                elif b + random.randint(-rand,rand) <= 0 :
                    b = 0
                else :
                    b = b + random.randint(-rand,rand)
                
            if color == "G" or color == "R and G" or color == "G and B" or color == "all" :     
                if g + random.randint(-rand,rand) >= 255 :
                    g = 255
                elif g + random.randint(-rand,rand) <= 0 :
                    g = 0
                else :
                    g = g + random.randint(-rand,rand)
                
            pic.setPixelColor(x, y, r, g, b)
    pic.display()
    goodStay = False
    while not goodStay :
        stay = raw_input("Would you like to keep editing your image? Reply yes or no: ")
        if stay == "yes" or stay == "no" :
            return stay
            goodStay = True
        else :
            print "Answer yes or no."
            goodStay = False
    
    

def picCopy(pic, w, h) :
    pic2 = picture2.Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r,g,b = pic.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    return pic2
    
    
    
main()    