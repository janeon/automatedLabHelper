





import picture2
import random
pic = picture2.Picture("crayons.bmp")

def copy(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    copy = picture2.Picture(w,h)
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            copy.setPixelColor(i,j,r,g,b)
    return copy

def flip(pic): 
    dup = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            dup.setPixelColor(w-i-1,j,r,g,b)
    return dup

def mirror(pic): 
    dup = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w//2):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            dup.setPixelColor(w-i-1,j,r,g,b)
    return dup
    
def scroll(pic): 
    test = False
    while test == False:
        try:
            s = eval(raw_input("Enter how many pixels to the right you'd like to scroll: "))
            new = copy(pic)
            w = pic.getWidth()
            h = pic.getHeight()
            for i in range(w):
                for j in range(h):
                    r,g,b = pic.getPixelColor(i,j)
                    new.setPixelColor((i+s)%w,j,r,g,b)
            test = True
        except:
            print''
            print'Enter valid input.'
            print''
    return new

def negative(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            c,m,y = pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,255-c,255-m,255-y)
    return pic
 
def grayscale(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            n = (r+g+b)/3
            pic.setPixelColor(i,j,n,n,n)
    return pic

def ccc(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,b,r,g)
    return pic

def zoom(pic): 
    new = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(w//2):
        for j in range(h//2) :
            r,g,b = pic.getPixelColor(i+w//4,j+h//4)
            new.setPixelColor(2*i,2*j,r,g,b)
            new.setPixelColor(2*i+1,2*j,r,g,b)
            new.setPixelColor(2*i,2*j+1,r,g,b)
            new.setPixelColor(2*i+1,2*j+1,r,g,b)    
    return new

def posterize(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(w):
        for j in range(h):
            r,g,b = pic.getPixelColor(i,j)
            r = int((round((r+1)/32)*32-1))
            g = int((round((g+1)/32)*32-1))
            b = int((round((b+1)/32)*32-1))
            pic.setPixelColor(i,j,r,g,b)
    return pic

def bright(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    test = False
    while test == False:
        try:
            print "Enter how much you'd like the picture brightened."
            a = eval(raw_input("(Effective values are in the range -1 to 1): "))
            if a > 1:
                a = 1
            if a < -1:
                a = -1
            for i in range(0,w):
                for j in range(0,h):
                    r,g,b = pic.getPixelColor(i,j)
                    if a > 0 :
                        r = r + int(round((255-r)*a))
                        g = g + int(round((255-g)*a))
                        b = b + int(round((255-b)*a))
                        pic.setPixelColor(i,j,r,g,b)
                    if a < 0 :
                        r = int(round(r - (r*(-a))))
                        g = int(round(g - (g*(-a))))
                        b = int(round(b - (b*(-a))))
                        pic.setPixelColor(i,j,r,g,b)
            test = True
        except:
            print''
            print'Enter valid input.'
            print''
    return pic

def contrast(pic): 
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            r = ((r-128)*2+r)
            g = ((g-128)*2+g)
            b = ((b-128)*2+b)
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
            pic.setPixelColor(i,j,r,g,b)
    return pic

def blur(pic): 
    new = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    c,m,y = 0,0,0
    for i in range(0,w):
        for j in range(0,h):
            p = 9
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    try:
                        d,n,z = pic.getPixelColor(k,l)
                        c = c + d
                        m = m + n
                        y = y + z
                    except IndexError:
                        p = p-1
            c = int(round(c/p))
            m = int(round(m/p))
            y = int(round(y/p))
            new.setPixelColor(i,j,c,m,y)
    return new
    
def rotate180(pic): 
    dup = copy(pic)
    w = pic.getWidth()
    h = pic.getHeight()
    pic = flip(pic)
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            dup.setPixelColor(i,h-j-1,r,g,b)
    return dup

def m1(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            if r >= 128:
                r = 255
            if r < 128:
                r = 0
            if g >= 128:
                g = 255
            if g < 128:
                g = 0
            if b >= 128:
                b = 255
            if b < 128:
                b = 0
            pic.setPixelColor(i,j,g,r,b)
    return pic

def m2(pic):
    pic = ccc(zoom(posterize(mirror(pic))))
    w = pic.getWidth()
    h = pic.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = pic.getPixelColor(i,j)
            if 200 > r > 50:
                rInt = random.randrange(-30,30)
                r = r + rInt
            if 200 > g > 50:
                rInt = random.randrange(-30,30)
                g = g + rInt
            if 200 > b > 50:
                rInt = random.randrange(-30,30)
                b = b + rInt
            pic.setPixelColor(i,j,r,g,b)
    return pic

def main():
    print ""
    print "Hello. Welcome to my Image Editor. "
    print''
    test = False
    while test == False:
        try:
            pic = raw_input("Please enter your image file: ")
            pic = picture2.Picture(pic)
            pic.display()
            print''
            raw_input("Press any key to continue.")
            test = True
        except:
            print''
            print'Enter valid file type.'
            print''
    print ""
    end = False
    while end == False:
        print "Select the appropriate number for the operation: "
        print "1. Flip horiz., 2. Mirror horiz. 3. scroll, 4. negative, 5. grayscale, 6. cycle color channels, 7. zoom"
        print "8. posterize, 9. change brightness, 10. increase contrast, 11. blur, 12. Mystery I, 13. Mystery II, 14. quit."
        print "10. increase contrast, 11. blur, 12. Rotate 180 degrees 13. Mystery I, 14. Mystery II, 15. quit."
        try:
            func = eval(raw_input("Enter here: "))
            if func == 15:
                end = True
            elif func < 1 or func > 15 or type(func)!= int or type(func) == str:
                print ''
                print 'Enter valid input.'
                raw_input("Press any key to continue.")
                print''
            else:
                if func == 1:
                    pic = flip(pic)
                if func == 2:
                    pic = mirror(pic)
                if func == 3:
                    pic = scroll(pic)
                if func == 4:
                    pic = negative(pic)
                if func == 5:
                    pic = grayscale(pic)
                if func == 6:
                    pic = ccc(pic)
                if func == 7:
                    pic = zoom(pic)
                if func == 8:
                    pic = posterize(pic)
                if func == 9:
                    pic = bright(pic)
                if func == 10:
                    pic = contrast(pic)
                if func == 11:
                    pic = blur(pic)
                if func == 12:
                    pic = rotate180(pic)
                if func == 13:
                    pic = m1(pic)
                if func == 14:
                    pic = m2(pic)
                pic.display()
                print ""
                raw_input("Press any key to continue.")
        except:
            print ''
            print 'Enter valid input!'
            raw_input("Press any key to continue.")
            print ''
main()