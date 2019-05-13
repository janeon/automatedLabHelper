





import picture2
import math

def Rain(pic,w,h):
    for x in range(0,(w-1)):
        for y in range(0, (h-1)):
            if x % 37 ==0 and y%3 == 0 and (x+y) % 15 == 0:
                
                pic.setPixelColor(x, y, 0, 0, 255)
            elif x %55 ==0 and y % 7 == 0:
                pic.setPixelColor(x, y, 0, 100, 255)
                
    pic.display()
    raw_input()
def scrollHorizontally(pic, w, h):
    bool = True
    while bool == True:
        try:
            n = eval(raw_input("Please enter how many pixels you would like to scroll to the right: "))
            pic2 = Copier(pic,w,h)

            for x in range(0, w-1):
                    for y in range(0, h-1):
                        r,g,b = pic2.getPixelColor(x,y)

                        newR = r
                        newG = g
                        newB = b
                        if (x+n) <= w:
                            pic.setPixelColor((x-1)+n,y, newR, newG, newB)
            for x in range(0, n):

                    for y in range(0, h-1):
                        r,g,b = pic2.getPixelColor((w-1)-x,y)

                        newR = r
                        newG = g
                        newB = b
                        pic.setPixelColor(x,y, newR, newG, newB)
            bool = False
            pic.display()
            raw_input()
        except Exception as e:
            print "It seems you have received ", str(e), "error.  Please provide a different number!"
def flipHorizontally(pic, w, h):
    pic2 = Copier(pic,w,h)

    for x in range(0, w-1):
        for y in range(0, h-1):
            r,g,b = pic2.getPixelColor(x,y)

            newR = r
            newG = g
            newB = b
            pic.setPixelColor((w-1)-x,y, newR, newG, newB)
    pic.display()
    raw_input()


def negatives(pic, w, h):
    for x in range(0, w-1):
        for y in range(0, h-1):
            r,g,b = pic.getPixelColor(x,y)
            newR = (255 - r)
            newG = 255 - g
            newB = 255 - b
            pic.setPixelColor(x,y, newR, newG, newB)
    pic.display()
    raw_input()

def mirrorHorizontally(pic, w, h):
    for x in range(0, (w/2)+1):
        for y in range(0, h-1):
            r,g,b = pic.getPixelColor(x,y)
            newR = r
            newG = g
            newB = b
            width= (w-1)-x
            pic.setPixelColor(width,y, newR, newG, newB)
    pic.display()
    raw_input()

def cycleColorChannels(pic, w, h):
    for x in range(0, w-1):
        for y in range(0, h-1):
            r,g,b = pic.getPixelColor(x,y)
            newR = b
            newG = r
            newB = g
            pic.setPixelColor(x,y, newR, newG, newB)
    pic.display()
    raw_input()

def increaseContrast(pic, w, h):
    for x in range(0, w-1):
        for y in range(0, h-1):
            r,g,b = pic.getPixelColor(x,y)
            
            if r == 128:
                newR = 128
            elif r > 128:
                difR = r-128
                newR = r + (difR*2)
            else:
                difR = 128-r
                newR = r - (difR*2)
                
            if g == 128:
                newG = 128
            elif g > 128:
                difG = g-128
                newG = g + (difG*2)
            else:
                difG = 128-g
                newG = g - (difG*2)
            
            if b == 128:
                newb = 128
            elif b > 128:
                difB = b-128
                newB = b + (difB*2)
            else:
                difB = 128-b
                newB = b - (difB*2)
            
            pic.setPixelColor(x,y, newR, newG, newB)
    pic.display()
    raw_input()
def Regret (pic,w,h):
    Badness = input("Please give a numerical value to how much you despise this picture: ")
    if Badness > 75:
        Badness = 75
        pic.setPenWidth(Badness)
        pic.drawLine(0,0,w-2,h-2)
        pic.drawLine(w-2,0,0,h-2)
    else:
        pic.setPenWidth(Badness)
        pic.drawLine(0,0,w-2,h-2)
        pic.drawLine(w-2,0,0,h-2)
    
    
    
    
    
    
    
    pic.display()
    raw_input()
                
                
                
        
    
    
def Rotate180Degrees(pic, w, h):
    CopyPic = Copier(pic, w, h)
    for x in range(0,(w-1)):
        for y in range(0, (h-1)):
            r,g,b = CopyPic.getPixelColor(w-1-x,h-1-y)
            pic.setPixelColor(x, y, r, g, b)
    pic.display()
    raw_input()
        

def Blur(pic, w, h): 
    CopyPic = Copier(pic,w,h)
    for x in range(0,(w-1)):
        for y in range(0, (h-1)):
            RB = 0
            GB = 0
            BB = 0
            if x == 0 and y == 0:
                RB = RB + CopyPic.getPixelRed(x,y)
                RB = RB + CopyPic.getPixelRed(x+1,y)
                RB = RB + CopyPic.getPixelRed(x+1,y+1)
                RB = RB + CopyPic.getPixelRed(x,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y)
                BB = BB + CopyPic.getPixelBlue(x+1,y)
                BB = BB + CopyPic.getPixelBlue(x+1,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y+1)
                pic.setPixelColor(x,y, RB/4, GB/4,BB/4)
            elif x == (w-2) and y == (h-2):
                RB = RB + CopyPic.getPixelRed(x,y)
                RB = RB + CopyPic.getPixelRed(x-1,y)
                RB = RB + CopyPic.getPixelRed(x-1,y-1)
                RB = RB + CopyPic.getPixelRed(x,y-1)
                GB = GB + CopyPic.getPixelGreen(x,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y-1)
                GB = GB + CopyPic.getPixelGreen(x,y-1)
                BB = BB + CopyPic.getPixelBlue(x,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y-1)
                BB = BB + CopyPic.getPixelBlue(x,y-1)
                pic.setPixelColor(x,y, RB/4, GB/4,BB/4)
            elif y == 0 and x !=0:
                RB = RB + CopyPic.getPixelRed(x,y)
                RB = RB + CopyPic.getPixelRed(x+1,y)
                RB = RB + CopyPic.getPixelRed(x+1,y+1)
                RB = RB + CopyPic.getPixelRed(x,y+1)
                RB = RB + CopyPic.getPixelRed(x-1,y)
                RB = RB + CopyPic.getPixelRed(x-1,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y+1)
                GB = GB + CopyPic.getPixelGreen(x-1,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y+1)
                BB = BB + CopyPic.getPixelBlue(x+1,y)
                BB = BB + CopyPic.getPixelBlue(x+1,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y+1)
                pic.setPixelColor(x,y, RB/6, GB/6,BB/6)
            elif x == 0 and y != 0:
                RB = RB + CopyPic.getPixelRed(x,y)
                RB = RB + CopyPic.getPixelRed(x+1,y)
                RB = RB + CopyPic.getPixelRed(x+1,y+1)
                RB = RB + CopyPic.getPixelRed(x,y+1)
                RB = RB + CopyPic.getPixelRed(x,y-1)
                RB = RB + CopyPic.getPixelRed(x+1,y-1)
                GB = GB + CopyPic.getPixelGreen(x,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y-1)
                GB = GB + CopyPic.getPixelGreen(x+1,y-1)
                BB = BB + CopyPic.getPixelBlue(x,y)
                BB = BB + CopyPic.getPixelBlue(x,y-1)
                BB = BB + CopyPic.getPixelBlue(x+1,y-1)
                BB = BB + CopyPic.getPixelBlue(x+1,y)
                BB = BB + CopyPic.getPixelBlue(x+1,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y+1)
                pic.setPixelColor(x,y, RB/6, GB/6,BB/6)
            elif x == (w-2) and y != (h-2):
                RB = RB + CopyPic.getPixelRed(x,y)
                RB = RB + CopyPic.getPixelRed(x-1,y)
                RB = RB + CopyPic.getPixelRed(x-1,y-1)
                RB = RB + CopyPic.getPixelRed(x,y-1)
                RB = RB + CopyPic.getPixelRed(x,y+1)
                RB = RB + CopyPic.getPixelRed(x-1,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y-1)
                GB = GB + CopyPic.getPixelGreen(x,y-1)
                GB = GB + CopyPic.getPixelGreen(x-1,y+1)
                GB = GB + CopyPic.getPixelGreen(x,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y-1)
                BB = BB + CopyPic.getPixelBlue(x,y-1)
                BB = BB + CopyPic.getPixelBlue(x-1,y+1)
                BB = BB + CopyPic.getPixelBlue(x,y+1)
                pic.setPixelColor(x,y, RB/6, GB/6,BB/6)
            elif y == (h-2) and x != (w-2):
                RB = RB + CopyPic.getPixelRed(x,y)
                RB = RB + CopyPic.getPixelRed(x-1,y)
                RB = RB + CopyPic.getPixelRed(x-1,y-1)
                RB = RB + CopyPic.getPixelRed(x,y-1)
                RB = RB + CopyPic.getPixelRed(x+1,y)
                RB = RB + CopyPic.getPixelRed(x+1,y-1)
                GB = GB + CopyPic.getPixelGreen(x,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y)
                GB = GB + CopyPic.getPixelGreen(x-1,y-1)
                GB = GB + CopyPic.getPixelGreen(x,y-1)
                GB = GB + CopyPic.getPixelGreen(x+1,y)
                GB = GB + CopyPic.getPixelGreen(x+1,y-1)
                BB = BB + CopyPic.getPixelBlue(x,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y)
                BB = BB + CopyPic.getPixelBlue(x-1,y-1)
                BB = BB + CopyPic.getPixelBlue(x,y-1)
                BB = BB + CopyPic.getPixelBlue(x+1,y)
                BB = BB + CopyPic.getPixelBlue(x+1,y-1)
                pic.setPixelColor(x,y, RB/6, GB/6,BB/6)
            else:       
                for i in range(0,3):
                    for j in range(0,3):
                        RB = RB + CopyPic.getPixelRed(x-1+j,y+1-i)
                        GB = GB + CopyPic.getPixelGreen(x-1+j,y+1-i)
                        BB = BB + CopyPic.getPixelBlue(x-1+j, y +1 - i)
                        
                pic.setPixelColor(x,y,RB/9,GB/9,BB/9)

    pic.display()
    raw_input()
            
            
            
                
    
def Copier(pic,w,h):
    pic = picture2.Picture("crayons.bmp")
    w = pic.getWidth()
    h = pic.getHeight()
    Copy = picture2.Picture(w,h)
    for i in range(0,(w-1)):
        for j in range(0, (h-1)):
            r,g,b = pic.getPixelColor(i,j)
            Copy.setPixelColor(i,j,r,g,b)
    return(Copy)

    
    
    

def Zoom(pic,w,h):
    CopyPic = Copier(pic,w,h)
    for i in range(0,(w-1)):
        for j in range(0, (h-1)):
            r,g,b = CopyPic.getPixelColor(((w/4)+(i/2)),((h/4)+(j/2)))
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    raw_input()
    


    

    
    
def Posterize(pic,w,h):
    for i in range(0,(w-1)):
        for j in range(0, (h-1)):
            r,g,b = pic.getPixelColor(i,j)
            rP = (((r+16)//32)*32)
            gP = (((g+16)//32)*32)
            bP = (((b+16)//32)*32)                   
            pic.setPixelColor(i,j,rP,gP,bP)
    pic.display()
    raw_input()
    
def SafeCheck(R,G,B):
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return (R,G,B)
def ChangeBrightness(pic,w,h):
    Change = input("How much would you like to change your number by?: ")
    for i in range(0,w-1):
        for j in range(0,h-1):
            r,g,b = pic.getPixelColor(i,j)
            RChange = r + Change
            GChange = g + Change
            BChange = b + Change
            RB, GB, BB= SafeCheck(RChange,GChange,BChange)
            pic.setPixelColor(i,j,RB, GB, BB)
    pic.display()
    raw_input()

def MakeGreyscale(pic,w,h):
    for i in range(0,(w-1)):
        for j in range(0, (h-1)):
            Color = pic.getPixelColor(i,j)
            Grey = (sum(Color))/3
            pic.setPixelColor(i,j,Grey,Grey,Grey)
    pic.display()
    raw_input()
    
    


def main():
    print "Welcome to an image munipulator"
    done = False
    while not done:
        fileName = raw_input("Please enter the image file you'd like loaded: ")
        try:
            pic = picture2.Picture(fileName)
            done = True
        except IOError:
            print "There is no such file or directory please retype"
    
    w = pic.getWidth()
    h = pic.getHeight()
    Done = False
    SuperDone = False
    print "You can change your image in the following ways:"
    print " 1 Flip Horizontally,  2 Mirror Horizontally, 3 Scroll Horizontally"
    print "4 Make Negative, 5 Make Grayscale, 6 Cycle Color Channels, 7 Zoom"
    print "8 Posterize,9 Change Brightness,10 Increase Contrast,"
    print "11 Blur, 12 Rotate 180 Degrees, 13 Regreterize or 14 Make it Rain"
    while not Done:
        Mod = raw_input("Type the number of the way you want to change your file or blank to quit: ") 
        if Mod == "5":
            
    
            MakeGreyscale(pic,w,h)
            
        elif Mod == "9":
            
            ChangeBrightness(pic,w,h)
            
        elif Mod == "3":
            
            scrollHorizontally(pic, w, h)
            
            
        elif Mod == "1":
            
            flipHorizontally(pic, w, h)
            
            
        elif Mod == "8":
            
            Posterize(pic,w,h)
            
        elif Mod == "14":
            Rain(pic,w,h)
        elif Mod == "7":
            
            Zoom(pic,w,h)
            
            
        elif Mod == "11":
            
            Blur(pic,w,h)
            
        elif Mod == "12":
            
            Rotate180Degrees(pic,w,h)
            
        elif Mod == "13":
            
            Regret(pic,w,h)
            
        elif Mod == "4":
            
            negatives(pic, w, h)
            
        elif Mod == "2":
            
            mirrorHorizontally(pic, w, h)
            
        elif Mod == "6":
            
            cycleColorChannels(pic, w, h)
            
        elif Mod == "10":
            
            increaseContrast(pic, w, h)
            
        elif Mod == "":
            Done = True
            print "I guess we are done here then"
        else:
            print "I am sorry that is not one of the options avalible"
    
main()
