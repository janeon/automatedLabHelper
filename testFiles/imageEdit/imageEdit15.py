





import picture2

def main():
    pic = picture2.Picture("crayons.bmp")
    print "You are so lucky that you stumbled upon this image editing program. Yeah"
    print "You can choose from flip, mirror, scroll, negative, grayscale,"
    print "cycle color channels, zoom, posterize, brightness, contrast, blur, "
    print "rotate 180 degrees, mirror2, and trippy."
    x = "yes"
    try:
        while x != "no":
            n = raw_input("What effect would you like? ")
            if n == "flip":
                flip(pic)
            if n == "mirror":
                mirror(pic)
            if n == "scroll":
                scroll(pic)
            if n == "negative":
                negative(pic)
            if n == "grayscale":
                grayscale(pic)
            if n == "cycle color channels":
                colorcycle(pic)
            if n == "zoom":
                zoom(pic)
            if n == "posterize":
                posterize(pic)
            if n == "brightness":
                brightness(pic)
            if n == "contrast":
                contrast(pic)
            if n == "blur":
                blur(pic)
            if n == "rotate 180 degrees":
                turn180(pic)
            if n == "mirror2":
                mirror2(pic)
            if n == "trippy":
                trippy(pic)
            x = raw_input("Do you want to add another effect? (yes or no) ")
        pic.display()
        input()
    except SyntaxError:
        print"Toodles!"
    
def grayscale(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            v = (r+g+b)/3
            pic.setPixelColor(x,y,v,v,v)
    return pic

def negatives(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pic.setPixelColor(x,y,r,g,b)
    return pic

def posterize(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            r2 = r//32
            r = r2*32
            g2 = g//32
            g = g2*32
            b2 = b//32
            b = b2*32
            pic.setPixelColor(x,y,r,g,b)
    return pic

def trippy(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = picture2.Picture(w,h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            x = w-1-x
            if x < 0:
                x = x * -1
            r = pic.getPixelRed(w-1-x,y)
            g = pic.getPixelGreen(w-1-x,y)
            b = pic.getPixelBlue(w-1-x,y)
            pic.setPixelColor(x,y,r,g,b)
    return pic

def contrast(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            rr = 128 - r
            r = 128 - (2 * rr)
            gg = 128 - g
            g = 128 - (2 * gg)
            bb = 128 - b
            b = 128 - (2 * bb)
            pic.setPixelColor(x,y,r,g,b)
    return pic

def brightness(pic):
    n = eval(raw_input("Enter an integer for the amount of change in brightness: "))
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            r = r + n
            if r > 255:
                r = 255
            if r < 0:
                r = 0
            g = g + n
            if g > 255:
                g = 255
            if g < 0:
                g = 0
            b = b + n
            if b > 255:
                b = 255
            if b < 0:
                b = 0
            pic.setPixelColor(x,y,r,g,b)
    return pic

def mirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(w/2,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(w-1-x,y)
            g = pic.getPixelGreen(w-1-x,y)
            b = pic.getPixelBlue(w-1-x,y)
            pic.setPixelColor(x,y,r,g,b)
    return pic

def mirror2(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            if x > (w/2):
                r = pic.getPixelRed(w-1-x,y)
                g = pic.getPixelGreen(w-1-x,y)
                b = pic.getPixelBlue(w-1-x,y)
                pic.setPixelColor(x,y,r,g,b)
            else:
                r = pic.getPixelRed((w/2)-x,y)
                g = pic.getPixelGreen((w/2)-x,y)
                b = pic.getPixelBlue((w/2)-x,y)
                pic.setPixelColor(x,y,r,g,b)
    return pic

def flip(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,(w-1)/2):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            r2 = pic.getPixelRed(w-1-x,y)
            g2 = pic.getPixelGreen(w-1-x,y)
            b2 = pic.getPixelBlue(w-1-x,y)
            pic.setPixelColor(w-1-x,y,r,g,b)
            pic.setPixelColor(x,y,r2,g2,b2)
    return pic

def turn180(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w/2):
        for y in range(0,h):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            r2 = pic.getPixelRed(w-1-x,h-1-y)
            g2 = pic.getPixelGreen(w-1-x,h-1-y)
            b2 = pic.getPixelBlue(w-1-x,h-1-y)
            pic.setPixelColor(w-1-x,h-1-y,r,g,b)
            pic.setPixelColor(x,y,r2,g2,b2)
    return pic

def blur(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = picture2.Picture("crayons.bmp")
    for x in range(1,w-2):
        for y in range(1,h-2):
            a = x+1
            k = x-1
            c = y+1
            d = y-1
            
            r = pic2.getPixelRed(x,y)
            rr = pic2.getPixelRed(a,y)
            Rr = pic2.getPixelRed(k,y)
            rR = pic2.getPixelRed(x,c)
            RR = pic2.getPixelRed(x,d)
            rrr = pic2.getPixelRed(a,c)
            Rrr = pic2.getPixelRed(k,c)
            RRr = pic2.getPixelRed(k,d)
            RRR = pic2.getPixelRed(a,d)
            
            g = pic2.getPixelGreen(x,y)
            gg = pic2.getPixelGreen(a,y)
            Gg = pic2.getPixelGreen(k,y)
            gG = pic2.getPixelGreen(x,c)
            GG = pic2.getPixelGreen(x,d)
            ggg = pic2.getPixelGreen(a,c)
            Ggg = pic2.getPixelGreen(k,c)
            GGg = pic2.getPixelGreen(k,d)
            GGG = pic2.getPixelGreen(a,d)
            
            b = pic2.getPixelBlue(x,y)
            bb = pic2.getPixelBlue(a,y)
            Bb = pic2.getPixelBlue(k,y)
            bB = pic2.getPixelBlue(x,c)
            BB = pic2.getPixelBlue(x,d)
            bbb = pic2.getPixelBlue(a,c)
            Bbb = pic2.getPixelBlue(k,c)
            BBb = pic2.getPixelBlue(k,d)
            BBB = pic2.getPixelBlue(a,d)
            
            r = (r+rr+Rr+rR+RR+rrr+Rrr+RRr+RRR)/9
            g = (g+gg+Gg+gG+GG+ggg+Ggg+GGg+GGG)/9
            b = (b+bb+Bb+bB+BB+bbb+Bbb+BBb+BBB)/9
            
            
            
            
            
            
            
            
            
            
            pic.setPixelColor(x,y,r,g,b)
    return pic

def colorcycle(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic.getPixelRed(x,y)
            g = pic.getPixelGreen(x,y)
            b = pic.getPixelBlue(x,y)
            r2 = b
            g2 = r
            b2 = g
            pic.setPixelColor(x,y,r2,g2,b2)
    return pic

def scroll(pic):
    d = eval(raw_input("Enter an integer for the amount of pixels you want scrolling to the right: "))
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = picture2.Picture("crayons.bmp")
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = pic2.getPixelRed((x+d)%(w),y)
            g = pic2.getPixelGreen((x+d)%(w),y)
            b = pic2.getPixelBlue((x+d)%(w),y)
            
            pic.setPixelColor(x,y,r,g,b)
    return pic

def zoom(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = picture2.Picture("crayons.bmp")
    for x in range(0,w-1):
        for y in range(0,h-1):
            if x%2 == 0 and y%2 ==0:
                r = pic2.getPixelRed(w/4-1+x/2,h/4-1+y/2)
                g = pic2.getPixelGreen(w/4-1+x/2,h/4-1+y/2)
                b = pic2.getPixelBlue(w/4-1+x/2,h/4-1+y/2)
            if x%2 == 1 and y%2 == 0:
                r = pic2.getPixelRed(w/4-1+(x-1)/2,h/4-1+y/2)
                g = pic2.getPixelGreen(w/4-1+(x-1)/2,h/4-1+y/2)
                b = pic2.getPixelBlue(w/4-1+(x-1)/2,h/4-1+y/2)
            if x%2 == 0 and y%2 == 1:
                r = pic2.getPixelRed(w/4-1+x/2,h/4-1+(y-1)/2)
                g = pic2.getPixelGreen(w/4-1+x/2,h/4-1+(y-1)/2)
                b = pic2.getPixelBlue(w/4-1+x/2,h/4-1+(y-1)/2)
            if x%2 ==1 and y%2 ==1:
                r = pic2.getPixelRed(w/4-1+(x-1)/2,h/4-1+(y-1)/2)
                g = pic2.getPixelGreen(w/4-1+(x-1)/2,h/4-1+(y-1)/2)
                b = pic2.getPixelBlue(w/4-1+(x-1)/2,h/4-1+(y-1)/2)
            pic.setPixelColor(x,y,r,g,b)
    return pic

main()
    
    

