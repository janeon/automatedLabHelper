






import picture2
from random import randint

pic1 = picture2.Picture("crayons.bmp")
w, h = pic1.getWidth(), pic1.getHeight()
pic2 = picture2.Picture(w,h)
savePic = picture2.Picture(w,h)
for x in range(0, w) :
    for y in range(0, h) :
        r, g, b = pic1.getPixelColor(x,y)
        savePic.setPixelColor(x, y, r, g, b)


def main() :
    print ""
    print "Welcome to the Image Manipulator!"
    print ""
    print "Available operations are :"
    print "1. Horizontal Flip"
    print "2. Horizontal Mirror"
    print "3. Horizontal Scroll"
    print "4. Make Negative"
    print "5. Make Grayscale"
    print "6. Cycle Color Channels"
    print "7. Zoom"
    print "8. Posterize"
    print "9. Change Brightness"
    print "10. Increase Contrast"
    print "11. Blur"
    print "12. Rotate 180 Degrees"
    print "13. Blur More"
    print "14. Static"
    print "15. Quit"

    op = 0
    while op == 0 :
        try:
            op = input("Which operation would you like to perform? : ")
            if op != 15 :
                if op == 1 :
                    savePic = flipHorizontal()
                elif op == 2 :
                    savePic = mirrorHorizontal()
                elif op == 3 :
                    savePic = scrollHorizontal()
                elif op == 4 :
                    savePic = makeNegative()
                elif op == 5 :
                    savePic = makeGrayscale()
                elif op == 6 :
                    savePic = cycleColors()
                elif op == 7 :
                    savePic = zoom()
                elif op == 8 :
                    savePic = posterize()
                elif op == 9 :
                    savePic = brightness()
                elif op == 10 :
                    savePic = contrast()
                elif op == 11 :
                    savePic = blur()
                elif op == 12 :
                    savePic = rotate180()
                elif op == 13 :
                    savePic = blurMore()
                elif op == 14 :
                    savePic = static()
                else :
                    print "What are you doing?!"
                op = 0
        except SyntaxError :
            print "You are why we can't have nice things."
        except NameError :
            print "You are why we can't have nice things."

def flipHorizontal() :
    for x in range(1, w):
        for y in range(1, h) :
            r, g, b = savePic.getPixelColor(w - x, y)
            pic2.setPixelColor(x, y, r, g, b)   
    openPic(pic2)
    saveResults(pic2)
    return savePic

def mirrorHorizontal() :
    for x in range(0, w // 2) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x, y)
            pic2.setPixelColor(x,y,r,g,b)
            pic2.setPixelColor(w - 1 - x, y, r, g, b)
    openPic(pic2)
    saveResults(pic2)
    return savePic

def scrollHorizontal() :
    d = input("How far do you want to scroll? : ")
    scroll = w - d
    for x in range(0, scroll) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(w - scroll + x, y)
            pic2.setPixelColor(x,y,r,g,b)
    for x in range(scroll, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x-scroll,y)
            pic2.setPixelColor(x,y,r,g,b)
    openPic(pic2)
    saveResults(pic2)
    return savePic

def makeNegative() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            pic2.setPixelColor(x, y, 255-r, 255-g, 255-b)
    openPic(pic2)
    saveResults(pic2)
    return savePic

def makeGrayscale() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            gray = (r + g + b) // 3
            pic2.setPixelColor(x, y, gray, gray, gray)
    openPic(pic2)
    saveResults(pic2)
    return savePic

def cycleColors() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            pic2.setPixelColor(x, y, b, r, g)
    openPic(pic2)
    saveResults(pic2)
    return savePic
    
def zoom() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor((w / 4) + x // 2, (h / 4) + y // 2)
            pic2.setPixelColor(x, y, r, g, b)
    openPic(pic2)
    saveResults(pic2)
    return savePic

def posterize() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            pic2.setPixelColor(x, y, round32(r), round32(g), round32(b))
    openPic(pic2)
    saveResults(pic2)
    return savePic

def round32(x) :
    x = (x // 32) * 32
    return x

def brightness() :
    bright = input("Enter the amount to increase the brightness by : ")
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            pic2.setPixelColor(x, y, keep255(r + bright), keep255(g + bright), keep255(b + bright))
    openPic(pic2)
    saveResults(pic2)
    return savePic
    
def contrast() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            pic2.setPixelColor(x, y, cont2(r), cont2(g), cont2(b))
    openPic(pic2)
    saveResults(pic2)
    return savePic

def cont2(x) :
    if x < 128 :
        x = keep255(128 - 2 * (128 - x))
    elif x > 128 :
        x = keep255(128 + 2 * (x - 128))
    return x

def blur() :
    rav = 0
    gav = 0
    bav = 0
    for x in range(1, w-1) :
        for y in range(1, h-1) :
            for i in range(x-1, x+2) :
                for j in range(y-1, y+2) :
                    r, g, b = savePic.getPixelColor(i,j)
                    rav, gav, bav = rav + r, gav + g, bav + b
            pic2.setPixelColor(x, y, (rav // 9), (gav // 9), (bav // 9))
            rav, bav, gav = 0, 0, 0
    openPic(pic2)
    saveResults(pic2)
    return savePic

def catchEdge(x,w) :
    if x == 0 or 1 :
        x = 2
    elif x == w :
        x = w - 1
    return x

def rotate180() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(w - x - 1, h - y- 1)
            pic2.setPixelColor(x, y, r, g, b)
    openPic(pic2)
    saveResults(pic2)
    return savePic    

def blurMore() :
    rav = 0
    gav = 0
    bav = 0
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = savePic.getPixelColor(x,y)
            pic2.setPixelColor(x, y, r, g, b)
    for x in range(1, w-2) :
        for y in range(1, h-2) :
            for i in range(x-1, x+3) :
                for j in range(y-1, y+3) :
                    r, g, b = savePic.getPixelColor(i,j)
                    rav, gav, bav = rav + r, gav + g, bav + b
            pic2.setPixelColor(x, y, (rav // 16), (gav // 16), (bav // 16))
            rav, bav, gav = 0, 0, 0
    openPic(pic2)
    saveResults(pic2)
    return savePic

def static() :
    for x in range(0, w) :
        for y in range(0, h) :
            r, g, b = randint(0,255), randint(0,255), randint(0,255)
            pic2.setPixelColor(x, y, r, g, b)
    openPic(pic2)
    saveResults(pic2)
    return savePic    

def keep255(x) :
    if x > 255 :
        x = 255
    elif x < 0 :
        x = 0
    return x

def openPic(pic2) :
    print "Operation successful!"
    while raw_input("Do you want to continue or refresh the window? : ") != "continue" :
        pic2.display()

def saveResults(pic2) :
    yn = raw_input("Would you like to keep the results of this operation? [Y/N] : ")
    if yn == "Y" :
        for x in range(0, w) :
            for y in range(0, h) :
                r, g, b = pic2.getPixelColor(x, y)
                savePic.setPixelColor(x, y, r, g, b)
    return savePic


main()