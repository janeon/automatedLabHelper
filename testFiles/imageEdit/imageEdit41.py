







import picture2

def createcopy(pic,w,h):
    pic1 = picture2.Picture(w,h)
    for i in range(0,w-1):
        for j in range(0,h-1):
            r = pic.getPixelRed(i,j)
            g = pic.getPixelGreen(i,j)
            b = pic.getPixelBlue(i,j)
            pic1.setPixelColor(i, j, r, g, b)
    return pic1


def fliphorizontal(pic,w,h):
    for i in range(0, (w)//2):
        for j in range(0, h-1):
            r1 = pic.getPixelRed(w-1-i,j)
            g1 = pic.getPixelGreen(w-1-i,j)
            b1 = pic.getPixelBlue(w-1-i,j)
            r2 = pic.getPixelRed(i,j)
            g2 = pic.getPixelGreen(i,j)
            b2 = pic.getPixelBlue(i,j)
            pic.setPixelColor(i, j, r1, g1, b1)
            pic.setPixelColor((w-1-i),j, r2, g2, b2)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
   
def mirrorhorizontal(pic,w,h):
    for i in range(w//2,w-1):
        for j in range(0, h-1):
            r1 = pic.getPixelRed(w-1-i,j)
            g1 = pic.getPixelGreen(w-1-i,j)
            b1 = pic.getPixelBlue(w-1-i,j)
            r2 = pic.getPixelRed(i,j)
            g2 = pic.getPixelGreen(i,j)
            b2 = pic.getPixelBlue(i,j)
            pic.setPixelColor(i, j, r1, g1, b1)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
  
def scrollhorizontal(pic1,pic2,w,h):
    pxls = raw_input("How many pixels do you want to shift to the right?: ")
    for i in range(0,w-1):
        for j in range(0,h-1):
            r1 = pic2.getPixelRed(i,j)
            g1 = pic2.getPixelGreen(i,j)
            b1 = pic2.getPixelBlue(i,j)
            pic1.setPixelColor((i + int(pxls))%w, j, r1, g1, b1)
    pic1.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
                           

def negative(pic,w,h):
    for i in range(0,w-1):
        for j in range(0,h-1):
            r = pic.getPixelRed(i,j)
            g = pic.getPixelGreen(i,j)
            b = pic.getPixelBlue(i,j)
            pic.setPixelColor(i,j,255-r,255-g,255-b)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
def grayscale(pic,w,h):
    for i in range(0,w-1):
        for j in range(0,h-1):
            r = pic.getPixelRed(i,j)
            g = pic.getPixelGreen(i,j)
            b = pic.getPixelBlue(i,j)
            gray = (r+g+b)//3
            pic.setPixelColor(i,j,gray,gray,gray)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
   
def cyclecolor(pic1,pic2,w,h):
    for i in range(0,w-1):
        for j in range(0,h-1):
            r1 = pic2.getPixelRed(i,j)
            g1 = pic2.getPixelGreen(i,j)
            b1 = pic2.getPixelBlue(i,j)
            pic1.setPixelColor(i, j, b1, r1, g1)                
    pic1.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    

def zoom(pic1,pic2,w,h):
    for i in range(0, w, 2):
        for j in range(0, h, 2):
            r1 = pic2.getPixelRed(i//2 + w//4, j//2 + h//4)
            g1 = pic2.getPixelGreen(i//2 + w//4, j//2 + h//4)
            b1 = pic2.getPixelBlue(i//2 + w//4, j//2 + h//4)
            pic1.setPixelColor(i, j, r1, g1, b1)
            pic1.setPixelColor(i + 1, j, r1, g1, b1)
            pic1.setPixelColor(i, j + 1, r1, g1, b1)
            pic1.setPixelColor(i + 1, j + 1, r1, g1, b1)
    pic1.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
 
def posterize(pic,w,h):
    for i in range(0,w-1):
        for j in range(0,h-1):
            r1 = pic.getPixelRed(i,j)
            g1 = pic.getPixelGreen(i,j)
            b1 = pic.getPixelBlue(i,j)
            pic.setPixelColor(i, j, (r1+16)//32*32, (g1+16)//32*32, (b1+16)//32*32)                
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
    
def brightness(pic,w,h):
    change = raw_input("How much do you want to change the brightness by?: ")
    for i in range(0,w-1):
        for j in range(0,h-1):
            r1 = pic.getPixelRed(i,j)
            g1 = pic.getPixelGreen(i,j)
            b1 = pic.getPixelBlue(i,j)
            r2 = r1 + int(change)
            g2 = g1 + int(change)
            b2 = b1 + int(change)
            if r1+int(change) > 255:
                r2=255
            if r1+int(change) < 0:
                r2=0
            if g1+int(change) > 255:
                g2=255
            if g1+int(change) < 0:
                g2=0
            if b1+int(change) > 255:
                b2=255
            if b1+int(change) < 0:
                b2=0    
            pic.setPixelColor(i, j, r2, g2, b2)                
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
    
def increasecontrast(pic,w,h):
    for i in range(0,w-1):
        for j in range(0,h-1):
            r = pic.getPixelRed(i,j)
            g = pic.getPixelGreen(i,j)
            b = pic.getPixelBlue(i,j)
            if r > 128:
                r = r + (r - 128)
            if r < 128:
                r = r + (r - 128)
            if g > 128:
                g = g + (g - 128)
            if g < 128:
                g = g + (g - 128) 
            if b > 128:
                b = b + (b - 128)
            if b < 128:
                b = b + (g - 128)
            if r > 255:
                r = 255
            if r < 0:
                r = 0
            if g > 255:
                g = 255
            if g < 0:
                g = 0
            if b > 255:
                b = 255
            if b < 0:
                b = 0    
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    



def blur(pic1,pic2,w,h):
    r1 = 0
    g1 = 0
    b1 = 0
    for i in range(0, w - 1):
        for j in range(0, h - 1):
            if i == 0 and j != 0 and j != h-1:
                for x in range(i,i+2):
                    for y in range(j-1,j+2):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                        pic1.setPixelColor(x, y, (r1//6), (g1//6), (b1//6))
            elif i == 0 and j == 0:
                for x in range(i,i+2):
                    for y in range(j,j+2):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                        pic1.setPixelColor(x, y, (r1//4), (g1//4), (b1//4))
            elif i == 0 and j == h - 1:
                for x in range(i,i+2):
                    for y in range(j-1,j+1):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                        pic1.setPixelColor(x, y, (r1//4), (g1//4), (b1//4))
            elif i == w - 1 and j != 0 and j != h-1:
                for x in range(i-1,i+1):
                    for y in range(j-1,j+2):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                        pic1.setPixelColor(x, y, (r1//6), (g1//6), (b1//6))
            elif i == w - 1 and j == 0:
                for x in range(i-1,i+1):
                    for y in range(j,j+2):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                        pic1.setPixelColor(x, y, (r1//4), (g1//4), (b1//4))
            elif i == w - 1 and j == h-1:
                for x in range(i-1,i+1):
                    for y in range(j-1,j+1):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                        pic1.setPixelColor(x, y, (r1//4), (g1//4), (b1//4))
            else:            
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        r1 = r1 + pic2.getPixelRed(x, y)
                        g1 = g1 + pic2.getPixelGreen(x, y)
                        b1 = b1 + pic2.getPixelBlue(x, y)
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        pic1.setPixelColor(x, y, (r1//9), (g1//9), (b1//9))
                    
    pic1.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2



def rotate180(pic,w,h):
    for i in range(0, (w)//2):
        for j in range(0, h):
            r1 = pic.getPixelRed(w-1-i,j)
            g1 = pic.getPixelGreen(w-1-i,j)
            b1 = pic.getPixelBlue(w-1-i,j)
            r2 = pic.getPixelRed(i,h-1-j)
            g2 = pic.getPixelGreen(i,h-1-j)
            b2 = pic.getPixelBlue(i,h-1-j)
            pic.setPixelColor(i, h-1-j, r1, g1, b1)
            pic.setPixelColor((w-1-i),j, r2, g2, b2)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
def collide(pic,w,h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r = pic.getPixelRed(w-1-i,j)
            g = pic.getPixelGreen(w-1-i,j)
            b = pic.getPixelBlue(w-1-i,j)
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2
    
def shadowize(pic1,pic2,w,h):    
    for i in range(1, w, 3):
            for j in range(1, h, 3):
                for a in range(i-1,i+2):
                    for b in range(j-1,j+2):
                        r1 = pic2.getPixelRed(a//3 + w//3, b//3 + h//3)
                        g1 = pic2.getPixelGreen(a//3 + w//3, b//3 + h//3)
                        b1 = pic2.getPixelBlue(a//3 + w//3, b//3 + h//3)
                        pic1.setPixelColor(i, j, r1, g1, b1)
                        pic1.setPixelColor(i + 1, j, r1, g1, b1)
                        pic1.setPixelColor(i, j + 1, r1, g1, b1)
                        pic1.setPixelColor(i + 1, j + 1, r1, g1, b1)
    pic1.display()
    cont = eval(raw_input("Would you like to continue manipulating this image? "))
    return cont
    return pic
    return pic1
    return pic2

def command(pic,pic1,pic2,w,h):
    cmd = eval(raw_input("What would you like to do with this image? "))
    if cmd == "flip":
        fliphorizontal(pic,w,h)
    elif cmd == "mirror":
        mirrorhorizontal(pic,w,h)
    elif cmd == "scroll":
        scrollhorizontal(pic1,pic2,w,h)
    elif cmd == "negative":
        negative(pic,w,h)
    elif cmd == "grayscale":
        grayscale(pic,w,h)
    elif cmd == "cycle color":
        cyclecolor(pic1,pic2,w,h)
    elif cmd == "zoom":
        zoom(pic1,pic2,w,h)
    elif cmd == "posterize":
        posterize(pic,w,h)
    elif cmd == "change brightness":
        brightness(pic,w,h)
    elif cmd == "increase the contrast":
        increasecontrast(pic,w,h)
    elif cmd == "rotate 180 degrees":
        rotate180(pic,w,h)
    elif cmd == "collide":
        collide(pic,w,h)
    elif cmd == "shadowize":
        shadowize(pic1,pic2,w,h)
    else:
        print"I think you entered something wrong, try again."

def main():
    print "Welcome to my Image Editor!"
    pic = picture2.Picture("crayons.bmp")
    pic.display()
    print"Please choose from the following options and put your response in quotes:"
    print"flip"
    print"mirror"
    print"scoll"
    print"negative"
    print"grayscale"
    print"cycle color"
    print"zoom"
    print"posterize"
    print"change brightness"
    print"increase the contrast"
    print"rotate 180 degrees"
    print"collide"
    print"shadowize"
    w = pic.getWidth()
    h = pic.getHeight()
    pic1 = createcopy(pic,w,h)
    pic2 = createcopy(pic,w,h)
    cont = "yes"
    while cont == "yes" or cont == "Yes":
            command(pic,pic1,pic2,w,h)
        
    
main()
