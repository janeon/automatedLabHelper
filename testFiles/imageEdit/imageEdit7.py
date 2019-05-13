






import picture2
import math




def editOptions(Origpic) : 
    done = 0
    pic1, h, w = picCopy(Origpic)
    try:    
        while done == 0 :     
            print "There are many editing options, please choose one of the following:"
            print "1 for Flip Horizontally"
            print "2 for Mirror Horizontally"
            print "3 for Scroll Horizontally"
            print "4 for Make Negative"
            print "5 for Make Grayscale"
            print "6 for Cycle Color Channels"
            print "7 for Zoom"
            print "8 for Posterize"
            print "9 for Change Brightness"
            print "10 for Increase Contrast"
            print "11 for Blur"
            print "12 Rotate 180 Degrees"
            print "13 for dots"
            print "14 for Fade"
            inpu = eval(raw_input("Editing option number: " ))
            
            if inpu == 1 :
                flip(pic1, h, w)
                
            if inpu == 2 :
                mirror(pic1, h, w)
                
            if inpu == 3 :
                scroll(pic1, h, w)
            
            if inpu == 4 :
                negative(pic1, h, w)
            
            if inpu == 5 :
                grayscale(pic1, h, w)
            
            if inpu == 6 :
                cycle(pic1, h, w)
            
            if inpu == 7 :
                zoom(pic1, h, w)
            
            if inpu == 8 :
                poster(pic1, h, w)
            
            if inpu == 9 :
                bright(pic1, h, w)
            
            if inpu == 10 :
                contrast(pic1, h, w)
            
            if inpu == 11:
                blur(pic1, h, w)
            
            if inpu == 12:
                rotate(pic1, h, w)
                
            if inpu == 13 :
                dots(pic1, h, w)
                
            if inpu == 14 :
                cool(pic1, h, w)
                
            
            ans = raw_input("Would you like to conintue editing this picture? (yes or no) : " )
            answ = ans.lstrip() 
            answr = answ.lower() 
            if str(answr[0]) == "y":
                done = 0
            else:
                done = done +10
                print "Hope you have enjoyed yourself!"
    except IndexError :
        print ""
        print "Oops. I don't think you answered the question correctly."
    except SyntaxError :
        print ""
        print "Oops. Make sure you are entering a number."
    except NameError:
        print ""
        print "Oops. Make sure you are entering a number."

def cool(pic1, h, w):
    pic11, h, w = picCopy(pic1)
    for x in range(w-1):
        for y in range(h-1):
            r, g, b = pic11.getPixelColor(x, y)
            r, g, b = staybetween(r, g, b)
            pic1.setPixelColor(x, y, r+(x//10)*8, g +(x//30)*8, b + (x//30)*8)
       
    for y in range(h-1):
        for x in range(w-1):
            r, g, b = pic11.getPixelColor(x, y)
            r, g, b = staybetween(r, g, b)
            pic1.setPixelColor(x, y, r+(y//10)*8, g +(y//30)*8, b + (y//30)*8)
       
    pic1.display()







def rotate(pic1, h, w):
    rocopy, h, w = picCopy(pic1)
    for x in range(w-1):
        for y in range(h-1):
            r, g, b = rocopy.getPixelColor(x, y)
            pic1.setPixelColor(x, h-y-1, r, g, b)
    pic1.display()





def blur(pic1, h, w):
    blurcopy, h, w = picCopy(pic1)
    for y in range(1, h-2):
        for x in range(1, w-2):
            r, g, b = blurcopy.getPixelColor(x-1, y-1)
            a, c, d = blurcopy.getPixelColor(x, y-1)
            e, f, g = blurcopy.getPixelColor(x+1, y-1)
            i, j, k =blurcopy.getPixelColor(x-1, y)
            l, m, n =blurcopy.getPixelColor(x-1, y+1)
            o, p, q =blurcopy.getPixelColor(x+1, y)
            s, t, u =blurcopy.getPixelColor(x, y+1)
            v, wo, z =blurcopy.getPixelColor(x+1, y+1)
            red = (r+a+e+i+l+o+s+v)//8
            green = (g+c+f+j+m+p+t+wo)//8
            blue = (b+d+g+k+n+q+u+z)//8
            pic1.setPixelColor(x, y, red, green, blue)
    pic1.display()




def contrast(pic1, h, w):
    for y in range(h-1):
        for x in range(w-1):
            r, g, b = pic1.getPixelColor(x, y)
            r = r+(r-128)*2
            g = g+(g-128)*2
            b = b+(b-128)*2
            r, g, b = staybetween(r, g, b)
            pic1.setPixelColor(x, y, r, g, b)
    pic1.display()





def bright(pic1, h, w):
    change = eval(raw_input("How much would you like to change the brightness(positive or negative integer)?: " ))
    for y in range(h-1):
        for x in range(w-1):
            r, g, b = pic1.getPixelColor(x, y)
            r = r+change
            g = g+change
            b = b+change
            r, g, b = staybetween(r, g, b)
            pic1.setPixelColor(x, y, r, g, b)
    pic1.display()
            
def staybetween(r, g, b):
    
    if r>255 :
        r = 255
    if g >255:
        g = 255
    if b >255 :
        b = 255
    if r<0:
        r =0
    if g <0:
        g = 0
    if b <0:
        b = 0
    else:
        r = r
        g = g
        b = b
    return r, g, b    


def poster(pic1, h, w):
    for y in range(h-1):
        for x in range(w-1):
            r, g, b = pic1.getPixelColor(x,y)
            if (r%32) >= 16 :
                r = r + (r%32)
            if r%32 < 16:
                r = r -(r%32)
            if g%32 >= 16 :
                g = g + (g%32)
            if g%32 < 16 :
                g = g-(g%32)
            if b%32 >= 16 :
                b= b + (b%32)
            if b%32 < 16:
                b = b - (b%32)
            pic1.setPixelColor(x, y, r, g, b)
    
    pic1. display()



def zoom(pic1, h, w):
    zoomcopy, h, w = picCopy(pic1)
    for y in range(h-1):
        for x in range(w-1):
            r, g, b = zoomcopy.getPixelColor((w//4 + x//2), (h//4 + y//2))
            pic1.setPixelColor(x, y, r, g, b)
    pic1.display()

    
    
    
def dots(pic1, h, w):
    dotspic, h, w = picCopy(pic1)
    for i in range(h-1):
        for j in range(w-1):
            pic1.setPixelColor(j, i, 205, 197, 191)

    for y in range(0, h-1, 2):
        for x in range(0, w-1, 2):
            r, g, b = dotspic.getPixelColor(x, y)
            pic1.setPixelColor(x, y, r, g, b)

    
    
    pic1.display()

            
            
            

def cycle(pic1, h, w):
    for y in range(h-1):
        for x in range(w-1):
            r, g, b = pic1.getPixelColor(x, y )
            pic1.setPixelColor(x,y, b, r, g)
    pic1.display()



def grayscale(pic1, h, w) :
    for y in range(h-1):
        for x in range(w-1) :
            r, g, b = pic1.getPixelColor(x, y)
            color = ((r+b+g)/3)
            pic1.setPixelColor(x, y, color, color, color)
    pic1.display()

    
    

def negative(pic1, h, w) :
    for y in range(h-1) :
        for x in range(w-1) :
            r, g, b = pic1.getPixelColor(x, y)
            pic1.setPixelColor(x, y, 255-r, 255-g, 255-b)
    pic1.display()



def scroll(pic1, h, w) :
    distance = eval(raw_input("By how many pixels would you like to shift your image?: "))
    scrollcopy, h, w = picCopy(pic1)
    for y in range(h-1):
        for x in range(w-1):
            if x > distance:   
                r, g, b = scrollcopy.getPixelColor(x, y)
                pic1.setPixelColor(x-distance, y, r, g, b)
            else:
                r, g, b = scrollcopy.getPixelColor(x, y)
                pic1.setPixelColor(w-x-1, y, r, g, b)
                
    pic1.display()



def flip(pic1, h, w) :
    flipcopy, h, w = picCopy(pic1)
    
    for y in range(h-1):
        for x in range(w/2):
            r, g, b = pic1.getPixelColor(w-1-x, y)
            pic1.setPixelColor(x, y, r, g, b)
    for y in range(h-1) :
        for x in range(w/2):
            r, g, b = flipcopy.getPixelColor(x, y)
            pic1.setPixelColor(w-1-x, y, r, g, b)
            
            
    pic1.display()

        

def mirror(pic1, h, w) :

    for y in range(h-1):
        for x in range(w-1):
            r, g, b = pic1.getPixelColor(x, y)
            pic1.setPixelColor(w-1-x, y, r, g, b)
    pic1.display()



def picCopy(Origpic):
    h = Origpic.getHeight()
    w = Origpic.getWidth()
    pitcha = picture2.Picture(w, h)
    for y in range(0, h-1):
        for x in range(0, w-1):            
            r, g, b = Origpic.getPixelColor(x, y)
            pitcha.setPixelColor(x, y, r, g, b)
    return pitcha, h, w


    
    
def Origpic() : 
    try:    
        print "Welcome to my picture editing program!" 
        filename = raw_input("Please enter the filename for the image you would like to edit (.bmp): " )
        Origpic = picture2.Picture(filename)
        Origpic.display()
        print()
        print "This is the image you have selected."
        editOptions(Origpic) 
    except IOError :
        print "I'm sorry we couldn't find that file"

Origpic()
    
