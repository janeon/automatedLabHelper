






import picture2
import math


if 1==1:
    print
    print "Welcome to my image manipulator!"
    print
    goodInput = False
    while not goodInput:
        try :
            print
            picChoice = raw_input("Please enter the image file you'd like loaded: ")
            pic = picture2.Picture(picChoice)
            
            print

            goodInput = True
            
            
 
  
    
        except Exception as e:
            print
            print
            print "Something went wrong.. Try to type the image again, or try another image?"
            print
            print(type(e))
            print(str(e))

w = pic.getWidth()
h = pic.getHeight()
pic2 = picture2.Picture(w,h)


def explanation():
    
    print 
    print "Enter:"
    print "     0 to display the original image"
    print "     1 to Flip Horizontally"
    print "     2 to Mirror Horizontally"
    print "     3 to Scroll Horizontally"
    print "     4 to Make Negative"
    print "     5 to Make Grayscale"
    print "     6 to Cycle Color Channels"
    print "     7 to Zoom"
    print "     8 to Posterize"
    print "     9 to Change Brightness"
    print "     10 to Increase Contrast"
    print "     11 to Blur"
    print "     12 to Rotate 180 Degrees"
    print "     13 to Chickenpox"
    print "     14 to Your Own Effect (II) "
    print "     15 to Exit program "
    print 

def picCopy(pic2):
    
    for x in range(0, w-1):
        for y in range (0, h-1) :
            getR = pic.getPixelRed(x,y)
            getB = pic.getPixelBlue(x,y)
            getG = pic.getPixelGreen(x,y)
            
            pic2.setPixelBlue(x,y, getB)
            pic2.setPixelRed(x,y, getR)
            pic2.setPixelGreen(x,y, getG)
            
    return pic2
    







def negative(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    
    for x in range (0, w-1) :
        for y in range (0, h-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)

            pic.setPixelBlue(x,y, 255-getB)
            pic.setPixelRed(x,y, 255-getR)
            pic.setPixelGreen(x,y, 255-getG)
            
    return pic

    
    
  
  
  
  

def flipH(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for x in range (0, w-1) :
        for y in range (0, h-1) : 
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            pic.setPixelBlue((w-1)-x,y, getB)
            pic.setPixelRed((w-1)-x,y, getR)
            pic.setPixelGreen((w-1)-x,y, getG)
    return pic
    
def mirrorH(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w/2-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            pic.setPixelBlue((w-1)-x,y, getB)
            pic.setPixelRed((w-1)-x,y, getR)
            pic.setPixelGreen((w-1)-x,y, getG)
            
    return pic

def scroll(pic):
    goodInput = False
    while not goodInput:
        try:
            scrollpix = input("How many pixels do you want the image shifted to the right?  ")
            goodInput = True
        except Exception as e:
            print
            print
            print "Something went wrong.. Make sure you only enter an integer! Try again."
            print
            print(type(e))
            print(str(e))
            print

    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            if x+scrollpix > w-1:
                x = (x+scrollpix)-(w-1)
            else:
                x=x+scrollpix
                
            pic.setPixelBlue(x,y, getB)
            pic.setPixelRed(x,y, getR)
            pic.setPixelGreen(x,y, getG)
    return pic
            
def grayscale(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
        
            pic.setPixelBlue(x,y, (getR+getB+getG)/3)
            pic.setPixelRed(x,y, (getR+getB+getG)/3)
            pic.setPixelGreen(x,y, (getR+getB+getG)/3)
    return pic


def channel(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
        
            pic.setPixelBlue(x,y, getG)
            pic.setPixelRed(x,y, getB)
            pic.setPixelGreen(x,y, getR)
    return pic


def zoom(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed((x+w/2)/2,(y+h/2)/2)
            getB = pic2.getPixelBlue((x+w/2)/2,(y+h/2)/2)
            getG = pic2.getPixelGreen((x+w/2)/2,(y+h/2)/2)
        
            pic.setPixelBlue(x,y, getB)
            pic.setPixelRed(x,y, getR)
            pic.setPixelGreen(x,y, getG)
    return pic

def posterize(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            
            getR=(getR//32)*32
            getB=(getB//32)*32
            getG=(getG//32)*32
            
            pic.setPixelBlue(x,y, getB)
            pic.setPixelRed(x,y, getR)
            pic.setPixelGreen(x,y, getG)
    return pic

def brightness(pic):
    print "How much brighter do you want the picture?  "
    goodInput = False
    while not goodInput:
        try:
            bri = input("(give me a positive or negative integer)    ")
            goodInput = True
        except Exception as e:
            print
            print
            print "Something went wrong.. Make sure you only enter an integer! Try again."
            print
            print(type(e))
            print(str(e))
            print
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            getR=(getR+bri)
            if getR>255:
                getR=255
            if getR<0:
                getR=0
            getB=(getB+bri)
            if getB>255:
                getB=255
            if getB<0:
                getB=0
            getG=(getG+bri)
            if getG>255:
                getG=255
            if getG<0:
                getG=0
            
            pic.setPixelBlue(x,y, getB)
            pic.setPixelRed(x,y, getR)
            pic.setPixelGreen(x,y, getG)
    return pic

def contrast(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1) :
        for x in range (0, w-1) :
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            getR=getR-(getR-128)+(2*(getR-128))
            getB= getB-(getB-128)+(2*(getB-128))
            getG=getG-(getG-128)+(2*(getG-128))
            
            pic.setPixelBlue(x,y, getB)
            pic.setPixelRed(x,y, getR)
            pic.setPixelGreen(x,y, getG)
    return pic

def blur(pic):

    
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h) :
        for x in range (0, w) :
            nine=0
            rRR=0
            bBB=0
            gGG=0
            if y-1<0:
                if x-1<0:
                    red=pic2.getPixelRed(0,0)+pic2.getPixelRed(1,0)+pic2.getPixelRed(0,1)+pic2.getPixelRed(1,1)
                    red=red/4
                    pic.setPixelRed(x, y, red)
                    green = pic2.getPixelGreen(0,0)+pic2.getPixelGreen(1,0)+pic2.getPixelGreen(1,0)+pic2.getPixelGreen(1,1)
                    green=green/4
                    pic.setPixelGreen(x,y,green)
                    blue=pic2.getPixelBlue(0,0)+pic2.getPixelBlue(1,0)+pic2.getPixelBlue(0,1)+pic2.getPixelBlue(1,1)
                    blue=blue/4
                    pic.setPixelBlue(x, y, blue)
                elif x+1>w-1:
                    red=pic2.getPixelRed(w-1,0)+pic2.getPixelRed(w-2,0)+pic2.getPixelRed(w-2,1)+pic2.getPixelRed(w-1,1)
                    red=red/4
                    pic.setPixelRed(x, y, red)
                    green = pic2.getPixelGreen(w-1,0)+pic2.getPixelGreen(w-2,0)+pic2.getPixelGreen(w-2,1)+pic2.getPixelGreen(w-1,1)
                    green=green/4
                    pic.setPixelGreen(x,y,green)
                    blue=pic2.getPixelBlue(w-1,0)+pic2.getPixelBlue(w-2,0)+pic2.getPixelBlue(w-2,1)+pic2.getPixelBlue(w-1,1)
                    blue=blue/4
                    pic.setPixelBlue(x, y, blue)
                else:
                    for i in range(y, y+2):
                        for j in range (x-1, x+2):
                            rRR= rRR+pic2.getPixelRed(j,i)
                            gGG = gGG+pic2.getPixelGreen(j,i)
                            bBB = bBB+pic2.getPixelBlue(j,i)
                        red=rRR/6
                        green=gGG/6
                        blue=bBB/6
                        pic.setPixelRed(x, y, red)
                        pic.setPixelGreen(x,y,green)
                        pic.setPixelBlue(x, y, blue)
                        
            elif y+1>h-1:
                if x-1<0:
                    red=pic2.getPixelRed(0, h-1)+pic2.getPixelRed(1, h-1)+pic2.getPixelRed(0, h-2)+pic2.getPixelRed(1, h-2)
                    red=red/4
                    pic.setPixelRed(x, y, red)
                    green = pic2.getPixelGreen(0, h-1)+pic2.getPixelGreen(1, h-1)+pic2.getPixelGreen(0, h-2)+pic2.getPixelGreen(1, h-2)
                    green=green/4
                    pic.setPixelGreen(x,y,green)
                    blue=pic2.getPixelBlue(0, h-1)+pic2.getPixelBlue(1, h-1)+pic2.getPixelBlue(0, h-2)+pic2.getPixelBlue(1, h-2)
                    blue=blue/4
                    pic.setPixelBlue(x, y, blue)
                elif x+1>w-1:
                    red=pic2.getPixelRed(w-1,0)+pic2.getPixelRed(w-2,0)+pic2.getPixelRed(w-2,1)+pic2.getPixelRed(w-1,1)
                    red=red/4
                    pic.setPixelRed(x, y, red)
                    green = pic2.getPixelGreen(w-1,0)+pic2.getPixelGreen(w-2,0)+pic2.getPixelGreen(w-2,1)+pic2.getPixelGreen(w-1,1)
                    green=green/4
                    pic.setPixelGreen(x,y,green)
                    blue=pic2.getPixelBlue(w-1,0)+pic2.getPixelBlue(w-2,0)+pic2.getPixelBlue(w-2,1)+pic2.getPixelBlue(w-1,1)
                    blue=blue/4
                    pic.setPixelBlue(x, y, blue)
                else:
                    for i in range (y-1, y+1):
                        for j in range(x-1, x+2):
                            rRR= rRR+pic2.getPixelRed(j,i)
                            gGG = gGG+pic2.getPixelGreen(j,i)
                            bBB = bBB+pic2.getPixelBlue(j,i)
                        red=rRR/6
                        green=gGG/6
                        blue=bBB/6
                        pic.setPixelRed(x, y, red)
                        pic.setPixelGreen(x,y,green)
                        pic.setPixelBlue(x, y, blue)
                        
       
                        
            elif x-1<0:
                for i in range (y-1, y+2):
                    for j in range (x, x+2):
                        rRR= rRR+pic2.getPixelRed(j,i)
                        gGG = gGG+pic2.getPixelGreen(j,i)
                        bBB = bBB+pic2.getPixelBlue(j,i)                       
                red=rRR/6
                green=gGG/6
                blue=bBB/6                       
                pic.setPixelRed(x, y, red)
                pic.setPixelGreen(x,y,green)
                pic.setPixelBlue(x, y, blue)       
            elif x+1>w-1:
                for m in range (y-1, y+2):
                    for n in range (x-1, i+1):
                        rRR= rRR+pic2.getPixelRed(j,i)
                        gGG = gGG+pic2.getPixelGreen(j,i)
                        bBB = bBB+pic2.getPixelBlue(j,i)  
                red=rRR/6
                green=gGG/6
                blue=bBB/6   
                pic.setPixelRed(x, y, red)
                pic.setPixelGreen(x,y,green)
                pic.setPixelBlue(x, y, blue)      
            else:
                for i in range (y-1, y+2):
                    for j in range (x-1, x+2):
                        rRR= rRR+pic2.getPixelRed(j,i)
                        gGG = gGG+pic2.getPixelGreen(j,i)
                        bBB = bBB+pic2.getPixelBlue(j,i)  
                red=rRR/9
                green=gGG/9
                blue=bBB/9
                pic.setPixelRed(x, y, red)
                pic.setPixelGreen(x,y,green)
                pic.setPixelBlue(x, y, blue) 
    return pic

def oneeighty(pic):
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for x in range (0, w-1) :
        for y in range (0, h-1) : 
            getR = pic2.getPixelRed(x,y)
            getB = pic2.getPixelBlue(x,y)
            getG = pic2.getPixelGreen(x,y)
            
            pic.setPixelBlue((w-1)-x-1,(h-1)-y-1, getB)
            pic.setPixelRed((w-1)-x-1, (h-1)-y-1, getR)
            pic.setPixelGreen((w-1)-x-1, (h-1)-y-1, getG)
    return pic

def chickenpox(pic):
    rRR=0
    bBB=0
    gGG=0
    nine=0
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-1, h/40) :
      
        for x in range (0, w-1, 3) :
            for k in range (0,3):
                for j in range (0,3):

                    getR = pic2.getPixelRed(x+k,y+j)
                    getB = pic2.getPixelBlue(x+k,y+j)
                    getG = pic2.getPixelGreen(x+k,y+j)
            
                    rRR=rRR+getR
                    bBB=bBB+getB
                    gGG=gGG+getG
            
                    nine=nine+2
            
                    getR=rRR//nine*nine
                    getB=getB//nine*nine
                    getG=getG//nine*nine
                    
            
                    getR=(getR//100)*100
                    getB=(getB//100)*100
                    getG=(getG//100)*100
            pic.setPixelBlue(x,y, getB)
            pic.setPixelRed(x,y, getR)
            pic.setPixelGreen(x,y, getG)
    return pic

def gOOgley(pic):

    
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    for y in range (0, h-7, 6) :
        for x in range (0, w-7, 6) :
            nine=0
            rRR=0
            bBB=0
            gGG=0
            for k in range (0,3):
                for j in range (0,3):

                    getR = pic2.getPixelRed(x+k,y+j)
                    getB = pic2.getPixelBlue(x+k,y+j)
                    getG = pic2.getPixelGreen(x+k,y+j)
            
                    rRR=rRR+getR
                    bBB=bBB+getB
                    gGG=gGG+getG
            
                    nine=nine+1
                    
                    getR=rRR/nine
                    getB=bBB/nine
                    getG=gGG/nine
                    
            for k in range (0,6):
                for j in range (0,6):

                    
                    pic.setPixelBlue(x+k,y+j, getB)
                    pic.setPixelRed(x+k,y+j, getR)
                    pic.setPixelGreen(x+k,y+j, getG)

def main():

  
    pic2 = picture2.Picture(w,h)
    picCopy(pic2)
    
    explanation()
    
    goodInput = False
    while not goodInput:
        try:
            mod = input("What manipulation do you want me to perform?    ")
            print
            goodInput = True
        except Exception as e:
            print
            print
            print "Something went wrong.. Make sure you only enter a number that corresponds to an action! Try again."
            print
            print(type(e))
            print(str(e))
            print

    

    if mod==0:
        print
    if mod ==1:
        flipH(pic)
    if mod==2:
        mirrorH(pic)
    if mod==3:
        scroll(pic)
    if mod==4:
        negative(pic)
    if mod==5:
        grayscale(pic)
    if mod==6:
        channel(pic)
    if mod==7:
        zoom(pic)
    if mod==8:
        posterize(pic)
    if mod==9:
        brightness(pic)
    if mod==10:
        contrast(pic)
    if mod==11:
        blur(pic)    
    if mod==12:    
        oneeighty(pic)
    if mod==13:
        chickenpox(pic)
    if mod==14:
        pixelate(pic)
    
    if mod<15:
        try:
            pic.display()
            print
            print "Press return when you're done viewing!"
            input()
        except SyntaxError:
            print("Thanks for using my image manipulator!")
    if mod >14:
        print
        print "Goodbye! Thanks for coming!"
        print

main()



