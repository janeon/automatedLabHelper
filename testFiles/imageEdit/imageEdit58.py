





import picture2
def PostNumber(x):
    y = x%32
    fin = x-y
    return fin

def Cycles(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    Cycle = picture2.Picture(w,h)
    for x in range(0, w):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y)
            green = canvas.getPixelGreen(x,y)
            blue = canvas.getPixelBlue(x, y)
            Cycle.setPixelRed(x,y,blue)
            Cycle.setPixelBlue(x,y,green)
            Cycle.setPixelGreen(x,y,red)
    Cycle.setTitle("Cycle Colors")
    input()
    
def Negatize(canvas):
    invert = 255
    w = canvas.getWidth()
    h = canvas.getHeight()
    Negative = picture2.Picture(w,h)
    for x in range(0, w):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y)
            green = canvas.getPixelGreen(x,y)
            blue = canvas.getPixelBlue(x, y)
            Negative.setPixelRed(x,y,(invert-red))
            Negative.setPixelBlue(x,y,(invert-blue))
            Negative.setPixelGreen(x,y,invert-green)
    Negative.setTitle("NEGATIZE THE RAINBOW")
    input()
    
def Flip(canvas):
    invert = 255
    w = canvas.getWidth()
    h = canvas.getHeight()
    Flips = picture2.Picture(w,h)
    for x in range(0, w):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y)
            green = canvas.getPixelGreen(x,y)
            blue = canvas.getPixelBlue(x, y)
            Flips.setPixelRed((w-x-1),y,(red))
            Flips.setPixelBlue((w-x-1),y,(blue))
            Flips.setPixelGreen((w-x-1),y,green)
    Flips.setTitle("Flippty Split!")
    Flips.display()
    input()
    
def Blur(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(1, w):
        for y in range(1, h):
            gone = canvas.getPixelGreen(x, y)
            gtwo = canvas.getPixelGreen(x-1, y)
            gthree = canvas.getPixelGreen(x+1, y)
            gfour = canvas.getPixelGreen(x, y-1) 
            gfive = canvas.getPixelGreen(x, y+1) 
            gsix = canvas.getPixelGreen(x+1, y+1) 
            gseven = canvas.getPixelGreen(x-1, y-1) 
            geight = canvas.getPixelGreen(x+1, y-1) 
            gnine = canvas.getPixelGreen(x-1, y+1) 
            g = (gone+gtwo+gthree+gfour+gfive+gsix+gseven+geight+gnine)/9 
            bone = canvas.getPixelBlue(x, y) 
            btwo = canvas.getPixelBlue(x-1, y) 
            bthree = canvas.getPixelBlue(x+1, y) 
            bfour = canvas.getPixelBlue(x, y-1) 
            bfive = canvas.getPixelBlue(x, y+1) 
            bsix = canvas.getPixelBlue(x+1, y+1) 
            bseven = canvas.getPixelBlue(x-1, y-1) 
            beight = canvas.getPixelBlue(x+1, y-1) 
            bnine = canvas.getPixelBlue(x-1, y+1) 
            b = (bone+btwo+bthree+bfour+bfive+bsix+bseven+beight+bnine)/9 
            rone = canvas.getPixelRed(x, y) 
            rtwo = canvas.getPixelRed(x-1, y) 
            rthree = canvas.getPixelRed(x+1, y) 
            rfour = canvas.getPixelRed(x, y-1) 
            rfive = canvas.getPixelRed(x, y+1) 
            rsix = canvas.getPixelRed(x+1, y+1) 
            rseven = canvas.getPixelRed(x-1, y-1) 
            reight = canvas.getPixelRed(x+1, y-1) 
            rnine = canvas.getPixelRed(x-1, y+1) 
            r = (rone+rtwo+rthree+rfour+rfive+rsix+rseven+reight+rnine)/9 
            if(x < 1):
                r = rone 
                g = gone 
                b = bone 
            if(x > (w-2)):
                r = rone 
                g = gone 
                b = bone 
            if(y < 1):
                r = rone 
                g = gone 
                b = bone 
            if(y > (h - 2)):
                r = rone 
                g = gone 
                b = bone 
            if(r < 0):
                r = 0 
            if(r > 255):
                r = 255
            if(g < 0):
                g = 0
            if(g > 255):
                g = 255 
            if(b < 0):
                b = 0 
            if(b > 255):
                b = 255 
            pic.setPixelColor(x, y, r, g, b) 
    pic.setTitle("Blur") 
    pic.display()
    input()

def MakeGrayscale(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(0, w):
        for y in range(0, h):
            r = canvas.getPixelRed(x, y) 
            g = canvas.getPixelGreen(x, y) 
            b = canvas.getPixelBlue(x, y) 
            gray = .299*r + .587*g + .114*b 
            grey = int(gray) 
            pic.setPixelColor(x, y, grey, grey, grey) 
    pic.setTitle("Grayscale") 
    pic.display()
    input()

def Mirror(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    Mirrors = picture2.Picture(w,h)
    for x in range(0, w/2):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y) 
            green = canvas.getPixelGreen(x,y) 
            blue = canvas.getPixelBlue(x, y) 
            Mirrors.setPixelRed(x,y,red) 
            Mirrors.setPixelBlue(x,y,blue) 
            Mirrors.setPixelGreen(x,y,green)
    for x in range(w/2, 0):
        for y in range(0, h):
            red = canvas.getPixelRed(w-x,y) 
            green = canvas.getPixelGreen(w-x,y) 
            blue = canvas.getPixelBlue(w-x, y) 
            Mirrors.setPixelRed(x,y,red) 
            Mirrors.setPixelBlue(x,y,blue) 
            Mirrors.setPixelGreen(x,y,green) 
    Mirrors.setTitle("Mirrored") 
    Mirrors.display()
    input()
    
def Rotate(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    degree = input("How much would you like to rotate the image?")
    Rot = picture2.Picture(w, h)
    for x in range(0, w):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y) 
            green = canvas.getPixelGreen(x,y) 
            blue = canvas.getPixelBlue(x, y) 
            Rot.setPixelRed(x,y,blue) 
            Rot.setPixelBlue(x,y,green) 
            Rot.setPixelGreen(x,y,red) 
    Rot.setTitle("Rotate the Picture") 
    Rot.display()
    input()

def Scroll(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    print("You have a width of "+w+" and a height of "+h) 
    pixel = input("How much would you like to scroll the image?") 
    scroll = picture2.Picture(w, h)
    newX = 0 
    PIXEL = w-pixel 
    for x in range(pixel, w):
        for y in range(0, h):
            red = canvas.getPixelRed(newX,y) 
            green = canvas.getPixelGreen(newX,y) 
            blue = canvas.getPixelBlue(newX, y) 
            scroll.setPixelRed(x,y,red) 
            scroll.setPixelBlue(x,y,blue) 
            scroll.setPixelGreen(x,y,green)  
            scroll.setTitle("Elder Scrolled") 
        newX=newX+1
    for x in range(pixel):
        for y in range(0, h):
            red = canvas.getPixelRed(PIXEL,y) 
            green = canvas.getPixelGreen( PIXEL,y) 
            blue = canvas.getPixelBlue(PIXEL, y) 
            scroll.setPixelRed(x,y,red) 
            scroll.setPixelBlue(x,y,blue) 
            scroll.setPixelGreen(x,y,green)  
            scroll.setTitle("Elder Scrolled") 
            PIXEL = PIXEL+1 
    scroll.display()
    input()

def Posterize(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    post = picture2.Picture(w, h)
    for x in range(0, w):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y) 
            green = canvas.getPixelGreen(x,y) 
            blue = canvas.getPixelBlue(x, y) 
            post.setPixelRed(x,y,PostNumber(red)) 
            post.setPixelBlue(x,y,PostNumber(blue)) 
            post.setPixelGreen(x,y,PostNumber(green)) 
    post.setTitle("What even is Posterization...?") 
    post.display()
    input()

def Graphic(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    graphic = picture2.Picture(w, h)
    for z in range(0, 151):
        for x in range(0, w):
            for y in range(0, y):
                red = canvas.getPixelRed(x,y) 
                green = canvas.getPixelGreen(x,y) 
                blue = canvas.getPixelBlue(x, y) 
                graphic.setPixelRed(x,y,red) 
                graphic.setPixelBlue(x,y,blue) 
                graphic.setPixelGreen(x,y,green) 
                graphic.setTitle("Draw it for me!") 
                graphic.display()
                                
def Zoom(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    zoom = picture2.Picture(w, h)
    for x in range(0, w):
        for y in range(0, h):
            red = canvas.getPixelRed(x,y) 
            green = canvas.getPixelGreen(x,y) 
            blue = canvas.getPixelBlue(x, y) 
            zoom.setPixelRed(x,y,red) 
            zoom.setPixelBlue(x,y,blue) 
            zoom.setPixelGreen(x,y,green) 
            zoom.setTitle("Zoom Zoom Zoom!") 
    zoom.display()
    input()

def PossibleOperations():
    print("1. Cycle Color Channels" ) 
    print("2. Make Negative" ) 
    print("3. Make Grayscale") 
    print("4. Increase Contrast") 
    print("5. Flip Horizontally") 
    print("6. Blur") 
    print("7. Scroll") 
    print("8. Mirror") 
    print("9. Renewing") 
    print("10. Posterize") 
    print("11. Rotate") 
    print("12. Zoom")
    print("13. Exit")

def IncreaseContrast(canvas):
    w = canvas.getWidth() 
    h = canvas.getHeight() 
    pic = picture2.Picture(w, h)
    for x in range(0, w):
        for y in range(0, h):
            r = canvas.getPixelRed(x, y) 
            g = canvas.getPixelGreen(x, y) 
            b = canvas.getPixelBlue(x, y) 
            if(r == 128):
                r = r 
            else:
                r = r-128 
                r = 2*r 
                r = 128 +r 
            if(g == 128):
                g = g 
            else:
                g = g - 128 
                g = 2*g 
                g = 128 + g 
            if (b == 128):
                b = b 
            else:
                b = b - 128 
                b = 2*b 
                b = 128 + b 
            if (r < 0):
                r = 0 
            if (r > 255):
                r = 255 
            if (g < 0):
                g = 0 
            if (g > 255):
                g = 255 
            if (b < 0):
                b = 0 
            if (b > 255):
                b = 255 
            pic.setPixelColor(x, y, r, g, b) 
    pic.setTitle("Increase Contrast") 
    pic.display()
    input()

def main():
    pic = raw_input("picture file?")
    canvas = picture2.Picture("crayons.bmp")
    canvas.display()
    input()
    done = False 
    while (not done):
        print("What would you like to do to the image?") 
        PossibleOperations() 
        print("Your choice?") 
        choice = input("your choice") 
        if (choice == 1):
            Cycles(canvas) 
        if (choice == 2):
             Negatize(canvas) 
        if (choice == 3):
             MakeGrayscale(canvas) 
        if (choice == 4):
            IncreaseContrast(canvas) 
        if (choice == 5):
            Flip(canvas) 
        if (choice == 6):
            Blur(canvas) 
        if (choice == 7):
            Scroll(canvas) 	
        if (choice == 8 ):
            Mirror(canvas) 
        if (choice == 9 ):
            Graphics(canvas) 
        if (choice == 10 ):
            Posterize(canvas) 
        if (choice == 11 ):
            Rotate(canvas) 
        if (choice == 12 ):
            Zoom(canvas)
        if (choice == 13):
            done = True
        if (choice > 13):
            print( "Pick again.")
main()