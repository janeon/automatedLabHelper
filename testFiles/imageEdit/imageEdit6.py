





from picture2 import *


def flip(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(w - 1 - x, y, r)
            pic2.setPixelGreen(w - 1 - x, y, g)
            pic2.setPixelBlue(w - 1 - x, y, b)
    pic2.display(); raw_input()
    

def mirror(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, (w - 1)//2 + 1) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            s = x - (w - 1)//2
            
            pic2.setPixelRed((w - 1)//2 - s, y, r)
            pic2.setPixelGreen((w - 1)//2 - s, y, g)
            pic2.setPixelBlue((w - 1)//2 - s, y, b)
            
            pic2.setPixelRed((w - 1)//2 + s, y, r)
            pic2.setPixelGreen((w - 1)//2 + s, y, g)
            pic2.setPixelBlue((w - 1)//2 + s, y, b)      
    pic2.display(); raw_input() 


def scroll(pic, w, h) :
    prompt = False 
    while prompt == False : 
        try :
            q = eval(raw_input("Please enter a positive integer value from 1 to", w - 1, ": ")) 
            prompt = True
        except TypeError :
            print "Error. Did you follow the instructions?"
        if q < 1 or q > w - 1 :
            prompt = False
    d = w - 1- q
    
    pic2 = Picture(w,h)
    for x in range(0, q) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed((x + d), y, r)
            pic2.setPixelGreen((x + d), y, g)
            pic2.setPixelBlue((x + d), y, b)
    
    for x in range(q, w - 1) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(x - q, y, r)
            pic2.setPixelGreen(x - q, y, g)
            pic2.setPixelBlue(x - q, y, b)
            
    pic2.display(); raw_input()


def neg(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(x,y,254-r)
            pic2.setPixelGreen(x,y,254-g)
            pic2.setPixelBlue(x,y,254-b)
    pic2.display(); raw_input()


def gray(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            s = r + g + b
            
            pic2.setPixelRed(x,y, s//3)
            pic2.setPixelGreen(x,y, s//3)
            pic2.setPixelBlue(x,y, s//3)
    pic2.display(); raw_input()
    

def cycle(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(x,y, b)
            pic2.setPixelGreen(x,y, r)
            pic2.setPixelBlue(x,y, g)
    pic2.display(); raw_input()
    

def zoom(pic, w, h) :
    pic2 = Picture(w, h)
    p = w//4 - 1; q = h//4 - 1
    for y in range(h//4 - 1, h - h//4 - 2) :
        for x in range(w//4 - 1, w - w//4 - 2) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(2*(x-p),2*(y-q), r)
            pic2.setPixelGreen(2*(x-p),2*(y-q), g)
            pic2.setPixelBlue(2*(x-p),2*(y-q), b)
            
            pic2.setPixelRed(2*(x-p) + 1, 2*(y-q), r)
            pic2.setPixelGreen(2*(x-p) + 1, 2*(y-q), g)
            pic2.setPixelBlue(2*(x-p) + 1, 2*(y-q), b)
            
            pic2.setPixelRed(2*(x-p),2*(y-q) + 1, r)
            pic2.setPixelGreen(2*(x-p),2*(y-q) + 1, g)
            pic2.setPixelBlue(2*(x-p),2*(y-q) + 1, b)
            
            pic2.setPixelRed(2*(x-p) + 1, 2*(y-q) + 1, r)
            pic2.setPixelGreen(2*(x-p) + 1, 2*(y-q) + 1, g)
            pic2.setPixelBlue(2*(x-p) + 1, 2*(y-q) + 1, b)
    pic2.display(); raw_input()


def posterize(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(x,y, (r//32) * 32)
            pic2.setPixelGreen(x,y, (g//32) * 32)
            pic2.setPixelBlue(x,y, (b//32) * 32)
    pic2.display(); raw_input()
    

def brightness(pic, w, h) :
    print "By how much would you like the brightmess changed?"
    prompt = False 
    while prompt == False : 
        try :
            n = eval(raw_input("Please enter a positive or negative integer value: "))
            prompt = True
        except TypeError :
            print "Error. Did you follow the instructions?"
            
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            r2 = r + n
            g2 = g + n
            b2 = b + n
            
            if r2 > 254 :
                r2 = 254
            elif r2 < 0 :
                r2 = 0
                
            if g2 > 254 :
                g2 = 254
            elif g2 < 0 :
                g2 = 0
            
            if b2 > 254 :
                b2 = 254
            elif b2 < 0 :
                b2 = 0
            
            pic2.setPixelRed(x,y, r2)
            pic2.setPixelGreen(x,y, g2)
            pic2.setPixelBlue(x,y, b2)
    pic2.display(); raw_input()
    

def contrast(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            r2 = 2*(r - 128) + r 
            g2 = 2*(g - 128) + g
            b2 = 2*(b - 128) + g
            
            if r2 > 254 :
                r2 = 254
            elif r2 < 0 :
                r2 = 0
                
            if g2 > 254 :
                g2 = 254
            elif g2 < 0 :
                g2 = 0
            
            if b2 > 254 :
                b2 = 254
            elif b2 < 0 :
                b2 = 0
            
            pic2.setPixelRed(x,y, r2)
            pic2.setPixelGreen(x,y, g2)
            pic2.setPixelBlue(x,y, b2)
    pic2.display(); raw_input()


def blur(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            xPlus = x + 1
            xMinus = x - 1
            yPlus = y + 1
            yMinus = y - 1
            
            if xMinus < 0 :
                xMinus = 0
                
            if xPlus > w - 1 :
                xPlus = w - 1
                
            if yMinus < 0 :
                yMinus = 0
            
            if yPlus > h - 1 :
                yPlus = h - 1
            
            r1 = pic.getPixelRed(xMinus, yMinus)
            g1 = pic.getPixelGreen(xMinus, yMinus)
            b1 = pic.getPixelBlue(xMinus, yMinus)
            
            r2 = pic.getPixelRed(x, yMinus)
            g2 = pic.getPixelGreen(x, yMinus)
            b2 = pic.getPixelBlue(x, yMinus)
            
            r3 = pic.getPixelRed(xPlus, yMinus)
            g3 = pic.getPixelGreen(xPlus, yMinus)
            b3 = pic.getPixelBlue(xPlus, yMinus)
            
            r4 = pic.getPixelRed(xMinus, y)
            g4 = pic.getPixelGreen(xMinus, y)
            b4 = pic.getPixelBlue(xMinus, y)
            
            r5 = pic.getPixelRed(x, y)
            g5 = pic.getPixelGreen(x, y)
            b5 = pic.getPixelBlue(x, y)
            
            r6 = pic.getPixelRed(xPlus, y)
            g6 = pic.getPixelGreen(xPlus, y)
            b6 = pic.getPixelBlue(xPlus, y)
            
            r7 = pic.getPixelRed(xMinus, yPlus)
            g7 = pic.getPixelGreen(xMinus, yPlus)
            b7 = pic.getPixelBlue(xMinus, yPlus)
            
            r8 = pic.getPixelRed(x, yPlus)
            g8 = pic.getPixelGreen(x, yPlus)
            b8 = pic.getPixelBlue(x, yPlus)
            
            r9 = pic.getPixelRed(xPlus, yPlus)
            g9 = pic.getPixelGreen(xPlus, yPlus)
            b9 = pic.getPixelBlue(xPlus, yPlus)
            
            rA = (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9)/9
            gA = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9)/9
            bA = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9)/9
            
            pic2.setPixelRed(x,y, rA)
            pic2.setPixelGreen(x,y, gA)
            pic2.setPixelBlue(x,y, bA)
    pic2.display(); raw_input()
            

def rotate(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(w - 1 - x, h - 1 - y, r)
            pic2.setPixelGreen(w - 1 - x, h - 1 - y, g)
            pic2.setPixelBlue(w - 1 - x, h - 1 - y, b)
    pic2.display(); raw_input()           
            


def psych(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            pic2.setPixelRed(x,y, (r%15) * 25)
            pic2.setPixelGreen(x,y, (g%15) * 25)
            pic2.setPixelBlue(x,y, (b%15) * 25)
    pic2.display(); raw_input()


def dawn(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            s = r + g + b
            
            pic2.setPixelRed(x,y, (r//100) * s//3)
            pic2.setPixelGreen(x,y, (g//100) * s//3 - 40)
            pic2.setPixelBlue(x,y, (b//100) * s//3 - 40)
    pic2.display(); raw_input()


def mystic(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            
            r2 = 2*(r - 128) + r 
            g2 = 2*(g - 128) + g
            b2 = 2*(g - 128) + g
            
            if r2 > 254 :
                r2 = 254
            elif r2 < 0 :
                r2 = 0
                
            if g2 > 254 :
                g2 = 254
            elif g2 < 0 :
                g2 = 0
            
            if b2 > 254 :
                b2 = 254
            elif b2 < 0 :
                b2 = 0
            
            pic2.setPixelRed(x,y, r2)
            pic2.setPixelGreen(x,y, g2)
            pic2.setPixelBlue(x,y, b2)
    pic2.display(); raw_input()


def grayRed(pic, w, h) :
    pic2 = Picture(w,h)
    for x in range(0, w) :
        for y in range(0, h) :
            r = pic.getPixelRed(x, y)
            g = pic.getPixelGreen(x, y)
            b = pic.getPixelBlue(x, y)
            s = int(1.5 * r) + g + b
            
            pic2.setPixelRed(x,y, s//3)
            pic2.setPixelGreen(x,y, s//3)
            pic2.setPixelBlue(x,y, s//3)
    pic2.display(); raw_input()

def main() :
    
    print "Welcome to Acme Image Editor."
    prompt = False
    
    
    while prompt == False :
        try : 
            fileName = raw_input("Please enter the image file that you'd like loaded: ")
            pic = Picture(fileName)
            prompt = True
            w = pic.getWidth()
            h = pic.getHeight()
        
        except IOError : 
            print "Error. Is that a picture in this directory?"  
    
    pic.display()
    raw_input("Press enter to continue ")
    
    
    prompt = False
    while prompt == False :
        try :
            print "Edit your photo with the following effects: "
            print "(1)  Flip Horizontally "
            print "(2)  Mirror Horizontally "
            print "(3)  Scroll Horizontally "
            print "(4)  Make Negative "
            print "(5)  Make Grayscale "
            print "(6)  Cycle Color Channels "
            print "(7)  Zoom "
            print "(8)  Posterize "
            print "(9)  Change Brightness "
            print "(10) Increase Contrast "
            print "(11) Blur "
            print "(12) Rotate 180 Degrees "
            print "(13) Psychedelic "
            print "(14) Break of Dawn "
            print "(15) Mystical"
            print "(16) Red-filtered Grayscale "
            print
            print "(0)  To Exit Program " 
            
            num_effect = eval(raw_input("Please enter the number of the effect you'd like to use: "))
            if num_effect == 1 :
                flip(pic, w, h)
                
            if num_effect == 2 :
                mirror(pic, w, h)
                
            elif num_effect == 3 :
                scroll(pic, w, h)
                
            elif num_effect == 4 :
                neg(pic, w, h)
              
            elif num_effect == 5 :
                gray(pic, w, h)
            
            elif num_effect == 6 :
                cycle(pic, w, h)
            
            elif num_effect == 7 :
                zoom(pic, w, h)
            
            elif num_effect == 8 :
                posterize(pic, w, h)
            
            elif num_effect == 9 :
                brightness(pic, w, h)
                
            elif num_effect == 10 :
                contrast(pic, w, h)
            
            elif num_effect == 11 :
                blur(pic, w, h)
                
            elif num_effect == 12 :
                rotate(pic, w, h)
                
            elif num_effect == 13 :
                psych(pic, w, h)
            
            elif num_effect == 14 :
                dawn(pic, w, h)   
            
            elif num_effect == 15 :
                mystic(pic, w, h)
            
            elif num_effect == 16 :
                grayRed(pic, w, h)
            
            
            elif num_effect == 0 :
                prompt = True
            else :
                pass
            
        except SyntaxError:
            ("Error. Make sure you are entering only the number of the effect.")
        
        except NameError:
            ("Error. Make sure you are entering only the number of the effect.")

main()