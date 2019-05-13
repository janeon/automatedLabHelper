





import picture2


def copy(w, h, pic) :
    picCopy = picture2.Picture(w, h)
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            picCopy.setPixelColor(x, y, r, g, b)
    return picCopy


def flip(w, h, pic) :
    for x in range(0, w/2) :
        for y in range(0, h) :
            r1, g1, b1 = pic.getPixelColor(x, y)
            r2, g2, b2 = pic.getPixelColor(w-x-1, y)
            pic.setPixelColor(x, y, r2, g2, b2)
            pic.setPixelColor(w-x-1, y, r1, g1, b1)
    return pic


def mirror(w, h, pic) :
    for x in range(w/2, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(w-x, y)
            pic.setPixelColor(x, y, r, g, b)
    return pic


def scroll(w, h, pic) :
    gInput = False
    while not gInput :
        try :
            d = eval(raw_input("Please enter the number of pixels to be shifted: "))
            pic2 = copy(w, h, pic)
            for x in range(0, w) :
                for y in range(0, h) :
                    r, g, b = pic.getPixelColor(x, y)
                    pic2.setPixelColor((x+d)%w, y, r, g, b)
            gInput = True
        except NameError :
            print "You best be using those Arabic numerals fool!"
    return pic2


def negative(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, abs(255-r), abs(255-g), abs(255-b))
    return pic


def grayscale(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            avg = (r+g+b)/3
            pic.setPixelColor(x, y, avg, avg, avg)
    return pic


def cycle(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, b, r, g)
    return pic


def zoom(w, h, pic) :
    pic2 = picture2.Picture(w/2, h/2)
    for x in range(w/4, (3*w)/4) :
        for y in range(h/4, (3*h)/4) :
            r, g, b = pic.getPixelColor(x, y)
            pic2.setPixelColor(x-(w/4), y-(h/4), r, g, b)
    picZoom = picture2.Picture(w, h)
    for x in range(0, w) :
        if x%2 == 0 and x != w:
            for y in range(0, h-1) :
                r, g, b = pic2.getPixelColor(x/2, y/2)
                picZoom.setPixelColor(x, y, r, g, b)
                picZoom.setPixelColor(x+1, y+1, r, g, b)
    return picZoom


def posterize(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, abs(r-(r%32)), abs(g-(g%32)), abs(b-(b%32)))
    return pic


def brightness(w, h, pic) :
    gInput = False
    while not gInput :
        try :
            bright = eval(raw_input("Please enter the change in brightness, either positive or negative: "))
            for x in range(0, w) :
                for y in range(0, h) :
                    r, g, b = pic.getPixelColor(x, y)
                    r, g, b = r+bright, g+bright, b+bright
                    if r > 255 :
                        r = 255
                    if g > 255 :
                        g = 255
                    if b > 255 :
                        b = 255
                    if r < 0 :
                        r = 0
                    if g < 0 :
                        g = 0
                    if b < 0 :
                        b = 0
                    pic.setPixelColor(x, y, r, g, b)
            gInput = True
        except TypeError :
            print "You best be using those Arabic numerals fool!"
        except NameError :
            print "You best be using those Arabic numerals fool!"
    return pic


def contrast(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            r2, g2, b2 = (r-128)*2+128, (g-128)*2+128, (b-128)*2+128
            pic.setPixelColor(x, y, r2, g2, b2)
    return pic


def blur(w, h, pic) :
    pic2 = copy(w, h, pic)
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            count = 0
            try :
                rLTop, gLTop, bLTop = pic.getPixelColor(x-1, y-1)
                r, g, b = r+rLTop, g+gLTop, b+bLTop
                rLeft, gLeft, bLeft = pic.getPixelColor(x-1, y)
                r, g, b = r+rLeft, g+gLeft, b+bLeft
                rLDown, gLDown, bLDown = pic.getPixelColor(x-1, y+1)
                r, g, b = r+rLDown, g+gLDown, b+bLDown
                rDown, gDown, bDown = pic.getPixelColor(x, y+1)
                r, g, b = r+rDown, g+gDown, b+bDown
                rRDown, gRDown, bRDown = pic.getPixelColor(x+1, y+1)
                r, g, b = r+rRDown, g+gRDown, b+bRDown
                rRight, gRight, bRight = pic.getPixelColor(x+1, y)
                r, g, b = r+rRight, g+gRight, b+bRight
                rRTop, gRTop, bRTop = pic.getPixelColor(x+1, y-1)
                r, g, b = r+rRTop, g+gRTop, b+bRTop
                rTop, gTop, bTop = pic.getPixelColor(x, y-1)
                r, g, b = r+rTop, g+gTop, b+bTop
            except IndexError :
                count = count+1
            r, g, b = r/(9-count), g/(9-count), b/(9-count)
            pic2.setPixelColor(x, y, r, g, b)
    return pic2


def rotate(w, h, pic) :
    pic2 = copy(w, h, pic)
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            x2, y2 = abs(w-x-1), abs(h-y-1)
            pic2.setPixelColor(x2, y2, r, g, b)
    return pic2




def blackwhite(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            avg = (r+g+b)/3
            if avg <= 128 :
                pic.setPixelColor(x, y, 255, 255, 255)
            else :
                pic.setPixelColor(x, y, 0, 0, 0)
    return pic


def greenify(w, h, pic) :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = pic.getPixelColor(x, y)
            r, b = 0, 0
            pic.setPixelColor(x, y, r, g, b)
    return pic

def main() :
    print("Welcome to my insanely awesome Image Manipulator 2000!")
    goodInput = False
    while not goodInput :
        try :
            image = raw_input("Enter the file name of the image to be manipulated: ")
            pic = picture2.Picture(image)
            w = pic.getWidth()
            h = pic.getHeight()
            pic.display()
            raw_input()
            
            function = ""
            goodInput2 = False
            while not goodInput2 :
                print "Flip Horizontally"
                print "Mirror Horizontally"
                print "Scroll Horizontally"
                print "Make Negative"
                print "Make Grayscale"
                print "Cycle Color Channels"
                print "Zoom"
                print "Posterize"
                print "Change Brightness"
                print "Increase Contrast"
                print "Blur"
                print "Rotate 180 Degrees"
                print "Black and White"
                print "Green-ify"
                print ""
                print "Please select a function to manipulate your picture,"
                function = raw_input("or type \"close\" to exit: ")
                
                if function == "Flip Horizontally" :
                    pic = flip(w, h, pic)
                elif function == "Mirror Horizontally" :
                    pic = mirror(w, h, pic)
                elif function == "Scroll Horizontally" :
                    pic = scroll(w, h, pic)
                elif function == "Make Negative" :
                    pic = negative(w, h, pic)
                elif function == "Make Grayscale" :
                    pic = grayscale(w, h, pic)
                elif function == "Cycle Color Channels" :
                    pic = cycle(w, h, pic)
                elif function == "Zoom" :
                    pic = zoom(w, h, pic)
                elif function == "Posterize" :
                    pic = posterize(w, h, pic)
                elif function == "Change Brightness" :
                    pic = brightness(w, h, pic)
                elif function == "Increase Contrast" :
                    pic = contrast(w, h, pic)
                elif function == "Blur" :
                    pic = blur(w, h, pic)
                elif function == "Rotate 180 Degrees" :
                    pic = rotate(w, h, pic)
                elif function == "Black and White" :
                    pic = blackwhite(w, h, pic)
                elif function == "Green-ify" :
                    pic = greenify(w, h, pic)
                elif function == "close" :
                    goodInput2 = True
                else :
                    print "Please pick one of the listed functions."
                pic.display()
                raw_input()
            
            goodInput = True
            
        except IOError :
            print "No such file or directory in this folder."

main()