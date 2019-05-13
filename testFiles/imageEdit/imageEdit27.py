








    
    
    
    
    
    
    
    
    
    
    
    
    
    
import math    
import picture2


def copy(pic):
    width=pic.getWidth()
    height=pic.getHeight()
    copy=picture2.Picture(width,height)
    for x in range (0, width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)
            copy.setPixelColor(x,y,r,g,b)
    return (copy)


def zoom(pic, copy):
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range (width/4, ((3/4)*(width))):
        for y in range (height/4, ((3/4)*(height))):
            r,g,b=pic.getPixelColor(x,y)
    for x in range (0,width-1,2):
        for y in range(0,height-1,2):
            r,g,b=pic.getPixelColor((width)//4+x//2,(height)//4+y//2)
            copy.setPixelColor(x,y,r,g,b)
            copy.setPixelColor(x+1,y,r,g,b)
            copy.setPixelColor(x,y+1,r,g,b)
            copy.setPixelColor(x+1,y+1,r,g,b)
    return (copy)


def fliphor(pic):
    
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width/2):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)   
            r2,g2,b2=pic.getPixelColor(width-x-1,y) 
            pic.setPixelColor(x,y,r2,g2,b2) 
            pic.setPixelColor(width-x-1,y,r,g,b) 
    return(pic)


def flip180(pic):
    width=pic.getWidth()
    height=pic.getHeight()
    fliphor(pic)
    for x in range(0,width-1):
        for y in range (0,height/2):
            r,g,b=pic.getPixelColor(x,y)   
            r2,g2,b2=pic.getPixelColor(x,height-y-1) 
            pic.setPixelColor(x,y,r2,g2,b2) 
            pic.setPixelColor(x,height-y-1,r,g,b) 
    return(pic)


def mirror(pic):
    
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width/2):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)   
            
            pic.setPixelColor(width-x-1,y,r,g,b)
    return(pic)


def scroll(pic,copy):
    
    
    d=input("How many pixels would you like me to shift the picture? ")
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)  
            copy.setPixelColor((x+d)%width,y,r,g,b)
            
    return(copy)

def negative(pic,copy):
    
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)
            r2,g2,b2=255-r,255-g,255-b
            
            copy.setPixelColor(x,y,r2,g2,b2)
            
    return(copy)

def grayscale (pic,copy):
    
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)  
            r2=((r+g+b)/3)
            g2=((r+g+b)/3)
            b2=((r+g+b)/3)
            
            copy.setPixelColor(x,y,r2,g2,b2) 
    return(copy)

def colorCycle (pic,copy):
    
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)
            r2,g2,b2= b,r,g
            
            
            copy.setPixelColor(x,y,r2,g2,b2)
            
    return(copy)

def posterize(pic, copy):
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range (0, width-1):
        for y in range(0, height-1):
            r,g,b=pic.getPixelColor(x,y)
            r2 = int(round(r/32))*32 
            g2 = int(round(g/32))*32
            b2 = int(round(b/32))*32
            copy.setPixelColor(x,y,r2,g2,b2)
    return(copy)

def brightness(pic, copy):
    change=input("How many color values would you like me to change the brightness of the picture? Enter a positive value to increase brightness, and a negative value to decrease brightness.")
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)
            r2 = r + change
            g2 = g + change
            b2 = b + change
            copy.setPixelColor(x,y,r2,g2,b2)
    return(copy)

def contrast(pic, copy):
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)
            r2 = 128 + (r-128)*2
            g2 = 128 + (g-128)*2
            b2 = 128 + (b-128)*2
            copy.setPixelColor(x,y,r2,g2,b2)
    return(copy)


def laCucaracha(pic,copy):
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)
            r2=r-(height-y)+100
            g2=g-(height-y)+100
            b2=b-(height-y)+100
            copy.setPixelColor(x,y,r2,g2,b2)
    return(copy)

def barneySwagga (pic,copy):
    
    width=pic.getWidth()
    height=pic.getHeight()
    for x in range(0,width-1):
        for y in range (0,height-1):
            r,g,b=pic.getPixelColor(x,y)  
            r2=((r+g)/2)
            g2=((g+b)/2)
            b2=((r+b)/2)
            
            copy.setPixelColor(x,y,r2,g2,b2) 
    return(copy)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def main():
    edits = ["Flip Horizontally", "Flip 180 Degrees", "Mirror", "Scroll", "Negative", "Grayscale", "Color Cycle", "Posterize", "Change Brightness", "Change Contrast", "Zoom", "Blur", "La Cucaracha", "Barney Swagga"]
    print("Welcome to my Image Manipulator! This powerful machine will take an imported image and take it for a spin, through funhouse mirrors, shapeshifters, mindbenders and beyond!")
    goodInput=True
    fileName=raw_input("Please enter the image file you'd like loaded: ")
    
        
    pic=picture2.Picture(fileName)
    realCopy=copy(pic)
    width=pic.getWidth()
    height=pic.getHeight()
   
        
    
    while goodInput:
        print("The list of available edits is", edits, ". If you would like to exit this program, type 'Exit'")
        effectName=raw_input("Please enter your desired effect from the list above: ")
        if effectName=="Flip Horizontally":
            pic = fliphor(pic)
            realCopy=copy(pic)
        elif effectName=="Flip 180 Degrees":
            pic = flip180(pic)
            realCopy=copy(pic)
        elif effectName=="Mirror":
            pic = mirror(pic)
            realCopy=copy(pic)
        elif effectName=="Scroll":
            pic = scroll(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Negative":
            pic = negative(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Grayscale":
            pic = grayscale(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Color Cycle":
            pic = colorCycle(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Posterize":
            pic = posterize(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Change Brightness":
            pic = brightness(pic, realCopy)
            realCopy=copy(pic)
        elif effectName=="Change Contrast":
            pic = contrast(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Zoom":
            pic = zoom(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="La Cucaracha":
            pic= laCucaracha(pic,realCopy)
            realCopy=copy(pic)
        elif effectName=="Barney Swagga":
            pic = barneySwagga(pic,realCopy)
            realCopy=copy(pic)
        
        
        
        if effectName=="Exit":
            goodInput = False
        else:
            pic.display()
            print ("")
main()


