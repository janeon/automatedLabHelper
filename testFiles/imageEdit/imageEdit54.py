





import picture2


def negative(pic,w,h): 
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,255-r,255-g,255-b)

def grayscale(pic,w,h): 
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            average=(r+g+b)/3
            pic.setPixelColor(x,y,average,average,average)

def colorchannels(pic,w,h): 
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,b,r,g)

def brightness(pic,w,h): 
    n=eval(raw_input("Please enter the amount you want to increase brightness: "))
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,r+n,g+n,b+n)
            
def contrast(pic,w,h): 
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,(r-128)*2+128,(g-128)*2+128,(b-128)*2+128)
            
def posterize(pic,w,h): 
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            r=((r+16)//32)*32
            g=((g+16)//32)*32
            b=((b+16)//32)*32
            pic.setPixelColor(x,y,r,g,b)
            
def flip(pic,w,h): 
    for x in range(0,w/2):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(w-1-x,y)
            f,l,c=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,r,g,b)
            pic.setPixelColor(w-1-x,y,f,l,c)
            
def mirror(pic,w,h): 
    for x in range(0,w/2):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(x,y)
            pic.setPixelColor(w-1-x,y,r,g,b)
            
def scroll(pic,w,h): 
    try:
        d=eval(raw_input("Please enter how far you want to shift it:"))
        newpic=picture2.Picture(w,h)
        for x in range(0,w-1):
            for y in range(0,h-1):
                r,g,b=pic.getPixelColor(x,y)
                newpic.setPixelColor((x+d)%w,y,r,g,b)
        for x in range(0,w-1):
            for y in range(0,h-1):
                r,g,b=newpic.getPixelColor(x,y)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
    except NameError:
        print "Please only enter numbers \n"
    except TypeError:
        print "Please only enter 1 number \n"
    except SyntaxError:
        print "please only enter 1 number \n"

def rotate(pic,w,h): 
    for x in range(0,w/2):
        for y in range(0,h-1):
            r,g,b=pic.getPixelColor(w-1-x,h-1-y)
            f,l,c=pic.getPixelColor(x,y)
            pic.setPixelColor(x,y,r,g,b)
            pic.setPixelColor(w-1-x,h-1-y,f,l,c)
            
            
def averageColor(pic,w,h,x,y): 
    r,g,b=0,0,0
    p=0
    for i in range(-1,2):
        for j in range(-1,2):
            if x+i>=0 and x+i<=w-1 and y+j>=0 and y+j<=h-1:
                f,l,c=pic.getPixelColor(x+i,y+1)
                r,g,b=(r+f),(g+l),(c+b)
                p=p+1
    
    r,g,b=r/p,g/p,b/p
    return r,g,b
    

def blur(pic,w,h): 
    newpic=picture2.Picture(w,h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=averageColor(pic,w,h,x,y)
            newpic.setPixelColor(x,y,r,g,b)
    for x in range(0,w-1):  
        for y in range(0,h-1):
            r,g,b=newpic.getPixelColor(x,y)
            pic.setPixelColor(x,y,r,g,b)


def zoomPixel(pic,newpic,w,h,x,y): 
    for i in range(0,2):
        for j in range(0,2):
                r,g,b=pic.getPixelColor(x,y)
                newpic.setPixelColor((x-(w/4))*2+i,(y-(h/4))*2+j,r,g,b)
        
            
def zoom(pic,w,h): 
    newpic=picture2.Picture(w+1,h+1)
    for x in range(w/4,3*w/4-1):
        for y in range(h/4,3*h/4-1):
            zoomPixel(pic,newpic,w,h,x,y)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r,g,b=newpic.getPixelColor(x,y)
            pic.setPixelColor(x,y,r,g,b)
        

            
def mirrorVertically(pic,w,h): 
    for y in range(0,h/2):
        for x in range(0,w-1):
            r,g,b=pic.getPixelColor(x,y)
            pic.setPixelColor(x,h-1-y,r,g,b)

def removeColor(pic,w,h): 
    try:
        print "This programs removes all of the red,blue or green from the image based on your desires"
        n=eval(raw_input("Please enter either 1,2 or 3, corresponding to removing red, green and blue: "))
        if n==1:
            for x in range(0,w-1):
                for y in range(0,h-1):
                    pic.setPixelRed(x,y,0)
        if n==3:
            for x in range(0,w-1):
                for y in range(0,h-1):
                    pic.setPixelBlue(x,y,0)
        if n==2:
            for x in range(0,w-1):
                for y in range(0,h-1):
                    pic.setPixelGreen(x,y,0)
        pic.display()
    except NameError:
        print "please only enter numbers \n"
    except TypeError:
        print "please only enter 1 number \n"
    except SyntaxError:
        print "please only enter 1 number \n"
        
    
            
                     

def main():
    q=True
    while q==True:
        try:
            fileName=raw_input("Please enter the image file you'd like loaded: ")
            pic=picture2.Picture(fileName)
            w= pic.getWidth()
            h= pic.getHeight()
            n=True
            print "Welcome to my image editor"
            print "It performs a variety of operations"
            print "Select the number that corresponds to the function you would like to perform \n"
            while n==True:
                print "0=rotate 180 degrees"
                print "1=horizontally scroll the picture"
                print "2=mirror horizontally"
                print "3=flip horizontally"
                print "4=posterize the picture"
                print "5=Increase the contrast"
                print "6=increase the brightness by a specific amount"
                print "7=Cycle Color Channels"
                print "8=Grayscale the picture"
                print "9=Make the picture negative"
                print "10=Blur the picture"
                print "11=Zoom the picture"
                print "12=Removes the color of your choosing (my own effect 1)"
                print "13=Mirror vertically (my own effect 2)"
                print "14=I am done \n"
                try:
                    p=eval(raw_input("Please enter the a number: "))
                    if p==0:
                        rotate(pic,w,h)
                        pic.display()
                    elif p==1:
                        scroll(pic,w,h)
                    elif p==2:
                        mirror(pic,w,h)
                        pic.display()
                    elif p==3:
                        flip(pic,w,h)
                        pic.display()
                    elif p==4:
                        posterize(pic,w,h)
                        pic.display()
                    elif p==5:
                        contrast(pic,w,h)
                        pic.display()
                    elif p==6:
                        brightness(pic,w,h)
                        pic.display()
                    elif p==7:
                        colorchannels(pic,w,h)
                        pic.display()
                    elif p==8:
                        grayscale(pic,w,h)
                        pic.display()
                    elif p==9:
                        negative(pic,w,h)
                        pic.display()
                    elif p==10:
                        blur(pic,w,h)
                        pic.display()
                    elif p==11:
                        zoom(pic,w,h)
                        pic.display()
                    elif p==12:
                        removeColor(pic,w,h)
                    elif p==13:
                        mirrorVertically(pic,w,h)
                        pic.display()
                    elif p==14:
                        n=False
                except NameError:
                    print "Please only enter numbers \n"
                except TypeError:
                    print "Please only enter 1 number \n"
                except SyntaxError:
                    print "Please only enter 1 number \n"
                    
            print "Thanks for using my Image Editor."
            n=False
            break
        except IOError:
            print "please enter a file in your directory"
main()




