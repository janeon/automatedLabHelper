





import picture2

def printtable():
    print"Listed below are your options for operations."
    print"1. Flip Horizontally"
    print"2. Mirror Horizontally"
    print"3. Scroll Horizontally"
    print"4. Make Negative"
    print"5. Make Grayscale"
    print"6. Cycle Color Channels"
    print"7. Zoom"
    print"8. Posterize"
    print"9. Change Brightness"
    print"10. Increase Contrast"
    print"11. Blur"
    print"12. Rotate 180 degrees"
    print"13. Make Pink"
    print"14. Bleed"

def picCopy(pic):
    
    w=pic.getWidth()
    h=pic.getHeight()
    
    pic2=picture2.Picture(w, h)
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic.getPixelColor(x,y)
            pic2.setPixelColor(x,y,r,g,b)
    

    return pic2
    input()
    pic2.display()


def fliphorizontally(pic):







    w=pic.getWidth()
    h=pic.getHeight()
    pic2= picCopy(pic)
    
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic2.getPixelColor(x, y)
            pic.setPixelColor(w-x-1, y, r, g, b)
            
    pic.display()
    

    

    
def mirrorhorizontally(pic):




    w=pic.getWidth()
    h=pic.getHeight()
    
    for x in range(0, w/2):
        for y in range(0, h):
            for i in range (0, x):
                r, g, b= pic.getPixelColor(w/2-i,y)
                pic.setPixelColor(w/2+i, y, r, g, b)
            
    pic.display()
    return pic



def scrollhorizontally(pic):




    
        
        
    
    scroll=eval(raw_input("How many pixels would you like to scroll? "))
    
    
    w=pic.getWidth()
    h=pic.getHeight()
    pic2= picCopy(pic)
    
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic2.getPixelColor(x, y)
            
            pic.setPixelColor((x+scroll)%w, y, r, g, b)
            
    pic.display()
    return pic



def makenegative(pic):






    w=pic.getWidth()
    h=pic.getHeight()
    
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, 255-r, 255-g, 255-b)
    
    pic.display()
    return pic


    
def makegrayscale(pic):




    

    
    w=pic.getWidth()
    h=pic.getHeight()
    
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic.getPixelColor(x, y)
            average= (r + g + b)/3
            pic.setPixelColor(x, y, average, average, average)
    
    pic.display()        
    return pic


def cyclecolorchannels(pic):


    
    w=pic.getWidth()
    h=pic.getHeight()
    
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic.getPixelColor(x, y)
            pic.setPixelColor(x, y, b, r, g)
    
    pic.display()
    return pic


def zoom(pic):
    
    w=pic.getWidth()
    h=pic.getHeight()
    pic2= picCopy(pic)
    
    for i in range(w):
        for j in range(h):
            r, g, b= pic2.getPixelColor(w/4+i//2, h/4+j//2)
            pic.setPixelColor(i, j, r, g, b)


                        
    pic.display()
    return pic


            
def posterize(pic):



    w=pic.getWidth()
    h=pic.getHeight()

    for x in range(0,w):
        for y in range(0,h):
            r, g, b= pic.getPixelColor(x, y)
            r= (r//32)*32
            g= (g//32)*32
            b= (b//32)*32
            pic.setPixelColor(x, y, r, g, b)
            
    pic.display()
    return pic
            

def changebrightness(pic):
    change=eval(raw_input("Enter an integer indicating how much you would like to change the brightness: "))
    
    w=pic.getWidth()
    h=pic.getHeight()

    for x in range(0,w):
        for y in range(0,h):
            r, g, b= pic.getPixelColor(x, y)
            r=r+change
            g=g+change
            b=b+change
            
            if r >255:
                    r=255
            if r < 0:
                    r=0
            if g >255:
                    g=255
            if g < 0:
                    g=0
            if b >255:
                    b=255
            if b < 0:
                    b=0
            
            pic.setPixelColor(x, y, r, g, b)
    
    pic.display()
    return pic



def contrast(pic):
    

    w=pic.getWidth()
    h=pic.getHeight()

    for x in range(0,w):
        for y in range(0,h):
            r, g, b= pic.getPixelColor(x, y)
            r= 2*(r-128) +128
            g= 2*(g-128) +128
            b= 2*(b-128) +128
            
            if r >255:
                r=255
            if r < 0:
                r=0
            if g >255:
                g=255
            if g < 0:
                g=0
            if b >255:
                b=255
            if b < 0:
                b=0
            
            pic.setPixelColor(x, y, r, g, b)
            
    pic.display()
    return pic



def blur(pic):

    w=pic.getWidth()
    h=pic.getHeight()
    pic2= picCopy(pic)
    
    rSum=0
    gSum=0
    bSum=0
    
    for x in range(1, w-1):
        for y in range(1, h-1):
            r1, g1, b1= pic2.getPixelColor(x, y)
            r2, g2, b2= pic2.getPixelColor(x+1, y)
            r3, g3, b3= pic2.getPixelColor(x-1, y)
            r4, g4, b4= pic2.getPixelColor(x, y+1)
            r5, g5, b5= pic2.getPixelColor(x+1, y+1)
            r6, g6, b6= pic2.getPixelColor(x-1, y+1)
            r7, g7, b7= pic2.getPixelColor(x, y-1)
            r8, g8, b8= pic2.getPixelColor(x+1, y-1)
            r9, g9, b9= pic2.getPixelColor(x-1, y-1)
            
            rSum=r1+r2+r3+r4+r5+r6+r7+r8+r9
            gSum=g1+g2+g3+g4+g5+g6+g7+g8+g9
            bSum=b1+b2+b3+b4+b5+b6+b7+b8+b9
            
            rAvg=rSum/9
            gAvg=gSum/9
            bAvg=bSum/9
    
            pic.setPixelColor(x, y, rAvg, gAvg, bAvg)
                    
    pic.display()

    
    return pic



          
def rotate(pic):
    

    
    w=pic.getWidth()
    h=pic.getHeight()
    pic2= picCopy(pic)

    
    for x in range(0, w):
        for y in range(0, h):
            r, g, b= pic2.getPixelColor(x, y)
            pic.setPixelColor(w-x-1, h-y-1, r, g, b)
            
    pic.display()




def pink(pic):

    w=pic.getWidth()
    h=pic.getHeight()

    for x in range(0,w):
        for y in range(0,h):
            r, g, b= pic.getPixelColor(x, y)
            average= (r + g + b)/3
            pic.setPixelColor(x, y, average, 30, 144)
            
    pic.display()

    


def bleed(pic):
    

    w=pic.getWidth()
    h=pic.getHeight()

    for x in range(0,w):
        for y in range(0,h):
            r, g, b= pic.getPixelColor(x, y)
            average= (r + g + b)/3
            if r < 150:
                pic.setPixelColor(x, y, average, 0, 0)
    
    pic.display()

    

                
    
def main():
    print"Welcome to the amazing image editor!"
    
    goodInput= False
    while not goodInput:
        try:
            n=raw_input("Enter the filename of the image you would like to edit: ")
            pic=picture2.Picture(n)
            goodInput=True
        
        except:
            print("You made a mistake entering the file name. Please try again.")            
    
    
    printtable()
    print("Hit Enter to quit.")
    operation=input("Enter the number corresponding to which operation you'd like to perform: ")

    
    
    try:
        while operation != "":
                
            if operation == 1:
                fliphorizontally(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")

            elif operation == 2:
                mirrorhorizontally(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 3:
                scrollhorizontally(pic)
                printtable()
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 4:
                makenegative(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 5:
                makegrayscale(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 6:
                cyclecolorchannels(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 7:
                zoom(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 8:
                posterize(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 9:
                changebrightness(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 10:
                contrast(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 11:
                blur(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation== 12:
                rotate(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation== 13:
                pink(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
            elif operation == 14:
                bleed(pic)
                printtable()
                print("Hit Enter to quit.")
                operation=input("Enter the number corresponding which operation you'd like to perform: ")
                
    except SyntaxError:
        print("Thanks for using the amazing image editor!")
          
    
        
main()