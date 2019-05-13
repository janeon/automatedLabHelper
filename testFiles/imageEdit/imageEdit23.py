





import picture2

def imageEditor ():
    print ""
    print "Welcome to the Image Manipulator, where we turn your lame pictures into high art."
    fileName = raw_input("Please enter the image file you'd like loaded: ")
    pic = picture2.Picture(fileName)
    h = pic.getHeight()
    w = pic.getWidth()
    print "Uploaded image of", h, "by", w, "pixels."
    pic.display()
    
    application = raw_input ("What would you like to apply to the image? Select: negate, grayscale, cycle colors, posterize, scroll, flip, blur, seizure, zoom, playing card, rotate 180 or mirror: ")
    
    if application == ("negate"):
        for r in range (0, h):
            for c in range (0, w):
                redvalue = pic.getPixelRed(c,r)
                pic.setPixelRed(c,r,(255-redvalue))
                greenvalue = pic.getPixelGreen(c,r)
                pic.setPixelGreen(c,r,(255-greenvalue))
                bluevalue = pic.getPixelBlue(c,r)
                pic.setPixelBlue(c,r,(255-bluevalue))
        pic.display()
        input()

    if application == ("grayscale"):
        for r in range (0, h):
                for c in range (0, w):
                    redvalue = pic.getPixelRed(c,r)
                    greenvalue = pic.getPixelGreen(c,r)
                    bluevalue = pic.getPixelBlue(c,r)
                    a = ((redvalue+greenvalue+bluevalue)/3)
                    pic.setPixelRed(c,r,a)
                    pic.setPixelGreen(c,r,a)
                    pic.setPixelBlue(c,r,a)
        pic.display()
        input()
        
    if application == ("cycle colors"):
        for r in range (0, h):
                for c in range (0, w):
                    redvalue = pic.getPixelRed(c,r)
                    greenvalue = pic.getPixelGreen(c,r)
                    bluevalue = pic.getPixelBlue(c,r)
                    pic.setPixelRed(c,r,bluevalue)
                    pic.setPixelGreen(c,r,redvalue)
                    pic.setPixelBlue(c,r,greenvalue)
        pic.display()
        input()
        
    if application == ("posterize"):
        for r in range (0, h):
                for c in range (0, w):
                    redvalue = pic.getPixelRed(c,r)
                    greenvalue = pic.getPixelGreen(c,r)
                    bluevalue = pic.getPixelBlue(c,r)
                    pic.setPixelRed(c,r,myround(redvalue))
                    pic.setPixelGreen(c,r,myround(greenvalue))
                    pic.setPixelBlue(c,r,myround(bluevalue))
        pic.display()
        input()
        
    if application == ("scroll"):
        w, h = bodyType(pic)
        piccopy = copy(pic)
        d = eval(raw_input("How far would you like to scroll? "))
        for j in range (0, h):
            for i in range (0, w):
                red, green, blue = piccopy.getPixelColor(i,j)
                pic.setPixelColor((i+d)%w, j, red, green, blue)
        pic.display()
        input()
        
    if application == ("flip"):
        w,h = bodyType(pic)
        temp = copy(pic)
        for i in range(w):
            for j in range(h):
                R,G,B = temp.getPixelColor(i,j)
                pic.setPixelColor(w-i-1,j,R,G,B)
        pic.display()
        input()
        
    if application == ("blur"):
        print "Blurring image-- this effect may take a few seconds."
        w,h = bodyType(pic)
        for i in range(1,w-2):
            for j in range(1,h-2):
                x,y,z = getRounded(pic,i,j)
                pic.setPixelColor(i,j,x,y,z)
        pic.display()
        input()

    if application == ("seizure"):
        w,h = bodyType(pic)
        for r in range (0, h):
            for c in range (0, w):
                redvalue = pic.getPixelRed(c,r)
                pic.setPixelRed(c,r,(255-redvalue))
                greenvalue = pic.getPixelGreen(c,r)
                pic.setPixelGreen(c,r,(255-greenvalue))
                bluevalue = pic.getPixelBlue(c,r)
                pic.setPixelBlue(c,r,(255-bluevalue))
        for i in range (0, h):
                for p in range (0, w):
                    redvalue = pic.getPixelRed(p,i)
                    greenvalue = pic.getPixelGreen(p,i)
                    bluevalue = pic.getPixelBlue(p,i)
                    pic.setPixelRed(p,i,bluevalue)
                    pic.setPixelGreen(p,i,redvalue)
                    pic.setPixelBlue(p,i,greenvalue)
        pic.display()
        input()
        
    if application == ("zoom"): 
        w,h = bodyType(pic)
        temp = picture2.Picture(w,h)
        for i in range(w/4, (3*w/4)):
            for j in range(h/4, (3*h/4)):
                R,G,B = temp.getPixelColor(i,j)
                for x in range(0,(w-1),2):
                    for y in range(0,(h-1),2):
                        for k in range(2):
                            for l in range(2):
                                pic.setPixelColor(i+k,j+l,R,G,B)
        pic.display()
        input()
        
    if application == ("playing card"):
        width, height = bodyType(pic)
        temp = picture2.Picture(width,height)
        for i in range(width//2):
            for j in range(height):
                R,G,B = pic.getPixelColor(i,j)
                pic.setPixelColor(width-i-1,height-j-1,R,G,B)
        for r in range (0, h):
                for c in range (0, w):
                    redvalue = pic.getPixelRed(c,r)
                    greenvalue = pic.getPixelGreen(c,r)
                    bluevalue = pic.getPixelBlue(c,r)
                    a = ((redvalue+greenvalue+bluevalue)/2)
                    pic.setPixelRed(c,r,a)
                    pic.setPixelGreen(c,r,a)
                    pic.setPixelBlue(c,r,a)
        pic.display()
        input()
        
    if application == ("rotate 180"):
        width, height = bodyType(pic)
        piccopy = copy(pic)
        for i in range(width):
            for j in range(height):
                R,G,B = piccopy.getPixelColor(i,j)
                pic.setPixelColor(width-i-1,height-j-1,R,G,B)
        pic.display()
        input()
        
    if application == ("mirror"):
            width, height = bodyType(pic)
            temp = picture2.Picture(width,height)
            for i in range(width//2):
                for j in range(height-1):
                    R,G,B = pic.getPixelColor(i,j)
                    pic.setPixelColor(width-i-1,j,R,G,B)
            pic.display()
            input()
    

def bodyType(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    return w, h

def myround(x, base=32): 
    return int(base * round(float(x)/base))

def copy(pic): 
    width,height = bodyType(pic)
    temp = picture2.Picture(width,height)
    for i in range(width):
        for j in range(height):
            R,G,B = pic.getPixelColor(i,j)
            temp.setPixelColor(i,j,R,G,B)
    return temp

def getRounded(pix,x,y): 
    temp = copy(pix)
    red = []
    green = []
    blue = []
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            R,G,B = temp.getPixelColor(i+x,j+y)
            red.append(R)
            green.append(G)
            blue.append(B)
    for item in red:
        a = 0
        a = a + item
    for item in green:
        p = 0
        p = p + item
    for item in blue:
        z = 0
        z = z + item
    a = a//9
    p = p//9
    z = z//9
    return a,p,z


    input()

imageEditor()
