







import picture2
import math

def makeCopy(pic, w, h):
    copy = picture2.Picture(w, h)
    for i in range(w):
        for j in range(h):
            copy.setPixelColor(i, j, pic.getPixelRed(i, j),pic.getPixelGreen(i, j),pic.getPixelBlue(i, j))
    return copy

def flipHorizontally(pic, w, h):
    for i in range(w//2):
        for j in range(h):
            r, g, b = pic.getPixelRed(i, j),pic.getPixelGreen(i, j),pic.getPixelBlue(i, j)
            pic.setPixelColor(i, j, pic.getPixelRed(w-i-1, j), pic.getPixelGreen(w-i-1, j),pic.getPixelBlue(w-i-1, j))
            pic.setPixelColor(w-i-1, j, r, g, b)

def mirrorHorizontally(pic, w, h):
    choice = ''
    while choice != 'l' and choice != 'r':
        choice = raw_input("Which side do you want mirrored (l or r): ")  
    if choice == "l":
        for i in range(w//2):
            for j in range(h):
                pic.setPixelColor(w-i-1, j, pic.getPixelRed(i,j), pic.getPixelGreen(i,j), pic.getPixelBlue(i,j))
    else:
        for i in range(w//2):
            for j in range(h):
                pic.setPixelColor(i, j, pic.getPixelRed(w-i-1,j), pic.getPixelGreen(w-i-1,j), pic.getPixelBlue(w-i-1,j))

def scrollHorizontally(pic, w, h):
    direction = ''
    scrolldistance = ''
    while direction != "l" and direction != "r":
        direction = raw_input("Which direction to scroll (l or r): ")
    while type(scrolldistance) != int :
        try:
            scrolldistance = input("How many pixels to scroll? ")
        except:
            print("You need to enter an integer.")
    copy = makeCopy(pic, w, h)
    if direction == "l":    
        for i in range(w):
            for j in range(h):
                r, g, b = copy.getPixelColor((i+scrolldistance)%w, j)
                pic.setPixelColor(i,j,r,g,b)
    else:
        for i in range(w):
            for j in range(h):
                r, g, b = copy.getPixelColor(i, j)
                pic.setPixelColor((i+scrolldistance)%w,j,r,g,b)

def makeNegative(pic, w, h):
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, 255-r, 255-g, 255-b)

def makeGreyscale(pic, w, h):
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            avg = (r+g+b)//3
            pic.setPixelColor(i, j, avg, avg, avg)

def cycleColorChannels(pic, w, h):
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, b, r, g)

def zoom(pic, w, h):
    copy = makeCopy(pic, w, h)
    for i in range(w):
        for j in range(h):
            r, g, b = copy.getPixelColor((i+ w//2)//2, (j+ h//2)//2)
            pic.setPixelColor(i,j, r, g, b)
            
def posterize(pic, w, h):
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            r = int(round(r/32)*32)
            g = int(round(g/32)*32)
            b = int(round(b/32)*32)
            pic.setPixelColor(i, j, r, g, b)
    
def changeBrightness(pic, w, h):
    change = ''
    while type(change) != int:
        try:
            change = input("How much to change brightness by? \nNegative means darker positive means brighter: ")
        except:
            print "Please enter an integer."
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            r, g, b = r + change, g + change, b + change
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b <  0:
                b = 0
            pic.setPixelColor(i, j, r, g, b)

def contrast(pic, w, h):
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            r, g, b = (2*r - 128, 2*g - 128, 2*b - 128)
            r-128
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b <  0:
                b = 0
            pic.setPixelColor(i, j, r, g, b)

def blur(pic, w, h):
    copy = makeCopy(pic, w, h)
    for i in range(1, w-1):
        for j in range(1, h-1):
            r, g, b = 0, 0, 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    tempr, tempg, tempb = copy.getPixelColor(k,l)
                    r, g, b = r+tempr, g+tempg, b+tempb
            r,g,b =r//9, g//9, b//9
            pic.setPixelColor(i,j,r,g,b)

def rotate(pic, w, h):
    copy = makeCopy(pic, w, h)
    for i in range(w):
        for j in range(h):
            r, g, b = copy.getPixelColor(w-1-i,h -1- j)
            pic.setPixelColor(i, j, r, g, b)

def ghost(pic, w, h):
    copy = makeCopy(pic, w, h)
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            r, g, b = copy.getPixelColor(i, j)
            avg = (r+g+b)//3
            for k in [i-1, i+1]:
                for l in [j-1, j+1]:
                    x, y, z =copy.getPixelColor(k, l)
                    if x > 25 + r or x< r - 35 or y > 25 + g or y< g - 35 or z > 25 + b or z< b - 35:
                        pic.setPixelColor(i, j, int(r/1.5), int(g/1.5), int(b/1.5))
                    else:
                        pic.setPixelColor(i, j, 255- (r//3), 255-(g//3), 255-(b//3))

def sepia(pic, w, h):
    for i in range(w):
        for j in range(h):
            r, g, b = pic.getPixelColor(i, j)
            avg = (r+g+b)/3
            r = int(avg*1.6)
            if r > 255:
                r = 255
            g = int(avg*0.8)
            b = int(avg*0.5)
            pic.setPixelColor(i, j, r, avg, b)

def blast(pic, w, h):
    maxdistance = math.sqrt((w//2)**2 + (h//2)**2) - .001
    for i in range(w):
        for j in range(h):
            distance = (math.sqrt((w//2 - i)**2 + (h//2 - j)**2)) - 0.1
            r, g, b = pic.getPixelColor(i, j)
            r = int((r)*maxdistance/(distance) - ((distance/maxdistance)**4)*150 + ((maxdistance/(distance + 1)))*10)
            g = int((g)*maxdistance/(distance) - ((distance/maxdistance)**4)*150 + ((maxdistance/(distance + 1)))*10)
            b = int((b)*maxdistance/(distance) - ((distance/maxdistance)**4)*150 + ((maxdistance/(distance + 1)))*10)
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            pic.setPixelColor(i, j, r, g, b)

def original(pic, w, h, picAddress):
    extra = picture2.Picture(picAddress)
    for i in range(w):
        for j in range(h):
            r, g, b = extra.getPixelColor(i, j)
            pic.setPixelColor(i, j, r, g, b)

def troll(pic, w, h):
    try:    
        troll =picture2.Picture("50ec2429d49e3.bmp")
        tw = troll.getWidth()
        th = troll.getHeight()
        for i in range(w):
            for j in range(h):
                if i < tw and j<th:
                    r, g, b = troll.getPixelColor(i, j)
                    pic.setPixelColor(i, j, r, g, b)
                else:
                    pic.setPixelColor(i, j, 0, 0 ,0)
    except:
        print "Sorry we can't do this one. Prolly has something to do with\n the handin system. :( "
        
def main():
    print "This program is AWESOME!!!!!"
    print "It will let you make all sorts of AMAZING modifications to an image."
    pic = ''
    while pic == '':
        picAddress = raw_input("Please enter the file name of a picture: ")
        try:
            pic = picture2.Picture(picAddress)
        except:
            print "That is not a valid picture."
    w = pic.getWidth()
    h = pic.getHeight()
    done = False
    pic.display()
    print
    print "You may make any of the following modifications to your picture: "
    print "1. Flip Horizontally  2. Mirror Horizontally  3. Scroll Horizontally"
    print "4. Make Negative  5. Make Greyscale  6. Cycle Color Channels  7. Zoom 2x"
    print "8. Posterize  9. Change Brightness  10. Increase Contrast  11. Blur"
    print "12. Rotate 180 Degrees  13. Ghost 14. Sepia  15. Bright Spot"
    print "16. Surprise  17. Get Original Picture Back 18.  Exit the Program "
    print "Entering 'help' will repeat this list"
    print
    while not done:
        x = raw_input("Please enter the number corresponding to one of the options: ")
        if x == '1':
            flipHorizontally(pic, w, h)
        elif x == '2':
            mirrorHorizontally(pic, w, h)
        elif x == '3':
            scrollHorizontally(pic, w, h)
        elif x == '4':
            makeNegative(pic, w, h)
        elif x == '5':
            makeGreyscale(pic, w, h)
        elif x == '6':
            cycleColorChannels(pic, w, h)
        elif x == '7':
            zoom(pic, w, h)
        elif x == '8':
            posterize(pic, w, h)
        elif x == '9':
            changeBrightness(pic, w, h)
        elif x == '10':
            contrast(pic, w, h)
        elif x == '11':
            blur(pic, w, h)
        elif x == '12':
            rotate(pic, w, h)
        elif x == '13':
            ghost(pic, w, h)
        elif x == '14':
            sepia(pic, w, h)
        elif x == '15':
            blast(pic, w, h)
        elif x == '18' or x == 'exit':
            done = True
        elif x == '17':
            original(pic, w, h, picAddress)
        elif x == '16':
            troll(pic, w, h)
        elif x == 'help':
            print
            print "You may make any of the following modifications to your picture: "
            print "1. Flip Horizontally  2. Mirror Horizontally  3. Scroll Horizontally"
            print "4. Make Negative  5. Make Greyscale  6. Cycle Color Channels  7. Zoom 2x"
            print "8. Posterize  9. Change Brightness  10. Increase Contrast  11. Blur"
            print "12. Rotate 180 Degrees  13. Ghost  14. Sepia  15. Bright Spot"
            print "16. Surprise    17. Get Original Picture Back 18. Exit the Program"
            print "Entering 'help' will repeat this list"
            print
        else:
            print "YOU MAKE TYPO. ENTER NUMBER 1 TO 16 OR 'help' TO REPEAT INSTRUCTIONS"
        pic.display()
    print "I IS SAD NOW :("

main()