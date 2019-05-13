








import math
import picture2

def copy(pic,W,H):    
    picCopy=picture2.Picture(W,H)
    for j in range (0,H):
        for i in range(0,W):
            r,g,b=pic.getPixelColor(i,j)
            picCopy.setPixelColor(i,j,r,g,b)
    return picCopy

def blur(pic,W,H):  
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r=0
            B=0
            g=0
            if i == 0: 
                i=i+1
            if i == W-1: 
                i=W-2
            if j == 0: 
                j=j+1
            if j == H-1:
                j=H-2
            for a in range(i-1,i+2):      
                for b in range (j-1,j+2):
                        r = r + picCopy.getPixelRed(a,b)
                        B = B + picCopy.getPixelBlue(a,b)
                        g = g + picCopy.getPixelGreen(a,b)
                pic.setPixelColor(i,j,(r/9),(g/9),(B/9))  
    return pic


def make_gray(pic,W,H):   
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            average=((r+g+b)/3)
            pic.setPixelColor(i,j,average,average,average)
    return pic


def zoom(pic,W,H):  
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor((i//2+W/4-1),(j//2+H/4-1))  
            pic.setPixelColor(i,j,r,g,b)
    return pic


def mirror(pic,W,H): 
    picCopy=copy(pic,W,H)
    for i in range(0,W/2):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor(W-i-1,j,r,g,b)
    return pic

def rotate(pic,W,H):  
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor(W-i-1,H-j-1,r,g,b)
    return pic

    
def flipy(pic,W,H): 
    picCopy=copy(pic,W,H)
    for i in range(0,W/2):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            R,G,B=picCopy.getPixelColor((W-i-1),j)
            pic.setPixelColor(i,j,R,G,B)
            pic.setPixelColor((W-i-1),j,r,g,b)
    return pic

 
    
def scroll(pic,W,H): 
    goodInput=False
    while not goodInput:
        try:
            n=eval(raw_input("Enter the number of pixels to scroll the image: "))
            picCopy=copy(pic,W,H)
            for j in range(0,H):
                for i in range(0,(W)):
                    r,g,b=picCopy.getPixelColor(i,j)
                    pic.setPixelColor(((i+n)%W),j,r,g,b)
            goodInput = True
        except:
            print "Enter regular numbers silly"
    return pic

    
def poster(pic,W,H):  
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            r=int((round(r/32))*32)
            g=int((round(g/32))*32)
            b=int((round(b/32))*32)
            pic.setPixelColor(i,j,r,g,b)
    return pic

    
def brightness(pic,W,H): 
    picCopy=copy(pic,W,H)
    goodInput=False
    while not goodInput:
        try:
            n=eval(raw_input("Please enter an integer to change the brightness: "))
            for i in range(0,W):
                for j in range(0,H):
                    r,g,b=picCopy.getPixelColor(i,j)
                    r,g,b=((r+n),(g+n),(b+n))
                    if r >255:  
                        r == 255
                    if g >255:
                        g == 255
                    if b >255:
                        b == 255
                    if r <0:
                        r == 0
                    if g < 0:
                        g == 0
                    if b < 0:
                        g == 0
                    pic.setPixelColor(i,j,r,g,b)
                    goodInput=True
        except:
            print "Enter regular numbers silly"
    return pic
  
    
    
def cycle(pic,W,H):  
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            r,g,b=b,r,g
            pic.setPixelColor(i,j,r,g,b)
    return pic
 
    
    
def make_neg(pic,W,H): 
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor(i,j,(255-r),(255-g),(255-b))
    return pic

    
    
def contrast(pic,W,H):  
    picCopy=copy(pic,W,H)
    for i in range(0,W):
        for j in range(0,H):
            r,g,b = picCopy.getPixelColor(i,j)
            r=(((r-128)*2)+r)
            g=(((g-128)*2)+g)
            b=(((b-128)*2)+b)
            pic.setPixelColor(i,j,r,g,b)
    return pic

    
def dotty(pic,W,H): 
    picCopy=copy(pic,W,H)
    for i in range(0,W-3,3):
        for j in range(0,H-3,3):
            r=0
            B=0
            g=0
            for a in range(i,i+3,):
                for b in range (j,j+3):
                    r = r + picCopy.getPixelRed(a,b)
                    B = B + picCopy.getPixelBlue(a,b)
                    g = g + picCopy.getPixelGreen(a,b)
            pic.setPixelColor(i,j,(r/9),(B/9),(g/9))
    return pic



def halfy(pic,W,H): 
    picCopy=copy(pic,W,H)
    for i in range(0,W/2):
        for j in range(0,H-1):
            r,g,b=picCopy.getPixelColor(i,j)
            R,B,G=picCopy.getPixelColor((W-i-1),j)
            pic.setPixelColor(i,j,R,G,B)
            pic.setPixelColor((W-i-1),j,r,g,b)
    return pic




def main(): 
    pic = False
    choices = True
    print "\nWelcome to my wonderful free picture editor!\n"
    while not pic:    
        try:
            image=raw_input("What image would you like to edit? ")  
            pic = picture2.Picture(image)
            W = pic.getWidth()
            H = pic.getHeight()
            while choices == True:  
                pic.display()  
                print "Here is a list of possible effects you can implement on your picture!"
                print "If at any time you would like to exit just type 'exit'"
                print " "
                print "1.Flip Horizontally"
                print "2. Mirror Horizontally"
                print "3. Scroll Horizontally"
                print "4. Make Negative"
                print "5. Make Grayscale"
                print "6. Cycle Color Channels"
                print "7. Zoom"
                print "8. Posterize"
                print "9. Change Brightness"
                print "10. Increase Contrast"
                print "11. Blur"
                print "12. Rotate 180 Degrees"
                print "13. Make Dotty"
                print "14. Half way flip and color change"
                goodInput = False
                while not goodInput:  
                    try:
                        p=0
                        choice=raw_input("\nChoose one and enjoy: ")
                        if choice == "1":
                            p=flipy(pic,W,H)
                        elif choice == "2":
                            p=mirror(pic,W,H)
                        elif choice == "3":
                            p=scroll(pic,W,H)
                        elif choice == "4":
                            p=make_neg(pic,W,H)
                        elif choice == "5":
                            p=make_gray(pic,W,H)
                        elif choice == "6":
                            p=cycle(pic,W,H)
                        elif choice == "7":
                            p=zoom(pic,W,H)
                        elif choice == "8":
                            p=poster(pic,W,H)
                        elif choice == "9":
                            p=brightness(pic,W,H)
                        elif choice == "10":
                            p=contrast(pic,W,H)
                        elif choice == "11":
                            p=blur(pic,W,H)
                        elif choice == "12":
                            p=rotate(pic,W,H)
                        elif choice == "13":
                            p=dotty(pic,W,H)
                        elif choice == "14":
                            p=halfy(pic,W,H)
                        elif choice == "exit":
                            return False
                        else:
                            print "That isn't one of the options, try again.\n"
                        p.display()
                        goodInput = True
                    except:
                        print"Please follow instructions."
        except IOError:
            print"Load an existing file"
        except:
            print "Try loading a .bmp file"
                

main()










