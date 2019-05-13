





import picture2, sys


def CycleColorChannel(pic):
    w = pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)

            pic2.setPixelRed(i, j, b)
            pic2.setPixelGreen(i, j, r)
            pic2.setPixelBlue(i, j, g)
        
    return pic2
    
def grayscale(pic):
    
    w = pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            v=(r+g+b)/3
            pic2.setPixelRed(i, j, v)
            pic2.setPixelGreen(i, j, v)
            pic2.setPixelBlue(i, j, v)
    
    return pic2

def mirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    pic2=picture2.Picture(w,h)
    for x in range (0, h-1):
        for z in range (0, w/2):
            r, g, b=pic.getPixelColor(z, x)
            pic2.setPixelColor(z, x, r, g, b)
    for j in range (0,h-1):
        for i in range (w/2, w-1):
            r, g, b=pic.getPixelColor(w-i-1, j)
            pic2.setPixelColor(i, j, r, g, b)
            
    return pic2

def flip(pic):
    w = pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            r, g, b=pic.getPixelColor(w-i-1, j)
            pic2.setPixelColor(i, j, r, g, b)
            
    return pic2


def brightness(pic):
    w = pic.getWidth()
    h=pic.getHeight()
    bright = eval(raw_input("Please enter an amount you would like to change the brightness by:"))
    pic2=picture2.Picture(w,h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            r = pic.getPixelRed(i, j)
            if r > 255:
                    r=255
            if r<0:
                    r=0
            else:
                r = r + bright
            g = pic.getPixelGreen(i, j)
            if g > 255:
                    g=255
            if g<0:
                    g=0
            else:
                g = g + bright
            b = pic.getPixelBlue(i, j)
            if b > 255:
                    b = 255
            if b < 0:
                    b = 0
            else:
                b = b + bright
            pic2.setPixelRed(i, j, r)
            pic2.setPixelGreen(i, j, g)
            pic2.setPixelBlue(i, j, b)
            
    return pic2

def IncreaseContrast(pic):
    w = pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            r = pic.getPixelRed(i, j)
            if r>128:
                r=128+((r-128)*2)
                if r>255:
                    r=255
            elif r<128:
                r=128-((128-r)*2)
                if r<0:
                    r=0
            else:
                r=128
            g = pic.getPixelGreen(i, j)
            if g>128:
                g=128+((g-128)*2)
                if g>255:
                    g=255
            elif g<128:
                g=128-((128-g)*2)
                if g<0:
                    g=0
            else:
                g=128
            b = pic.getPixelBlue(i, j)
            if b>128:
                b=128+((b-128)*2)
                if b>255:
                    b=255
            elif b<128:
                b=128-((128-b)*2)
                if b<0:
                    b=0
            else:
                b=128
            pic2.setPixelRed(i, j, r)
            pic2.setPixelGreen(i, j, g)
            pic2.setPixelBlue(i, j, b)
    return pic2














def posterize(pic):
    W = pic.getWidth()
    H = pic.getHeight()
    pic2 = picture2.Picture(W, H)
    for row in range(0, H - 1):
        for col in range(0, W - 1):
            r = pic.getPixelRed(col, row)
            g = pic.getPixelGreen(col, row)
            b = pic.getPixelBlue(col, row)
            pic2.setPixelRed(col, row, (r//32)*32)
            pic2.setPixelGreen(col, row, (g//32)*32)
            pic2.setPixelBlue(col, row, (b//32)*32)
    return pic2

def zoom(pic):
    W = pic.getWidth()
    H = pic.getHeight()
    col = 0
    row = 0
    pic2 = picture2.Picture(W, H)
    for i in range(W/4, W-W/4-1):
        row = 0
        for j in range(H/4 ,H-H/4-1):
            color = pic.getPixelColor(i, j)
            
            
            pic2.setPixelColor(col, row, color[0], color[1], color[2])
            pic2.setPixelColor(col+1, row, color[0], color[1], color[2])
            pic2.setPixelColor(col, row+1, color[0], color[1], color[2])
            pic2.setPixelColor(col+1, row+1, color[0], color[1], color[2])
            row = row+2
        col = col+2
    return pic2



def scroll(pic):
    W = pic.getWidth()
    H = pic.getHeight()
    pic2 = picture2.Picture(W, H)
    offset = eval(raw_input("Please enter value to scroll the image by:"))
    for row in range(0,H):
        for col in range(0,W):
            r, g, b = pic.getPixelColor(col, row)
            
            
            pic2.setPixelColor(((col + offset)%W),row, r, g, b)
    return pic2




def rotate180(pic):
    w = pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            r, g, b=pic.getPixelColor(w-i-1, h-j-1)
            pic2.setPixelColor(i, j, r, g, b)
            
    return pic2

def colorBlindRed(pic):
    pic = picture2.Picture("crayons.bmp")
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = picture2.Picture(w, h)
    for j in range (0,h-1):
        for i in range (0, w-1):
            g= pic.getPixelGreen(i,j)
            b= pic.getPixelBlue(i,j)
            r=0
            pic2.setPixelGreen(i,j,g)
            pic2.setPixelBlue(i,j,b)
            pic2.setPixelRed(i,j,r)
    return pic2
            

def frame(pic):
    
    pic = picture2.Picture("crayons.bmp")
    W = pic.getWidth()
    H = pic.getHeight()
    pic2 = picture2.Picture(W, H)
    for j in range(5, H-5):
        for i in range(5, W-5):
            r, g, b  = pic.getPixelColor(i,j)
            pic2.setPixelColor(i, j, r, g, b)
    return pic2

def negate(pic):
    
    W = pic.getWidth()
    H = pic.getHeight()
    pic2= picture2.Picture(W, H)
    for row in range(0, H):
        for col in range(0, W):
            r = pic.getPixelRed(col, row)
            g = pic.getPixelGreen(col, row)
            b = pic.getPixelBlue(col, row)
            pic2.setPixelRed(col, row, 255-r)
            pic2.setPixelGreen(col, row, 255-g)
            pic2.setPixelBlue(col, row, 255-b)     
            
    return pic2

def Blur(pic):
    
    w = pic.getWidth()
    h=pic.getHeight()
    pic2=picture2.Picture(w,h)
    for j in range (0,h):
        for i in range (0, w):
            rstorage=0
            gstorage=0
            bstorage=0
            if j-1<0:
                if i-1<0:
                    r=pic.getPixelRed(0,0) + pic.getPixelRed(0,1) + pic.getPixelRed(1,0)+ pic.getPixelRed(1,1)
                    r=r/4
                    pic2.setPixelRed(i,j,r)
                    g=pic.getPixelGreen(0,0) + pic.getPixelGreen(0,1) + pic.getPixelGreen(1,0)+ pic.getPixelGreen(1,1)
                    g=g/4
                    pic2.setPixelGreen(i,j,g)
                    b=pic.getPixelBlue(0,0) + pic.getPixelBlue(0,1) + pic.getPixelBlue(1,0)+ pic.getPixelBlue(1,1)
                    b=b/4
                    pic2.setPixelBlue(i,j,b)
                elif i+1>w-1:
                    r=pic.getPixelRed(w-1,0) + pic.getPixelRed(w-2,0) + pic.getPixelRed(w-2,1)+ pic.getPixelRed(w-1,1)
                    r=r/4
                    pic2.setPixelRed(i,j,r)
                    g=pic.getPixelGreen(w-1,0) + pic.getPixelGreen(w-2,0) + pic.getPixelGreen(w-2,1)+ pic.getPixelGreen(w-1,1)
                    g=g/4
                    pic2.setPixelGreen(i,j,g)
                    b=pic.getPixelBlue(w-1,0) + pic.getPixelBlue(w-2,0) + pic.getPixelBlue(w-2,1)+ pic.getPixelBlue(w-1,1)
                    b=b/4
                    pic2.setPixelBlue(i,j,b)
                    
                else:
                    for m in range (j,j+2):
                        for n in range (i-1,i+2):
                            rstorage= rstorage+pic.getPixelRed(n,m)
                            gstorage= gstorage+pic.getPixelGreen(n,m)
                            bstorage= bstorage+pic.getPixelBlue(n,m)
                    r=rstorage/6
                    g=gstorage/6
                    b=bstorage/6
                    pic2.setPixelRed(i,j,r)
                    pic2.setPixelGreen(i,j,g)
                    pic2.setPixelBlue(i,j,b)
            elif j+1>h-1:
                if i-1<0:
                    r=pic.getPixelRed(0,h-1) + pic.getPixelRed(1,h-1) + pic.getPixelRed(0,h-2)+ pic.getPixelRed(1,h-2)
                    r=r/4
                    pic2.setPixelRed(i,j,r)
                    g=pic.getPixelGreen(0,h-1) + pic.getPixelGreen(1,h-1) + pic.getPixelGreen(0,h-2)+ pic.getPixelGreen(1,h-2)
                    g=g/4
                    pic2.setPixelGreen(i,j,g)
                    b=pic.getPixelBlue(0,h-1) + pic.getPixelBlue(1,h-1) + pic.getPixelBlue(0,h-2)+ pic.getPixelBlue(1,h-2)
                    b=b/4
                    pic2.setPixelBlue(i,j,b)
                elif i+1>w-1:
                    r=pic.getPixelRed(w-1,0) + pic.getPixelRed(w-2,0) + pic.getPixelRed(w-2,1)+ pic.getPixelRed(w-1,1)
                    r=r/4
                    pic2.setPixelRed(i,j,r)
                    g=pic.getPixelGreen(w-1,0) + pic.getPixelGreen(w-2,0) + pic.getPixelGreen(w-2,1)+ pic.getPixelGreen(w-1,1)
                    g=g/4
                    pic2.setPixelGreen(i,j,g)
                    b=pic.getPixelBlue(w-1,0) + pic.getPixelBlue(w-2,0) + pic.getPixelBlue(w-2,1)+ pic.getPixelBlue(w-1,1)
                    b=b/4
                    pic2.setPixelBlue(i,j,b)
                else:
                    for m in range (j-1,j+1):
                        for n in range (i-1,i+2):
                            rstorage= rstorage+pic.getPixelRed(n,m)
                            gstorage= gstorage+pic.getPixelGreen(n,m)
                            bstorage= bstorage+pic.getPixelBlue(n,m)
                    r=rstorage/6
                    g=gstorage/6
                    b=bstorage/6
                    pic2.setPixelRed(i,j,r)
                    pic2.setPixelGreen(i,j,g)
                    pic2.setPixelBlue(i,j,b)
            elif i-1<0:
                for m in range (j-1,j+2):
                    for n in range (i,i+2):
                        rstorage= rstorage+pic.getPixelRed(n,m)
                        gstorage= gstorage+pic.getPixelGreen(n,m)
                        bstorage= bstorage+pic.getPixelBlue(n,m)
                r=rstorage/6
                g=gstorage/6
                b=bstorage/6
                pic2.setPixelRed(i,j,r)
                pic2.setPixelGreen(i,j,g)
                pic2.setPixelBlue(i,j,b)
            elif i+1>w-1:
                for m in range (j-1,j+2):
                    for n in range (i-1,i+1):
                        rstorage= rstorage+pic.getPixelRed(n,m)
                        gstorage= gstorage+pic.getPixelGreen(n,m)
                        bstorage= bstorage+pic.getPixelBlue(n,m)
                r=rstorage/6
                g=gstorage/6
                b=bstorage/6
                pic2.setPixelRed(i,j,r)
                pic2.setPixelGreen(i,j,g)
                pic2.setPixelBlue(i,j,b)
            else:
                for m in range (j-1,j+2):
                    for n in range (i-1,i+2):
                        rstorage= rstorage+pic.getPixelRed(n,m)
                        gstorage= gstorage+pic.getPixelGreen(n,m)
                        bstorage= bstorage+pic.getPixelBlue(n,m)
                r=rstorage/9
                g=gstorage/9
                b=bstorage/9
                pic2.setPixelRed(i,j,r)
                pic2.setPixelGreen(i,j,g)
                pic2.setPixelBlue(i,j,b)
            
    return pic2          
    
def main():
    print "welcome to our image editor. better then photoshop."
    goodInput=False
    while not goodInput:
        try:
            n=raw_input("What picture do you want to use?")
            pic = picture2.Picture(n)
            goodInput=True
        except IOError:
            print""
            print"Please enter a valid picture object."
            print""
    
    print""
    W = pic.getWidth()
    H= pic.getHeight()  
    validInput = False
    while not validInput:
        try:
            print"Thank you for choosing our image Editor."
            print"Enter 0 to Flip the image."
            print"Enter 1 to Mirror the image"
            print"Enter 2 to scroll the image."
            print"Enter 3 to Negate the image."
            print"Enter 4 to Grayscale the Image"
            print"Enter 5 to Cycle Color Channel the Image."
            print"Enter 6 To Zoom the Picture."
            print"Enter 7 To Posterize the image"
            print"Enter 8 to Adjust the Brightness."
            print"Enter 9 to Increase the Contrast."
            print"Enter 10 to Blur the image."
            print"Enter 11 to rotate the image 180 degrees."
            print"Enter 12 to use Edit 1."
            print"Enter 13 to use Edit 2"
            print"Enter 14 to exit the Editor."
            
            image = input("Please enter the manipulation you would like to use on the image:")
            
            if image == 0:
                pic = flip(pic)
            if image == 1:
                pic = mirror(pic)
            if image == 2:
                pic = scroll(pic)
            if (image) == 3:
                pic = negate(pic)           
            if (image) == 4:
                pic = grayscale(pic)          
            if (image) == 5:
                pic = CycleColorChannel(pic)          
            if (image) == 6:
                pic = zoom(pic)           
            if (image) == 7:
                pic = posterize(pic)           
            if (image) == 8:
                pic = brightness(pic)          
            if (image) == 9:
                pic = IncreaseContrast(pic)
            if (image) == 10:
                pic = Blur(pic)         
            if (image) == 11:
                pic = rotate180(pic)           
            if (image) == 12:
                pic = frame(pic)           
            if (image) == 13:
                pic = colorBlindRed(pic)
            if image > 14:
                print "no edit can occur, please enter correct integer between 0 - 14"
            if image < 0:
                print "no edit can occur, please enter correct integer between 0 - 14"
            
            if (image) == 14:
                validInput= True
            pic.display()
            raw_input()
        except TypeError:
            print "enter a number between 0 -14"
        except NameError:
            print "enter a number between 0 - 14"
        except SyntaxError:
            print"enter a number between 0 -14"
        
    pic.display()
    raw_input()
    sys.exit()
    
    
main()



