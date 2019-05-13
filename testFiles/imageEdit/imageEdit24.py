





import picture2

def copy(pic,w,h):
    picCopy=picture2.Picture(w,h)
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            picCopy.setPixelColor(x,y,R,G,B)
    return picCopy
    
def flip(pic,w,h):
    picCopy=copy(pic,w,h)
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            picCopy.setPixelColor(w-1-x,y,R,G,B)
    for x in range (w):
        for y in range (h):
            R,G,B=picCopy.getPixelColor(x,y)
            pic.setPixelColor(x,y,R,G,B)
    return pic

def mirror(pic,w,h):
    picCopy=copy(pic,w,h)
    for x in range ((w)//2):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            picCopy.setPixelColor((w-1-x),y,R,G,B)
    for x in range (w):
        for y in range (h):
            R,G,B=picCopy.getPixelColor(x,y)
            pic.setPixelColor(x,y,R,G,B)
    return pic
    
def scroll(pic,w,h):
    scroll=eval(raw_input("By how many pixels would you like your picture to be moved to the right? "))
    picCopy=copy(pic,w,h)
    for x in range (w):
        for y in range(h):
            R,G,B=pic.getPixelColor(x,y)
            picCopy.setPixelColor(((x+scroll)%w),y,R,G,B)
    for x in range (w):
        for y in range (h):
            R,G,B=picCopy.getPixelColor(x,y)
            pic.setPixelColor(x,y,R,G,B)
    return pic
    
def neg(pic,w,h):
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,(255-R),(255-G),(255-B))
    return pic
    
def gray(pic,w,h):
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,((R+G+B)/3),((R+G+B)/3), ((R+G+B)/3))
    return pic

def cycle(pic,w,h):
    for x in range (w):
        for y in range(h):
            R,G,B=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,B,R,G)
    return pic


def zoom(pic,w,h):
    picCopy=copy(pic,w,h)
    xnew = -2
    ynew = -2
    for x in range ((w-1)//4,3*(w-1)//4):
        xnew = xnew+2
        for y in range ((h-1)//4,3*(h-1)//4):
            ynew=ynew+2
            R,G,B=pic.getPixelColor(x,y)
            picCopy.setPixelColor(xnew, ynew, R,G,B)
            picCopy.setPixelColor(xnew+1, ynew, R,G,B)
            picCopy.setPixelColor(xnew, ynew+1, R,G,B)
            picCopy.setPixelColor(xnew+1, ynew+1, R,G,B)
        ynew=-2
    for x in range (w):
        for y in range (h):
            R,G,B=picCopy.getPixelColor(x,y)
            pic.setPixelColor(x,y,R,G,B)
    return pic
    

def post(pic,w,h):
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,(32*(int(round(R/32)))),(32*int((round(G/32)))),(32*int((round(B/32)))))
    return pic

def bright(pic,w,h):
    print "How much would you like to change the brightness of this picture?"
    bright=eval(raw_input("Please enter a number between 0 and 255: "))
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            R2,G2,B2=R+bright,G+bright,B+bright
            if R2>255:
                R2=255
            elif R2<0:
                R2=0
            if G2>255:
                G2=255
            elif G2<0:
                G2=0
            if B2>255:
                B2=255
            elif B2<0:
                B2=0
            pic.setPixelColor(x,y,R2,G2,B2)
    return pic

def contrast(pic,w,h):
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            if (R-128)*2+R > 255:
                R = 255
            elif (R-128)*2+R < 0:
                R = 0
            else:
                R = (R-128)*2+R
            if (G-128)*2+G > 255:
                G = 255
            elif (G-128)*2+G < 0:
                G = 0
            else:
                G = (G-128)*2+G
            if (B-128)*2+B > 255:
                B = 255
            elif (B-128)*2+B < 0:
                B = 0
            else:
                B = (B-128)*2+B
            pic.setPixelColor(x,y,R,G,B)
    return pic


def blur(pic,w,h):
    picCopy=copy(pic,w,h)
    for x in range (w):
        for y in range(h):
            Ravg=0
            Gavg=0
            Bavg=0
            if x==0 and y==0:
                for i in range (2):
                    for j in range (2):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/4))
                Bavg=int(round(Bavg/4))
                Gavg=int(round(Gavg/4))
            elif x==w-1 and y==0:
                for i in range (-1,1):
                    for j in range (2):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/4))
                Bavg=int(round(Bavg/4))
                Gavg=int(round(Gavg/4))
            elif x==0 and y==h-1:
                for i in range (2):
                    for j in range (-1,1):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/4))
                Bavg=int(round(Bavg/4))
                Gavg=int(round(Gavg/4))
            elif x==w-1 and y==h-1:
                for i in range (-1,1):
                    for j in range (-1,1):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/4))
                Bavg=int(round(Bavg/4))
                Gavg=int(round(Gavg/4))
            elif x==0:
                for i in range (2):
                    for j in range (-1,2):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/6))
                Bavg=int(round(Bavg/6))
                Gavg=int(round(Gavg/6))
            elif x==w-1:
                for i in range (-1,1):
                    for j in range (-1,2):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/6))
                Bavg=int(round(Bavg/6))
                Gavg=int(round(Gavg/6))
            elif y==0:
                for i in range (-1,2):
                    for j in range (2):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/6))
                Bavg=int(round(Bavg/6))
                Gavg=int(round(Gavg/6))
            elif y==h-1:
                for i in range (-1,2):
                    for j in range (-1,1):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/6))
                Bavg=int(round(Bavg/6))
                Gavg=int(round(Gavg/6))
            else:
                for i in range (-1,2):
                    for j in range (-1,2):
                        R,G,B=pic.getPixelColor(x+i,y+j)
                        Ravg=Ravg+R
                        Gavg=Gavg+G
                        Bavg=Bavg+B
                Ravg=int(round(Ravg/9))
                Bavg=int(round(Bavg/9))
                Gavg=int(round(Gavg/9))
            picCopy.setPixelColor(x,y,Ravg,Gavg,Bavg)
    for x in range (w):
        for y in range (h):
            R,G,B=picCopy.getPixelColor(x,y)
            pic.setPixelColor(x,y,R,G,B)
    return pic
    
    
def rotate(pic,w,h):
    picCopy=copy(pic,w,h)
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            picCopy.setPixelColor((w-1-x),(h-1-y),R,G,B)
    for x in range (w):
        for y in range (h):
            R,G,B=picCopy.getPixelColor(x,y)
            pic.setPixelColor(x,y,R,G,B)
    return pic
    
def tiled(pic,w,h):
    print "This will produce an n x n tiled version of your picture."
    n = eval(raw_input("What would you like n to be? "))
    picCopyBig = picture2.Picture(w*n, h*n)
    for x in range (w):
        for y in range (h):
            R,G,B=pic.getPixelColor(x,y)
            for i in range(n):
                for j in range(n):
                    picCopyBig.setPixelColor(x+w*i, y+h*j, R, G, B)
    for x in range(w*n):
        for y in range(h*n):
            if (x%n == 0) and (y%n == 0):
                R, G, B = picCopyBig.getPixelColor(x, y)
                pic.setPixelColor(x/n, y/n, R, G, B)
    return pic  
    
def old(pic,w,h):
    for x in range (w):
        for y in range(h):
            R,G,B=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,(R+112),(G+66),(B+20))
    return pic

def main():
    print "Hello there. You wanna edit that picture of yours, eh?"
    print "We can help you with that!"
    goodInput = False
    while not goodInput:
        fileName=raw_input("Please enter the name of the image file you'd like loaded: ")
        try:
            pic=picture2.Picture(fileName)
            goodInput = True
        except IOError:
            print""
            print "Either that file doesn't exist, or I can't edit it. Try again."
            print""
    w=pic.getWidth()
    h=pic.getHeight()
    Continue=True
    while Continue:
        pic.display()
        try:
            print ""
            print "1=Flip Horizontally    2=Mirror Horizontally    3=Scroll Horizontally"
            print "4=Make Negative    5=Make Grayscale    6=Cycle Color Channels"
            print "7=Zoom    8=Posterize    9=Change Brightness    10=Increase Contrast"
            print "11=Blur    12=Rotate 180 Degrees    13=Make Tiled    14=Make Old Timey"
            print "15=Quit out of editing"
            print ""
            manip=eval(raw_input("What would you like to do to your picture?: "))
            if manip==1:
                pic=flip(pic,w,h)
            elif manip==2:
                pic=mirror(pic,w,h)
            elif manip==3:
                pic=scroll(pic,w,h)
            elif manip==4:
                pic=neg(pic,w,h)
            elif manip==5:
                pic=gray(pic,w,h)
            elif manip==6:
                pic=cycle(pic,w,h)
            elif manip==7:
                pic=zoom(pic,w,h)
            elif manip==8:
                pic=post(pic,w,h)
            elif manip==9:
                pic=bright(pic,w,h)
            elif manip==10:
                pic=contrast(pic,w,h)
            elif manip==11:
                pic=blur(pic,w,h)
            elif manip==12:
                pic=rotate(pic,w,h)
            elif manip==13:
                pic=tiled(pic,w,h)
            elif manip==14:
                pic=old(pic,w,h)
            elif manip==15:
                print "Thanks for using this program! Please come again soon!"
                Continue=False
            else:
                print""
                print "That is not one of the numbers I listed. Please try again!"
        except Exception:
            print""
            print "Huh? I'm sorry, I don't understand. Please try again."
        
main()