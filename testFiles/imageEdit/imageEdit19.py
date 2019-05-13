






import picture2

def main():
    n = raw_input("What picture would you like to edit? To use our crayons, enter 'crayons.bmp' ")
    pic = picture2.Picture(n)
    w = pic.getWidth()
    h = pic.getHeight()
    print "Here are the options for editing your picture. Please type in the number of the effect you would like to use."
    print "1 - Flip Horizontally", "2 - Mirror Horizontally", "3 - Scroll Horizontally"
    print "4 - Make Negative", "5 - Make Grayscale", "6 - Cycle Color Channels"
    print "7 - Zoom", "8 - Posterize", "9 - Change Brightness"
    print "10 - Increase Contrast", "11 - Blur", "12 - Rotate 180 Degrees"
    print "13 - Icepop effect", "14 - 'Gone Clubbing' effect", "type exit to quit"
    f = ""
    while f != exit:
        function = eval(raw_input("Please enter a number: "))
        if function == 1:
            flipHorizontal(pic, w, h)
        if function == 2:
            mirror(pic, w, h)
        if function == 3:
            scroll(pic, w, h)
        if function == 4:
            negative(pic, w, h)
        if function == 5:
            grayscale(pic, w, h)
        if function == 6:
            cyclecolorchannels(pic, w, h)
        if function == 7:
            zoom(pic, w, h)
        if function == 8:
            posterize(pic, w, h)
        if function == 9:
            changebrightness(pic, w, h)
        if function == 10:
            increasecontrast(pic, w, h)
        if function == 11:
            blur(pic, w, h)
        if function == 12:
            rotate180(pic, w, h)
        if function == 13:
            icepop(pic, w, h)
        if function == 14:
            GoneClubbing(pic, w, h)
        if function == "exit":
            f = exit
    
    
    
    
    
def copy(pic, w, h):
    picCopy = picture2.Picture(w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i,j)
            picCopy.setPixelColor(i, j, r, g, b)
    return picCopy
            
            
def flipHorizontal(pic, w, h):
    picCopy = copy(pic, w, h)
    for x in range(0, w-1):
        for y in range(0, h-1):
            r, g, b = pic.getPixelColor(x, y)
            picCopy.setPixelColor(w-x-1, y, r, g, b)
    picCopy.display()
    input()

def rotate180(pic, w, h):
    picCopy = copy(pic, w, h)
    for x in range(0, w-1):
        for y in range(0, h-1):
            r, g, b = pic.getPixelColor(x, y)
            picCopy.setPixelColor(w-x-1, h-y-1, r, g, b)
    picCopy.display()
    input()

def scroll(pic, w, h):
    picCopy = copy(pic, w, h)
    n = eval(raw_input("Please enter a number of pixels: "))
    n = n % pic.getWidth()
    for x in range(0, w-1):
        for y in range(0, h-1):
            r, g, b = pic.getPixelColor(x, y)
            if (n+x) <= w:
                picCopy.setPixelColor(n+x-1, y, r, g, b)
            else:
                q = n + x - 1
                while q > w:
                    q = q - w
                    picCopy.setPixelColor(q, y, r, g, b)
    picCopy.display()
    input()

def zoom(pic, w, h): 
    picCopy = copy(pic, w, h)
    for x in range(w/4, ((3*w)/4)-1):
        for y in range(h/4, ((3*h)/4)-1):
            r, g, b = pic.getPixelColor(x, y)
            for i in range((x-(w/4))*2, (x-(w/4))*2 + 2):
                for j in range((y-(h/4))*2, (y-(h/4))*2 + 2):
                    picCopy.setPixelColor(i, j, r, g, b)
    picCopy.display()
    input()

    
def blur(pic, w, h):
    picCopy = copy(pic, w, h)
    for x in range(0, w-1):
        for y in range (0, h-1):
            if x == 0 and y != 0 and y!= h-1:
                r, g, b = pic.getPixelColor(x, y)
                rr, gg, bb = pic.getPixelColor(x, y+1)
                rrr, ggg, bbb = pic.getPixelColor(x+1, y+1)
                rrrr, gggg, bbbb = pic.getPixelColor(x, y-1)
                rrrrr, ggggg, bbbbb = pic.getPixelColor(x+1, y-1)
                rrrrrr, gggggg, bbbbbb = pic.getPixelColor(x+1, y)
                aveR = (r + rr + rrr + rrrr + rrrrr + rrrrrr)/6
                aveG = (g + gg + ggg + gggg + ggggg + gggggg)/6
                aveB = (b + bb + bbb + bbbb + bbbbb + bbbbbb)/6
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif y == 0 and x != 0 and x != w-1:
                r, g, b = pic.getPixelColor(x, y)
                rr, gg, bb = pic.getPixelColor(x, y+1)
                rrr, ggg, bbb = pic.getPixelColor(x+1, y+1)
                rrrr, gggg, bbbb = pic.getPixelColor(x+1, y)
                rrrrr, ggggg, bbbbb = pic.getPixelColor(x-1, y)
                rrrrrr, gggggg, bbbbbb = pic.getPixelColor(x-1, y+1)
                aveR = (r + rr + rrr + rrrr + rrrrr + rrrrrr)/6
                aveG = (g + gg + ggg + gggg + ggggg + gggggg)/6
                aveB = (b + bb + bbb + bbbb + bbbbb + bbbbbb)/6
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif x == w-1 and y != h-1 and y != 0:
                r, g, b = pic.getPixelColor(w, y)
                rr, gg, bb = pic.getPixelColor(w, y-1)
                rrr, ggg, bbb = pic.getPixelColor(w, y+1)
                rrrr, gggg, bbbb = pic.getPixelColor(w-1, y-1)
                rrrrr, ggggg, bbbbb = pic.getPixelColor(w-1, y)
                rrrrrr, gggggg, bbbbbb = pic.getPixelColor(w-1, y+1)
                aveR = (r + rr + rrr + rrrr + rrrrr + rrrrrr)/6
                aveG = (g + gg + ggg + gggg + ggggg + gggggg)/6
                aveB = (b + bb + bbb + bbbb + bbbbb + bbbbbb)/6
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif y == h-1 and x != w-1 and x != 0:
                r, g, b = pic.getPixelColor(x, h)
                rr, gg, bb = pic.getPixelColor(x, h-1)
                rrr, ggg, bbb = pic.getPixelColor(x-1, h)
                rrrr, gggg, bbbb = pic.getPixelColor(x-1, h-1)
                rrrrr, ggggg, bbbbb = pic.getPixelColor(x+1, h-1)
                rrrrrr, gggggg, bbbbbb = pic.getPixelColor(x+1, h)
                aveR = (r + rr + rrr + rrrr + rrrrr + rrrrrr)/6
                aveG = (g + gg + ggg + gggg + ggggg + gggggg)/6
                aveB = (b + bb + bbb + bbbb + bbbbb + bbbbbb)/6
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif y == 0 and x == 0:
                r, g, b = pic.getPixelColor(x, y)
                rr, gg, bb = pic.getPixelColor(x, y+1)
                rrr, ggg, bbb = pic.getPixelColor(x+1, y)
                rrrr, gggg, bbbb = pic.getPixelColor(x+1, y+1)
                aveR = (r + rr + rrr + rrrr)/4
                aveG = (g + gg + ggg + gggg)/4
                aveB = (b + bb + bbb + bbbb)/4
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif y == 0 and x == w-1:
                r, g, b = pic.getPixelColor(w, y)
                rr, gg, bb = pic.getPixelColor(w, y+1)
                rrr, ggg, bbb = pic.getPixelColor(w-1, y)
                rrrr, gggg, bbbb = pic.getPixelColor(w-1, y+1)
                aveR = (r + rr + rrr + rrrr)/4
                aveG = (g + gg + ggg + gggg)/4
                aveB = (b + bb + bbb + bbbb)/4
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif y == h-1 and x == w-1:
                r, g, b = pic.getPixelColor(w, h)
                rr, gg, bb = pic.getPixelColor(w-1, h-1)
                rrr, ggg, bbb = pic.getPixelColor(w, h-1)
                rrrr, gggg, bbbb = pic.getPixelColor(w-1, h)
                aveR = (r + rr + rrr + rrrr)/4
                aveG = (g + gg + ggg + gggg)/4
                aveB = (b + bb + bbb + bbbb)/4
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            elif y == h-1 and x == 0:
                r, g, b = pic.getPixelColor(x, h)
                rr, gg, bb = pic.getPixelColor(x+1, h)
                rrr, ggg, bbb = pic.getPixelColor(x, h-1)
                rrrr, gggg, bbbb = pic.getPixelColor(x+1, h-1)
                aveR = (r + rr + rrr + rrrr)/4
                aveG = (g + gg + ggg + gggg)/4
                aveB = (b + bb + bbb + bbbb)/4
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
            else:
                r, g, b = pic.getPixelColor(x, y)
                rr, gg, bb = pic.getPixelColor(x, y+1)
                rrr, ggg, bbb = pic.getPixelColor(x+1, y+1)
                rrrr, gggg, bbbb = pic.getPixelColor(x, y-1)
                rrrrr, ggggg, bbbbb = pic.getPixelColor(x+1, y-1)
                rrrrrr, gggggg, bbbbbb = pic.getPixelColor(x+1, y)
                f, t, v = pic.getPixelColor(x-1, y-1)
                ff, tt, vv = pic.getPixelColor(x-1, y)
                fff, ttt, vvv = pic.getPixelColor(x-1, y+1)
                aveR = (r + rr + rrr + rrrr + rrrrr + rrrrrr + f + ff + fff)/9
                aveG = (g + gg + ggg + gggg + ggggg + gggggg + t + tt + ttt)/9
                aveB = (b + bb + bbb + bbbb + bbbbb + bbbbbb + v + vv + vvv)/9
                picCopy.setPixelColor(x, y, aveR, aveG, aveB)
    picCopy.display()
    input()
    
    
def mirror(pic, w, h):
    for x in range(0, w-1):
        for y in range(0, h-1):
            r = pic.getPixelRed(x,y)
            pic.setPixelRed(w-x-1, y, r)
            g = pic.getPixelGreen(x,y)
            pic.setPixelGreen(w-x-1, y, g)
            b = pic.getPixelBlue(x, y)
            pic.setPixelBlue(w-x-1, y, b)
    pic.display()
    input()

def negative(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, 255-r, 255-g, 255-b)
    pic.display()       
    input()

def posterize(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            if r <= 16:
                pic.setPixelRed(i,j, 0)
            if g <= 16:
                pic.setPixelGreen(i,j, 0)
            if b <= 16:
                pic.setPixelBlue(i,j, 0)
            if r > 16 and r <=48:
                pic.setPixelRed(i,j, 32)
            if g > 16 and g <=48:
                pic.setPixelGreen(i,j, 32)
            if b > 16 and b <=48:
                pic.setPixelBlue(i,j, 32)
            if r > 48 and r <=80:
                pic.setPixelRed(i,j, 64)
            if g > 48 and g <=80:
                pic.setPixelGreen(i,j, 64)
            if b > 48 and b <=80:
                pic.setPixelBlue(i,j, 64)
            if r > 80 and r <=112:
                pic.setPixelRed(i,j, 96)
            if g > 80 and g <=112:
                pic.setPixelGreen(i,j, 96)
            if b > 80 and b <=112:
                pic.setPixelBlue(i,j, 96)
            if r > 112 and r <=144:
                pic.setPixelRed(i,j, 128)
            if g > 112 and g <=144:
                pic.setPixelGreen(i,j, 128)
            if b > 112 and b <=144:
                pic.setPixelBlue(i,j, 128)
            if r > 144 and r <=176:
                pic.setPixelRed(i,j, 160)
            if g > 144 and g <=176:
                pic.setPixelGreen(i,j, 160)
            if b > 144 and b <=176:
                pic.setPixelBlue(i,j, 160)
            if r > 176 and r <=208:
                pic.setPixelRed(i,j, 192)
            if g > 176 and g <=208:
                pic.setPixelGreen(i,j, 192)
            if b > 176 and b <=208:
                pic.setPixelBlue(i,j, 192)  
            if r > 208 and r <=240:
                pic.setPixelRed(i,j, 224)
            if g > 208 and g <=240:
                pic.setPixelGreen(i,j, 224)
            if b > 208 and b <=240:
                pic.setPixelBlue(i,j, 224)
            if r > 240:
                pic.setPixelRed(i,j, 255)
            if g > 240:
                pic.setPixelGreen(i,j, 255)
            if b > 240:
                pic.setPixelBlue(i,j, 255)
           
    pic.display()       
    input()

def grayscale(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            a = (r + g + b)/3
            pic.setPixelColor(i, j, a, a, a)
    pic.display()       
    input()
    
def increasecontrast(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            a = (abs(128-r))*2
            bb = (abs(128-g))*2
            c = (abs(128-b))*2
            if r > 128:
                pic.setPixelRed(i, j, 128+a)
            else:
                pic.setPixelRed(i, j, 128-a)
            if g > 128:
                pic.setPixelGreen(i, j, 128+bb)
            else:
                pic.setPixelGreen(i, j, 128-bb)
            if b > 128:
                pic.setPixelBlue(i, j, 128+c)
            else:
                pic.setPixelBlue(i, j, 128-c)   
    pic.display()       
    input()

def cyclecolorchannels(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, b, r, g)
    pic.display()       
    input()   

def changebrightness(pic, w, h):
    n = eval(raw_input("Please enter a value to change the color pixels: "))
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
    while (r + n) > 255 or (g+n) > 255 or (b+n) > 255:
        n = eval(raw_input("Please enter a lower value: "))
    while (r + n) < 0 or (g+n) < 0 or (b+n) < 0:
        n = eval(raw_input("Please enter a larger value: "))
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, r+n, g+n, b+n)
    pic.display()       
    input()
    
def GoneClubbing(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, 255-g, r, g)
    pic.display()       
    input()

def icepop(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            r, g, b = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, r, 255-r, 255-r)
    pic.display()       
    input()
    
main()