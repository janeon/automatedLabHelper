




import picture2


def copyPic (w,h, pic):
    picCopy=picture2.Picture(w,h)
    for i in range(0,w):
        for j in range(0,h):
            (r,g,b) = pic.getPixelColor(i,j)
            picCopy.setPixelColor(i,j,r,g,b)
    return picCopy
 

def negative (w,h, pic):
    for i in range(0, w):
        for j in range(0, h):
            r=pic.getPixelRed(i,j)
            g=pic.getPixelGreen(i,j)
            b=pic.getPixelBlue(i,j)
            pic.setPixelColor(i,j, 255-r, 255-g, 255-b)
    pic.display()
    return pic


def grayscale (w,h, pic):
    for i in range(0, w):
        for j in range(0, h):
            r,g,b= pic.getPixelColor(i,j)
            summ = r + g + b
            avg = summ/3
            pic.setPixelColor(i,j, avg, avg, avg)
    pic.display()
    return pic
    

def colorCycle(w,h,pic):
    for i in range(0,w):
        for j in range(0, h):
            r,g,b= pic.getPixelColor(i,j)
            r,g,b= b,r,g
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    return pic


def posterize(w,h,pic):
    for i in range (0, w):
        for j in range (0, h):
            r,g,b=pic.getPixelColor(i,j)
            r= (r//32)*32
            g= (g//32) *32
            b= (b//32) * 32
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    return pic


def brightness(w,h,pic):
    x= input("How much would you like to change the brightness by: ")
    for i in range (0, w):
        for j in range (0, h):
            r,g,b = pic.getPixelColor(i,j)
            r= r + x
            g= g + x
            b= b + x
            if r> 255:
                r=255
            elif r<0:
                r=0
            if g> 255:
                g=255
            elif g<0:
                g=0    
            if b> 255:
                b=255
            elif b<0:
                b=0
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    return pic


def mirror(w,h,pic):
    picCopy=copyPic(w,h,pic)
    for j in range (0, h):
        for i in range (0, (w//2)):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor(w-1-i,j,r,g,b)
    pic.display()
    return pic


def flip(w,h,pic):
    picCopy=copyPic(w,h,pic)
    for j in range (0, h):
        for i in range (0, w):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor(w-i-1,j, r,g,b)
    pic.display()
    return pic


def scroll(w,h,pic):
    d =input("Please give us a number of pixels to scroll by: ")
    picCopy=copyPic(w,h,pic)
    for i in range (0, w):
        for j in range (0, h):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor((i+d)%w, j, r,g,b)
    pic.display()
    return pic


def contrast(w,h,pic):
    for i in range (0, w):
        for j in range (0, h):
            r,g,b= pic.getPixelColor(i,j)
            r = (2*r)-128
            g = (2*g)-128
            b = (2*b)-128
            if r> 255:
                r=255
            elif r<0:
                r=0
            if g> 255:
                g=255
            elif g<0:
                g=0    
            if b> 255:
                b=255
            elif b<0:
                b=0
            pic.setPixelColor(i,j,r,g,b)
    pic.display()
    return pic





def blur(w,h,pic):
    picCopy=copyPic(w,h,pic)
    for i in range(0,w):
        for j in range (0, h):
            xUL,yUL= i-1, j-1
            xL,yL= i-1,j
            xBL, yBL= i-1, j+1
            xB, yB= i, j+1
            xBR, yBR= i+1, j+1
            xR, yR= i+1, j
            xUR, yUR = i+1, j-1
            xU, yU= i, j-1
            if xUL<0:
                xUL=0
            if yUL <0:
                yUL=0
            if yU<0:
                yU=0
            if xUR >(w-1):
                xUR=(w-1)
            if yUR < 0:
                yUR=0
            if xR> (w-1):
                xR=w-1
            if xBR> (w-1):
                xBR= w-1
            if yBR> (h-1):
                yBR= h-1
            if yB > h-1:
                yB= h-1
            if xBL< 0:
                xBL=0
            if yBL> h-1:
                yBL= h-1
            if xL <0:
                xL=0
            r,g,b = picCopy.getPixelColor(i,j)
            rUL,gUL,bUL=picCopy.getPixelColor(xUL,yUL)
            rL,gL,bL= picCopy.getPixelColor(xL,yL)
            rBL,gBL,bBL= picCopy.getPixelColor(xBL,yBL)
            rB,gB,bB= picCopy.getPixelColor(xB,yB)
            rBR,gBR,bBR= picCopy.getPixelColor(xBR,yBR)
            rR,gR,bR= picCopy.getPixelColor(xR,yR)
            rUR,gUR,bUR= picCopy.getPixelColor(xUR,yUR)
            rU,gU,bU= picCopy.getPixelColor(xU,yU)
            ravg= (r+rUL+rL+rBL+rB+rBR+rR+rUR+rU)//9
            gavg= (g+gUL+gL+gBL+gB+gBR+gR+gUR+gU)//9
            bavg= (b+bUL+bL+bBL+bB+bBR+bR+bUR+bU)//9
            pic.setPixelColor (i,j, ravg,gavg,bavg)
    pic.display()
    return pic


def zoom(w,h,pic):
    enlarge=picture2.Picture(2*w,2*h)
    for j in range(h//4,(3*h//4)):
        for i in range (w//4,(3*w//4)):
            r,g,b=pic.getPixelColor(i,j)
            enlarge.setPixelColor(i*2,2*j, r,g,b)
            enlarge.setPixelColor((2*i)+1,2*j, r,g,b)
            enlarge.setPixelColor((2*i)+1,(2*j)+1, r,g,b)
            enlarge.setPixelColor(2*i,(2*j)+1,r,g,b)
    y = 0
    for j in range(h//2,(3*h//2)):
        x=0
        for i in range (w//2,(3*w//2)):
            r,g,b=enlarge.getPixelColor(i,j)
            pic.setPixelColor(x,y,r,g,b)
            x=x+1
        y=y+1
    pic.display()
    return pic


def rotate(w,h,pic):
    picCopy=copyPic(w,h,pic)
    for j in range (0, h):
        for i in range (0, w):
            r,g,b=picCopy.getPixelColor(i,j)
            pic.setPixelColor(w-i-1,h-j-1, r,g,b)
    pic.display()
    return pic


def blue(w,h,pic):
    for i in range(0, w):
        for j in range(0, h):
            r,g,b= pic.getPixelColor(i,j)
            summ = r + g + b
            avg = summ/3
            pic.setPixelColor(i,j,0,0,avg)
    print
    print "You've selected our special manipulation! As a reward, here's your special message:"
    print
    print "I have a blue house with a blue window"
    print "Blue is the colour of all that I wear."
    print "Blue are the streets and all the trees are too."
    print "I have a girlfriend and she is so blue."
    print "Blue are the people here that walk around,"
    print "Blue like my corvette, it's standing outside."
    print "Blue are the words I say and what I think."
    print "Blue are the feelings that live inside me."
    print 
    print "I'm blue da ba dee da ba die..."
    print
    pic.display()
    return pic


def shutter(w,h,pic):
    d =input("Please give us a value to shutter by: ")
    for i in range (0, w):
        for j in range (0, h):
            r,g,b=pic.getPixelColor(i,j)
            pic.setPixelColor((i+d)%w, j, r,g,b)
    pic.display()
    return pic


def main():
    print "Welcome to our Image Editor!"
    fileName=raw_input("Please enter the file name of the image you would like to edit: ")
    try:
        pic=picture2.Picture(fileName)
        w=pic.getWidth()
        h=pic.getHeight()
        done=False
        print
        print "This allows you to make multiple manipulations on any image you upload."
        print
        print "Your manipulation options are: negative, grayscale, color cycle, posterize, brightness, mirror, flip, scroll, contrast, blur, zoom, rotate, shutter, and blue."
        print
        print "Type the manipulation you'd like to see implemented, then press enter. Repeat this process until you're satisfied with your image, and then type exit. Have fun!"
        print
        while not done:
            x=raw_input("How would you like to change your image:  ")
            if x == "negative":
                pic=negative(w,h,pic)
            elif x== "grayscale":
                pic=grayscale(w,h,pic)
            elif x == "color cycle":
                pic=colorCycle(w,h,pic)
            elif x =="posterize":
                pic=posterize(w,h,pic)
            elif x == "brightness":
                pic= brightness(w,h,pic)
            elif x == "mirror":
                pic=mirror(w,h,pic)
            elif x == "flip":
                pic=flip(w,h,pic)
            elif x == "scroll":
                pic=scroll(w,h,pic)
            elif x == "contrast":
                pic=contrast(w,h,pic)
            elif x == "blur":
                pic= blur(w,h,pic)
            elif x == "zoom":
                pic=zoom(w,h,pic)
            elif x =="rotate":
                pic= rotate(w,h,pic)
            elif x == "blue":
                pic=blue(w,h,pic)
            elif x == "shutter":
                pic=shutter(w,h,pic)
            elif x == "exit":
                print
                print "Thanks for stopping by. Try again with some different manipulations!"
                done= True
            else:
                print "Oops! That's not a manipulation we offer here. Please try again."
                
    except SyntaxError:
        print "Oops! You entered something I didn't understand. Re-read the instructions and make sure you're typing the right command at the right time!"
    except IOError:
        print "I'm sorry, that file does not exist. Please try again."
    except Exception as e:
        print "I'm sorry, something else went wrong. Please try again."
        print (type(e))
        print (str(e))
    
    
   
       
    
    
main()