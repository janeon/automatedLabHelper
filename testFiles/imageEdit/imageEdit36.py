





import picture2
import math

def main():
    
    print "WELCOME TO A WIZARD. I KNOW MANY SPELLS FOR BITMAPS"
    print "MY MIGHT COLLECTION OF BITMAPS CONTAINS: crayons.bmp, aurora.bmp, newtbirds.bmp"
    
    correct = False
    
    while correct == False:
        try :
            fileName = raw_input("WHAT IMAGE WOULD YOU LIKE DARK MAGICS DONE UPON? ")
            pic = picture2.Picture(fileName)
            correct = True
        except:
            print "IT IS NOT WISE TO TRY TO TRICK A WIZARD!"
            
    print "1. Talitrum Horizontaliter! (Flip Horizontally)"
    print "2. Referri Horizontaliter! (Mirror Horizontally)"
    print "3. Praetereo Horizontaliter! (Scroll Horizontally)"
    print "4. Mutare Negativa! (Make Negative)"
    print "5. Mutare Cincereo! (Make Grayscale)"
    print "6. Cycli Colorum! (Cycle color channels)"
    print "7. Salomith Et In! (Zoom)"
    print "8. Simpliciorem! (Posterize)"
    print "9. Mutari Splendor! (Change Brightness)"
    print "10. Crescere Conparationis! (Increase Contrast)"
    print "11. Labes! (Blur)"
    print "12. Praepostero! (Rotate 180 Degrees)"
    print "13. Gemerare Circulus! (Generate Vignette)"
    print "14. Hauriendam Summatim! (Draw outlines)"
    
    pick = int(raw_input("WHAT RITUAL SHOULD I PERFORM?"))
        
        
    if pick == 1:
        flipHorizontal(pic)
    elif pick == 2:
        mirrorHorizontal(pic)
    elif pick == 3:
        amount = int(raw_input("HOW MUCH?"))
        scrolling(pic,amount)
    elif pick == 4:
        negative(pic)
    elif pick == 5:
        grayscale(pic)
    elif pick == 6:
        cycle(pic)
    elif pick == 7:
        zoom(pic)
    elif pick == 8:
        posterize(pic)
    elif pick == 9:
        amount = int(raw_input("HOW MUCH?"))
        brightness(pic,amount)
    elif pick == 10:
        contrast(pic)
    elif pick == 11:
        blur(pic)
    elif pick == 12:
        rotate180(pic)
    elif pick == 13:
        vignette(pic)
    elif pick == 14:
        outlines(pic)
    else:
        print "I HAVE LITTLE PATIENCE FOR YOUR TOMFOOLERY"
        
   
        
        
    print "W I Z A R D\a"
    pic.display()
    raw_input()
    
    

def outlines(pic):
    posterize(pic)
    
    w = pic.getWidth()
    h = pic.getHeight()
    
    pic2 = picture2.Picture(w,h)
    pic2 = copyImage(pic,pic2)
    
    oldred,oldgreen,oldblue = pic.getPixelRed(0,0),pic.getPixelGreen(0,0),pic.getPixelBlue(0,0)
    
    for x in range(1,w-1):
        for y in range(1,h-1):
            newred = pic2.getPixelRed(x,y)
            newgreen = pic2.getPixelGreen(x,y)
            newblue = pic2.getPixelBlue(x,y)
            if newred != oldred or newgreen != oldgreen or newblue != oldblue:
                pic.setPixelColor(x,y,0,0,0)
                oldred,oldgreen,oldblue = newred,newgreen,newblue
            
    for y in range(1,h-1):
        for x in range(1,w-1):
            newred = pic2.getPixelRed(x,y)
            newgreen = pic2.getPixelGreen(x,y)
            newblue = pic2.getPixelBlue(x,y)
            
            if newred != oldred or newgreen != oldgreen or newblue != oldblue:
                pic.setPixelColor(x,y,0,0,0)
                oldred,oldgreen,oldblue = newred,newgreen,newblue
            
def vignette(pic):
    
    brightness(pic,20)
    
    w = pic.getWidth()
    h = pic.getHeight()
    hyp = math.sqrt((w*w)+(h*h))
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            red = pic.getPixelRed(x,y)
            green = pic.getPixelGreen(x,y)
            blue = pic.getPixelBlue(x,y)
            
            dist = math.sqrt(((x-(w/2))*(x-(w/2)))+((y-(h/2))*(y-(h/2))))
            
            
            z = int((dist*255)/hyp)*2
            
            pic.setPixelColor(x,y,red-z,green-z,blue-z)
            
def blur(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    pic2 = picture2.Picture(w,h)
    pic2 = copyImage(pic,pic2)
    
    cells = 0
    averageRed = 0
    averageGreen = 0
    averageBlue = 0
    
  
    for x in range(1,w-1):
        for y in range(1,h-1):
            averageRed,averageBlue,averageGreen,cells = 0,0,0,0
            
            try:
                averageRed += pic2.getPixelRed(x-1,y-1)
                averageGreen += pic2.getPixelGreen(x-1,y-1)
                averageBlue += pic2.getPixelBlue(x-1,y-1)
                cells += 1
            except:
                cells = cells
            try:
                averageRed += pic2.getPixelRed(x,y-1)
                averageGreen += pic2.getPixelGreen(x,y-1)
                averageBlue += pic2.getPixelBlue(x,y-1)
                cells += 1
            except:
                cells = cells
            try:
                averageRed +=pic2.getPixelRed(x+1,y-1)
                averageGreen +=pic2.getPixelGreen(x+1,y-1)
                averageBlue +=pic2.getPixelBlue(x+1,y-1)
                cells += 1
            except:
                cells = cells
            try:
                averageRed += pic2.getPixelRed(x-1,y)
                averageGreen += pic2.getPixelGreen(x-1,y)
                averageBlue += pic2.getPixelBlue(x-1,y)
                cells += 1
            except:
                cells = cells
            try:
                averageRed += pic2.getPixelRed(x+1,y)
                averageGreen += pic2.getPixelGreen(x+1,y)
                averageBlue += pic2.getPixelBlue(x+1,y)
                cells += 1
            except:
                cells = cells
            try:
                averageRed += pic2.getPixelRed(x-1,y+1)
                averageGreen += pic2.getPixelGreen(x-1,y+1)
                averageBlue += pic2.getPixelBlue(x-1,y+1)
                cells += 1
            except:
                cells = cells
            try:
                averageRed += pic2.getPixelRed(x,y+1)
                averageGreen += pic2.getPixelGreen(x,y+1)
                averageBlue += pic2.getPixelBlue(x,y+1)
                cells += 1
            except:
                cells = cells
            try:
                averageRed += pic2.getPixelRed(x+1,y+1)
                averageGreen += pic2.getPixelGreen(x+1,y+1)
                averageBlue += pic2.getPixelBlue(x+1,y+1)
                cells += 1
            except:
                cells = cells
            
            averageRed = averageRed / cells
            averageGreen = averageGreen / cells
            averageBlue = averageBlue / cells
            
            pic.setPixelColor(x,y,averageRed,averageGreen,averageBlue)
            
def zoom(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    pic2 = picture2.Picture(w,h)
    pic2 = copyImage(pic,pic2)
    
    regionX = int((w-1)*.25)
    regionY = int((h-1)*.25)
    
  
    for x in range(0,w-1):
        regionY = int((h-1)*.25)
        for y in range(0,h-1):
            red = pic2.getPixelRed(regionX,regionY)
            green = pic2.getPixelGreen(regionX,regionY)
            blue = pic2.getPixelBlue(regionX,regionY)
            pic.setPixelColor(x,y,red,green,blue)
            if y % 2 == 0 and regionY < h-1:
                regionY += 1
        if x % 2 == 0 and regionX < w - 1:
            regionX +=  1

def copyImage(pic,pic2):
    w = pic.getWidth()
    h = pic.getHeight()
    
    
    
    for x in range(0,w-1):
        for y in range(0,h-1):
                red = pic.getPixelRed(x,y)
                green = pic.getPixelGreen(x,y)
                blue = pic.getPixelBlue(x,y)
                pic2.setPixelRed(x,y,red)
                pic2.setPixelGreen(x,y,green)
                pic2.setPixelBlue(x,y,blue)
                
    return pic2
    
def scrolling(pic,amount):
    w = pic.getWidth()
    h = pic.getHeight()
    
    pic2 = picture2.Picture(w,h)
    pic2 = copyImage(pic,pic2)
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            if x + amount >= w:
                pic.setPixelRed(x,y,  pic2.getPixelRed((x+amount)%w,y)    )
                pic.setPixelGreen(x,y,  pic2.getPixelGreen((x+amount)%w,y)  )
                pic.setPixelBlue(x,y,  pic2.getPixelBlue((x+amount)%w,y)  )
            else:
                pic.setPixelRed(x,y,  pic2.getPixelRed(x+amount,y)  )
                pic.setPixelGreen(x,y,  pic2.getPixelGreen(x+amount,y)  )
                pic.setPixelBlue(x,y,  pic2.getPixelBlue(x+amount,y)    ) 
    
def flipHorizontal(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    
    for x in range(0,(w-1)/2):
        for y in range(0,h-1):
            red = pic.getPixelRed((w-1)-x,y)
            green = pic.getPixelGreen((w-1)-x,y)
            blue = pic.getPixelBlue((w-1)-x,y)
            pic.setPixelColor((w-1)-x,y,pic.getPixelRed(x,y),pic.getPixelGreen(x,y),pic.getPixelBlue(x,y))
            pic.setPixelColor(x,y,red,green,blue)
            
def mirrorHorizontal(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for x in range(0,(w-1)/2):
        for y in range(0,h-1):
            red1 = pic.getPixelRed(x,y)
            green1 = pic.getPixelGreen(x,y)
            blue1 = pic.getPixelBlue(x,y)
            pic.setPixelColor((w-1)-x,y,red1,green1,blue1)
            
def negative(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            pic.setPixelRed(x,y,255-pic.getPixelRed(x,y))
            pic.setPixelGreen(x,y,255-pic.getPixelGreen(x,y))
            pic.setPixelBlue(x,y,255-pic.getPixelBlue(x,y))
            
def grayscale(pict):
    w = pict.getWidth()
    h = pict.getHeight()
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            average = (pict.getPixelRed(x,y)+pict.getPixelGreen(x,y)+pict.getPixelBlue(x,y))/3
            pict.setPixelColor(x,y,average,average,average)

def cycle(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            red = pic.getPixelRed(x,y)
            
            pic.setPixelRed(x,y,pic.getPixelBlue(x,y))
            pic.setPixelBlue(x,y,pic.getPixelGreen(x,y))
            pic.setPixelGreen(x,y,red)
            
def posterize(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            newred = pic.getPixelRed(x,y)-(pic.getPixelRed(x,y)%32)
            newblue = pic.getPixelBlue(x,y)-(pic.getPixelBlue(x,y)%32)
            newgreen = pic.getPixelGreen(x,y)-(pic.getPixelGreen(x,y)%32)
            
            pic.setPixelRed(x,y,newred)
            pic.setPixelGreen(x,y,newgreen)
            pic.setPixelBlue(x,y,newblue)
        
def brightness(pic,amount):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            if pic.getPixelRed(x,y)+amount > 255:
                pic.setPixelRed(x,y,255)
            else:
                pic.setPixelRed(x,y,pic.getPixelRed(x,y)+amount)
            
            if pic.getPixelBlue(x,y)+amount > 255:
                pic.setPixelBlue(x,y,255)
            else:
                pic.setPixelBlue(x,y,pic.getPixelBlue(x,y)+amount)
            
            if pic.getPixelGreen(x,y)+amount > 255:
                pic.setPixelGreen(x,y,255)
            else:
                pic.setPixelGreen(x,y,pic.getPixelGreen(x,y)+amount)  
            
def contrast(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for x in range(0,w-1):
        for y in range(0,h-1):
            red = pic.getPixelRed(x,y)
            green = pic.getPixelGreen(x,y)
            blue = pic.getPixelBlue(x,y)
            
            if red > 128 and red+(red-128)*2 < 255:
                pic.setPixelRed(x,y,red+(red-128)*2)
            elif red > 128 and red+(red-128)*2 > 255:
                pic.setPixelRed(x,y,255)
            
            elif red < 128 and red-(128-red)*2 > 0:
                pic.setPixelRed(x,y,red-(128-red)*2)
            elif red < 128 and red+(red-128)*2 < 0:
                pic.setPixelRed(x,y,0)
            
            
            
            if blue > 128 and blue+(blue-128)*2 < 255:
                pic.setPixelBlue(x,y,blue+(blue-128)*2)
            elif blue > 128 and red+(blue-128)*2 > 255:
                pic.setPixelBlue(x,y,255)
            
            elif blue < 128 and blue-(128-blue)*2 > 0:
                pic.setPixelBlue(x,y,blue-(128-blue)*2)
            elif blue < 128 and blue+(blue-128)*2 < 0:
                pic.setPixelBlue(x,y,0)
                
                
                
                
            if green > 128 and green+(green-128)*2 < 255:
                pic.setPixelGreen(x,y,green+(green-128)*2)
            elif green > 128 and green+(green-128)*2 > 255:
                pic.setPixelGreen(x,y,255)
            
            elif green < 128 and green-(128-green)*2 > 0:
                pic.setPixelGreen(x,y,green-(128-green)*2)
            elif green < 128 and green+(green-128)*2 < 0:
                pic.setPixelGreen(x,y,0)
            
def rotate180(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    
    for y in range(0,(h-1)/2):
        for x in range(0,w-1):
            red = pic.getPixelRed(x,(h-1)-y)
            green = pic.getPixelGreen(x,(h-1)-y)
            blue = pic.getPixelBlue(x,(h-1)-y)
            pic.setPixelColor(x,(h-1)-y,pic.getPixelRed(x,y),pic.getPixelGreen(x,y),pic.getPixelBlue(x,y))
            pic.setPixelColor(x,y,red,green,blue)


main()