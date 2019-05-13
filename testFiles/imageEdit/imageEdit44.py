







import picture2


def flip(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    canvas.close()
    for x in range(0, w-1):
        for y in range(0, h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            f = w - x - 1
            pic.setPixelRed(f,y,r)
            pic.setPixelGreen(f,y,g)
            pic.setPixelBlue(f,y,b)
    return pic


def mirror(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(0, w-1):
        for y in range(0,h-1):
            if x <= w//2:
                r = canvas.getPixelRed(x,y)
                g = canvas.getPixelGreen(x,y)
                b = canvas.getPixelBlue(x,y)
            if x > w//2:
                r = canvas.getPixelRed(w-x,y)
                g = canvas.getPixelGreen(w-x,y)
                b = canvas.getPixelBlue(w-x,y)
            pic.setPixelRed(x,y,r)
            pic.setPixelGreen(x,y,g)
            pic.setPixelBlue(x,y,b)
    return pic


def scroll(canvas,d):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            s = x + d
            if s >= w:
                s = s - w
            pic.setPixelRed(s,y,r)
            pic.setPixelGreen(s,y,g)
            pic.setPixelBlue(s,y,b)
    return pic


def negative(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            pic.setPixelRed(x,y,255-r)
            pic.setPixelGreen(x,y,255-g)
            pic.setPixelBlue(x,y,255-b)
    return pic


def grayscale(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(0,w - 1):
        for y in range(0,h - 1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            p = (r+g+b) / 3
            p = int(p)
            pic.setPixelRed(x,y,p)
            pic.setPixelGreen(x,y,p)
            pic.setPixelBlue(x,y,p)
    return pic


def cycle(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            pic.setPixelRed(x,y,b)
            pic.setPixelGreen(x,y,r)
            pic.setPixelBlue(x,y,g)
    return pic


def zoom(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    xbegin = w//4
    ybegin = h//4
    xend = w//2
    yend = h//2
    for x in range(0,xend-1):
        for y in range(0,yend-1):
            r = canvas.getPixelRed(x + xbegin,y + ybegin)
            g = canvas.getPixelGreen(x + xbegin, y + ybegin)
            b = canvas.getPixelBlue(x + xbegin,y + ybegin)
            x2 = x*2
            y2 = y*2
            pic.setPixelRed(x2,y2,r)
            pic.setPixelGreen(x2,y2,g)
            pic.setPixelBlue(x2,y2,b)
            pic.setPixelRed(x2+1,y2,r)
            pic.setPixelGreen(x2+1,y2,g)
            pic.setPixelBlue(x2+1,y2,b)
            pic.setPixelRed(x2,y2+1,r)
            pic.setPixelGreen(x2,y2+1,g)
            pic.setPixelBlue(x2,y2+1,b)
            pic.setPixelRed(x2+1,y2+1,r)
            pic.setPixelGreen(x2+1,y2+1,g)
            pic.setPixelBlue(x2+1,y2+1,b)
    return pic


def posterize(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            pic.setPixelRed(x,y,(r//32)*32)
            pic.setPixelGreen(x,y,(g//32)*32)
            pic.setPixelBlue(x,y,(b//32)*32)
    return pic


def brightness(canvas, d):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w, h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            r = r + d
            if r > 255:
                r = 255
            g = g + d
            if g > 255:
                g = 255
            b = b + d
            if b > 255:
                b = 255
            pic.setPixelRed(x,y,r+d)
            pic.setPixelGreen(x,y,g+d)
            pic.setPixelBlue(x,y,b+d)
    return pic


def contrast(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range(0, w-1):
        for y in range(0,h-1):
            r = newcontrast(canvas.getPixelRed(x,y))
            g = newcontrast(canvas.getPixelGreen(x,y))
            b = newcontrast(canvas.getPixelBlue(x,y))
            pic.setPixelColor(x,y,r,g,b)
    return pic
            
def newcontrast(n):
    if n==128:
        return n
    x = n - 128
    x = x*2
    n = n + x
    if n < 0:
        return 0
    if n > 255:
        return 255
    return n


def blur(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range (0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            m = 0
            if x == 0:
                r+= canvas.getPixelRed(x+1,y)
                g+= canvas.getPixelGreen(x+1,y)
                b+= canvas.getPixelBlue(x+1,y)
                m = m + 1
                if y != 0:
                    r+= canvas.getPixelRed(x+1,y-1)
                    g+= canvas.getPixelGreen(x+1,y-1)
                    b+= canvas.getPixelBlue(x+1,y-1)
                    m = m + 1
                    r+= canvas.getPixelRed(x,y-1)
                    g+= canvas.getPixelGreen(x,y-1)
                    b+= canvas.getPixelBlue(x,y-1)
                    m = m + 1
                if y != h-1:
                    r+= canvas.getPixelRed(x+1,y+1)
                    g+= canvas.getPixelGreen(x+1,y+1)
                    b+= canvas.getPixelBlue(x+1,y+1)
                    m = m + 1
                    r+= canvas.getPixelRed(x,y+1)
                    g+= canvas.getPixelGreen(x,y+1)
                    b+= canvas.getPixelBlue(x,y+1)
                    m = m + 1
            elif x == w - 1:
                r+= canvas.getPixelRed(x-1,y)
                g+= canvas.getPixelGreen(x-1,y)
                b+= canvas.getPixelBlue(x-1,y)
                m = m + 1
                if y != 0:
                    r+= canvas.getPixelRed(x-1,y-1)
                    g+= canvas.getPixelGreen(x-1,y-1)
                    b+= canvas.getPixelBlue(x-1,y-1)
                    m = m + 1
                    r+= canvas.getPixelRed(x,y-1)
                    g+= canvas.getPixelGreen(x,y-1)
                    b+= canvas.getPixelBlue(x,y-1)
                    m = m + 1
                if y != h-1:
                    r+= canvas.getPixelRed(x-1,y+1)
                    g+= canvas.getPixelGreen(x-1,y+1)
                    b+= canvas.getPixelBlue(x-1,y+1)
                    m = m + 1
                    r+= canvas.getPixelRed(x,y+1)
                    g+= canvas.getPixelGreen(x,y+1)
                    b+= canvas.getPixelBlue(x,y+1)
                    m = m + 1
            else:
                r+= canvas.getPixelRed(x+1,y)
                g+= canvas.getPixelGreen(x+1,y)
                b+= canvas.getPixelBlue(x+1,y)
                m = m + 1
                r+= canvas.getPixelRed(x-1,y)
                g+= canvas.getPixelGreen(x-1,y)
                b+= canvas.getPixelBlue(x-1,y)
                m = m + 1
                if y != 0:
                    r+= canvas.getPixelRed(x+1,y-1)
                    g+= canvas.getPixelGreen(x+1,y-1)
                    b+= canvas.getPixelBlue(x+1,y-1)
                    m = m + 1
                    r+= canvas.getPixelRed(x,y-1)
                    g+= canvas.getPixelGreen(x,y-1)
                    b+= canvas.getPixelBlue(x,y-1)
                    m = m + 1
                    r+= canvas.getPixelRed(x-1,y-1)
                    g+= canvas.getPixelGreen(x-1,y-1)
                    b+= canvas.getPixelBlue(x-1,y-1)
                    m = m + 1
                if y != h-1:
                    r+= canvas.getPixelRed(x+1,y+1)
                    g+= canvas.getPixelGreen(x+1,y+1)
                    b+= canvas.getPixelBlue(x+1,y+1)
                    m = m + 1
                    r+= canvas.getPixelRed(x,y+1)
                    g+= canvas.getPixelGreen(x,y+1)
                    b+= canvas.getPixelBlue(x,y+1)
                    m = m + 1
                    r+= canvas.getPixelRed(x-1,y+1)
                    g+= canvas.getPixelGreen(x-1,y+1)
                    b+= canvas.getPixelBlue(x-1,y+1)
                    m = m + 1
            pic.setPixelColor(x,y,r/m,g/m,b/m)
                
    return pic


def rotate(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range (0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(w-x-1, h-y-1)
            g = canvas.getPixelGreen(w-x-1, h-y-1)
            b = canvas.getPixelBlue(w-x-1, h-y-1)
            pic.setPixelColor(x,y,r,g,b)
    return pic


def awesomeness(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range(0,w-1):
        for y in range(0,h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            pic.setPixelRed(x,y,(b//32)*32)
            pic.setPixelGreen(x,y,(r//32)*32)
            pic.setPixelBlue(x,y,(g//32)*32)
    return pic


def look(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    pic = picture2.Picture(w,h)
    for x in range(0, w-1):
        for y in range(0, h-1):
            r = canvas.getPixelRed(x,y)
            g = canvas.getPixelGreen(x,y)
            b = canvas.getPixelBlue(x,y)
            pic.setPixelColor(x,y,r,g,b)
    return pic
        
                           
def main():
    canvas = picture2.Picture("crayons.bmp")
    raw_input("You will be given a list of ideas to chose from. Please pick the one you wish to have done to a crayon image.")
    raw_input("")
    try: 
        n = eval(raw_input("For Flip Horizontally press 1, for Mirror Horizontally press 2, for Scroll Horizontally press 3, for Make Negative press 4, for make grayscale press 5. for cycle color channels press 6, for zoom press 7, for posterize press 8, for change brightness press 9, for increase contrast press 10, for blur press 11, for rotate 180 degrees press 12, for an awesome manipulation press 13, for multiple pictures of crayons press 14: "))  
        if n == 1:
            canvas = flip(canvas)
            canvas.display()
            input()
        elif n == 2:
            canvas = mirror(canvas)
            canvas.display()
            input()
        elif n == 3:
            d = eval(raw_input("How far? "))
            canvas = scroll(canvas, d)
            canvas.display()
            input()
        elif n == 4:
            canvas = negative(canvas)
            canvas.display()
            input()
        elif n == 5:
            canvas = grayscale(canvas)
            canvas.display()
            input()
        elif n == 6:
            canvas = cycle(canvas)
            canvas.display()
            input()
        elif n == 7:
            canvas = zoom(canvas)
            canvas.display()
            input()
        elif n ==8:
            canvas = posterize(canvas)
            canvas.display()
            input()
        elif n == 9:
            d = eval(raw_input("By how much would like the brightness to change; this value may be positive or negative."))
            canvas = brightness(canvas, d)
            canvas.display()
            input()
        elif n == 10:
            canvas = contrast(canvas)
            canvas.display()
            input()
        elif n == 11:
            canvas = blur(canvas)
            canvas.display()
            input()
        elif n == 12:
            canvas = rotate(canvas)
            canvas.display()
            input()
        elif n == 13:
            canvas = awesomeness(canvas)
            canvas.display()
            input()
        elif n == 14:
            raw_input("Look more crayons!")
            raw_input("Drag the first two images to the left and right respectively and see the surprise.")
            canvas = look(canvas)
            canvas.display()
            canvas2 = look(canvas)
            canvas2.display()
            canvas3 = look(canvas)
            canvas3.display()
            input()
        elif n > 14:
            raw_input("We do not have a manipulation for that, sorry.")
    except SyntaxError:
        raw_input("You may have an error somewhere in the program")
    

    
main()