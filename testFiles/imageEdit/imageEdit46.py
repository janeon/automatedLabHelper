





import picture2 

def main ():
    
    print "Welcome to the image editor"
    flag = True 
    while flag == True: 
        try:
            filename = raw_input("Please enter the filename ending in .bmp: ") 
            pic = picture2.Picture(filename)
            w = pic.getWidth()
            h = pic.getHeight()
            pic2 = picture2.Picture(w,h)
            flag = False 
        except IOError:
            print "Please enter a valid filename ending in bmp."
            print " "
        except :
            print "Unknown error.  Please try again."
            print " "
            
    print "Thanks!  Here are your choices!"
    print " "
    print "1.Flip Horizontally"
    print "2.Mirror Horizontally" 
    print "3.Scroll Horizontally"
    print "4.Make Negative"
    print "5.Make Grayscale"
    print "6.Cycle Color Channels"
    print "7.Zoom"
    print "8.Posterize"
    print "9.Change Brightness"
    print "10.Increase Contrast"
    print "11.Blur"
    print "12.Rotate 180 Degrees"
    print" "
    
    while flag == False: 
        try:
            method = eval(raw_input("Please enter the number corresponding to the manipulation you would like: "))
            
            if method == 1:
                flip(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 2:
                mirror(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 3:
                scroll(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 4:
                negat(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 5:
                grayscale(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 6:
                cycle(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 7:
                zoom(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 8:
                poster(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 9:
                bright(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 10:
                contrast(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 11:
                blur(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            elif method == 12:
                rotate(w,h,pic,pic2)
                pic.display()
                flag = True
                input()
            else:
                print "Please enter a number from 1 to 12"
                print " "  
        except NameError:
            if flag != True:    
                print "Please enter a number value"
                print " " 
        except :
            if flag != True:    
                print "Unknown error.  Please try again."
                print " "

def copy (w,h,pic,pic2):
    
    for y in range (0,h) :
        for x in range (0,w) :
            pic2.setPixelColor(x,y,pic.getPixelRed(x,y),pic.getPixelGreen(x,y),pic.getPixelBlue(x,y))

def flip (w,h,pic,pic2):
    
    for y in range (0,h) :
        for x in range (0,w) :
            pic2.setPixelColor((w-1-x),y,pic.getPixelRed(x,y),pic.getPixelGreen(x,y),pic.getPixelBlue(x,y))
            
    copy(w,h,pic2,pic)
    
def rotate (w,h,pic,pic2) :
    
    for y in range (0,h) :
        for x in range (0,w) :
            pic2.setPixelColor((w-1-x),y,pic.getPixelRed(x,y),pic.getPixelGreen(x,y),pic.getPixelBlue(x,y))
    
    for y in range (0,h) :
        for x in range (0,w) :
            pic.setPixelColor(x,(h-1-y),pic2.getPixelRed(x,y),pic2.getPixelGreen(x,y),pic2.getPixelBlue(x,y))

def mirror (w,h,pic,pic2) :
    
    for y in range (0,h) :
        for x in range (0,w) :
            pic2.setPixelColor((w-1-x),y,pic.getPixelRed(x,y),pic.getPixelGreen(x,y),pic.getPixelBlue(x,y))
    
    wTwo = w//2
    
    for y in range (0,h) :
        for x in range (wTwo,w) :
            pic.setPixelColor(x,y,pic2.getPixelRed(x,y),pic2.getPixelGreen(x,y),pic2.getPixelBlue(x,y))

def scroll (w,h,pic,pic2) :
    
    flag = True
    
    while flag == True :
        try:
            print " "
            scroll = eval(raw_input("Please enter how many pixels you'd like to scroll:"))
            
            copy(w,h,pic,pic2)
            
            for y in range (0,h) :
                for x in range (0,w-scroll) :
                    pic.setPixelColor(x,y,pic2.getPixelRed(x+scroll,y),pic2.getPixelGreen(x+scroll,y),pic2.getPixelBlue(x+scroll,y))
            
            for y in range (0,h) :
                for x in range (w-scroll,w) :
                    pic.setPixelColor(x,y,pic2.getPixelRed(x-(w-scroll),y),pic2.getPixelGreen(x-(w-scroll),y),pic2.getPixelBlue(x-(w-scroll),y))
            
            flag = False
        except IndexError:
            print "Please enter a number within your image's width"
        except :
            print "Unknown error please try again." 

def negat(w,h,pic,pic2) :
    
    copy(w,h,pic,pic2)
    for y in range (0,h) :
        for x in range (0,w) :
            pic2.setPixelColor(x,y,abs(pic.getPixelRed(x,y)-255),abs(pic.getPixelGreen(x,y)-255),abs(pic.getPixelBlue(x,y)-255))
    copy(w,h,pic2,pic)
    
def grayscale(w,h,pic,pic2) :
    
    copy(w,h,pic,pic2)
    for y in range (0,h) :
        for x in range (0,w) :
            avg = (pic.getPixelRed(x,y)+pic.getPixelGreen(x,y)+pic.getPixelBlue(x,y))/3
            pic2.setPixelColor(x,y,avg,avg,avg)
    copy(w,h,pic2,pic)

def cycle(w,h,pic,pic2) :
    
    copy(w,h,pic,pic2)
    for y in range (0,h) :
        for x in range (0,w) :
            r,g,b = pic.getPixelBlue(x,y), pic.getPixelRed(x,y), pic.getPixelGreen(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    copy(w,h,pic2,pic)

def zoom(w,h,pic,pic2) :
    
    for y in range (0,h-(h//2)) :
        for x in range (0,w-(w//2)) :
            pic2.setPixelColor(x,y,pic.getPixelRed(x+(w//4),y+(h//4)),pic.getPixelGreen(x+(w//4),y+(h//4)),pic.getPixelBlue(x+(w//4),y+(h//4)))
            
    
    for y in range (0,h//2) :
        for x in range (0,w//2) :
            pic.setPixelColor((x*2),(y*2),pic2.getPixelRed(x,y),pic2.getPixelGreen(x,y),pic2.getPixelBlue(x,y))
            pic.setPixelColor((x*2)+1,(y*2),pic2.getPixelRed(x,y),pic2.getPixelGreen(x,y),pic2.getPixelBlue(x,y))
        for x in range (0,w//2) :
            pic.setPixelColor((x*2),(y*2)+1,pic2.getPixelRed(x,y),pic2.getPixelGreen(x,y),pic2.getPixelBlue(x,y))
            pic.setPixelColor((x*2)+1,(y*2)+1,pic2.getPixelRed(x,y),pic2.getPixelGreen(x,y),pic2.getPixelBlue(x,y))

def poster(w,h,pic,pic2) :
    
    copy(w,h,pic,pic2)
    for y in range (0,h) :
        for x in range (0,w) :
            r = round(pic.getPixelRed(x,y)/32)*32
            g = round(pic.getPixelGreen(x,y)/32)*32
            b = round(pic.getPixelBlue(x,y)/32)*32
            pic2.setPixelColor(x,y,int(r),int(g),int(b))
    copy(w,h,pic2,pic)

def bright(w,h,pic,pic2) :
    
    flag = True
    
    while flag == True: 
        try: 
            brightDif = eval(raw_input("Please enter the difference in brightness you'd like using an integer.(Negative values will decrease brightness and values larger than 255 or -255 will result in white and black images respectively):"))
            
            copy(w,h,pic,pic2)
            for y in range (0,h) :
                for x in range (0,w) :
                    r = pic.getPixelRed(x,y)+brightDif
                    g = pic.getPixelGreen(x,y)+brightDif
                    b = pic.getPixelBlue(x,y)+brightDif
                    
                    if r < 0:
                        r = 0
                    if g < 0:
                        g = 0
                    if b < 0:
                        b = 0
                    if r > 255:
                        r = 255
                    if g > 255:
                        g = 255
                    if b > 255:
                        b = 255          
                    
                    pic2.setPixelColor(x,y,r,g,b)
        
            copy(w,h,pic2,pic)
            flag = False 
        except NameError:
            print "Please enter a number"

def contrast(w,h,pic,pic2) :
    
    copy(w,h,pic,pic2)
    for y in range (0,h) :
        for x in range (0,w) :
            r = contrcalc(pic.getPixelRed(x,y))
            g = contrcalc(pic.getPixelGreen(x,y))
            b = contrcalc(pic.getPixelBlue(x,y))
            
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255          
            
            pic2.setPixelColor(x,y,r,g,b)

    copy(w,h,pic2,pic)
    
def contrcalc(x) :
    
    dif = x - 128
    dif = dif * 2
    return(128+dif)

def blur(w,h,pic,pic2) :
    
    copy(w,h,pic,pic2)
    for y in range (0,h) :
        for x in range (0,w):
            counter = 1
            r = pic2.getPixelRed(x,y)
            g = pic2.getPixelGreen(x,y)
            b = pic2.getPixelBlue(x,y)
            
            for i in range (y-1,y+2):
                if i >= 0 and i < h:
                    for j in range (x-1,x+2) :
                        if j >= 0 and j < w:
                            r = r + pic2.getPixelRed(j,i)
                            g = g + pic2.getPixelGreen(j,i)
                            b = b + pic2.getPixelBlue(j,i)
                            counter = counter+1
            
            pic.setPixelColor(x,y,r/counter,g/counter,b/counter)
            

    
    
    
    
main()