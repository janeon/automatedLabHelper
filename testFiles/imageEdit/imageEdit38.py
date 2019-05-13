






def main() :
    import picture2
    
    

    def picCopy() : 
        for x in range(0,w-1) :
            for y in range(0,h-1) :
                r=pic.getPixelRed(x,y)
                g=pic.getPixelGreen(x,y)
                b=pic.getPixelBlue(x,y)
                pic2.setPixelColor(x,y,r,g,b)
    
    def picFlip() : 
        for x in range(0,w-1) :
            for y in range(0,h-1) :
                r=pic2.getPixelRed(w-(x+1),y)
                g=pic2.getPixelGreen(w-(x+1),y)
                b=pic2.getPixelBlue(w-(x+1),y)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
    
    def picMirror() : 
        for x in range(w/2,w-1) :
            for y in range(0,h-1) :
                r=pic2.getPixelRed(w-(x+1),y)
                g=pic2.getPixelGreen(w-(x+1),y)
                b=pic2.getPixelBlue(w-(x+1),y)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()

        
                
    def picScroll() : 
        d=eval(raw_input("Please specify the number of pixels you would like the image scrolled to the right: "))
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                g=pic2.getPixelGreen(x,y)
                b=pic2.getPixelBlue(x,y)
                if w<=x+d :
                    nx=(x+d)%w
                else :
                    nx=x+d
                pic.setPixelColor(nx,y,r,g,b)
        pic.display()
    
    def picNeg() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                g=pic2.getPixelGreen(x,y)
                b=pic2.getPixelBlue(x,y)
                pic.setPixelColor(x,y,255-r,255-g,255-b)          
        pic.display()
    
    def picGreyscale() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                g=pic2.getPixelGreen(x,y)
                b=pic2.getPixelBlue(x,y)
                c=(r+g+b)/3
                pic.setPixelColor(x,y,c,c,c)
        pic.display()
    
    def picColorCycle() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                g=pic2.getPixelGreen(x,y)
                b=pic2.getPixelBlue(x,y)
                pic.setPixelColor(x,y,b,r,g)
        pic.display()
    
    def picZoom() : 
        for y in range(0,h-1) :
            if y==0 :
                ny=.25*h
            else :
                ny=(.25*h)+y*.5
            for x in range(0,w-1) :
                if x==0 :
                    nx=.25*w
                else :
                    nx=(.25*w)+x*.5
                r=pic2.getPixelRed(nx,ny)
                g=pic2.getPixelGreen(nx,ny)
                b=pic2.getPixelBlue(nx,ny)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
    def picPoster() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                r=nearMult(r)
                g=pic2.getPixelGreen(x,y)
                g=nearMult(g)
                b=pic2.getPixelBlue(x,y)
                b=nearMult(b)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
    
    def nearMult(c) : 
        n=32
        s=c//n
        j=c%n
        if j>=n/2 :
            j=1
        else :
            j=0
        c=n*(s+j)
        return c
    
    def picBright() : 
        bright=eval(raw_input("Please enter the desired change in brightness: "))
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                r=r+bright
                r=colorLimit(r)
                g=pic2.getPixelGreen(x,y)
                g=g+bright
                g=colorLimit(g)
                b=pic2.getPixelBlue(x,y)
                b=b+bright
                b=colorLimit(b)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
  
    def picContrast() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(x,y)
                r=128+(r-128)*2
                r=colorLimit(r)
                g=pic2.getPixelGreen(x,y)
                g=128+(g-128)*2
                g=colorLimit(g)
                b=pic2.getPixelBlue(x,y)
                b=128+(b-128)*2
                b=colorLimit(b)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
          
    def colorLimit(c) : 
        if c>255 :
            c=255
        elif c<0 :
            c=0
        return c
   
    def avgRedPixel(x,y) : 
        c=pic2.getPixelRed(x, y)
        if x+y==0 :
            c=c+pic2.getPixelRed(x, y+1)+pic2.getPixelRed(x+1, y+1)+pic2.getPixelRed(x+1, y)
            c=c/4
            return c
        elif x==0:
            c=c+pic2.getPixelRed(x, y+1)+pic2.getPixelRed(x+1, y+1)+pic2.getPixelRed(x+1, y)+pic2.getPixelRed(x+1, y-1)+pic2.getPixelRed(x, y-1)
            c=c/6
            return c
        elif y==0 :
            c=c+pic2.getPixelRed(x-1, y)+pic2.getPixelRed(x-1, y+1)+pic2.getPixelRed(x, y+1)+pic2.getPixelRed(x+1, y+1)+pic2.getPixelRed(x+1, y)
            c=c/6
            return c
        elif x+y==2*w :
            c=c+pic2.getPixelRed(x-1, y-1)+pic2.getPixelRed(x-1, y)+pic2.getPixelRed(x,y-1)
            c=c/4
            return c
        elif x==w :
            c=c+pic2.getPixelRed(x-1, y-1)+pic2.getPixelRed(x-1, y)+pic2.getPixelRed(x-1, y+1)+pic2.getPixelRed(x, y+1)+pic2.getPixelRed(x, y-1)
            c=c/6
            return c
        elif y==h :
            c=c+pic2.getPixelRed(x-1, y-1)+pic2.getPixelRed(x-1, y)+pic2.getPixelRed(x+1, y)+pic2.getPixelRed(x+1, y-1)+pic2.getPixelRed(x, y-1)
            c=c/6
            return c
        else :
            c=c+pic2.getPixelRed(x-1, y-1)+pic2.getPixelRed(x-1, y)+pic2.getPixelRed(x-1, y+1)+pic2.getPixelRed(x, y+1)+pic2.getPixelRed(x+1, y+1)+pic2.getPixelRed(x+1, y)+pic2.getPixelRed(x+1,y-1)+pic2.getPixelRed(x,y-1)
            c=c/9
            return c
        
    def avgGreenPixel(x,y) : 
        c=pic2.getPixelGreen(x, y)
        if x+y==0 :
            c=c+pic2.getPixelGreen(x, y+1)+pic2.getPixelGreen(x+1, y+1)+pic2.getPixelGreen(x+1, y)
            c=c/4
            return c
        elif x==0:
            c=c+pic2.getPixelGreen(x, y+1)+pic2.getPixelGreen(x+1, y+1)+pic2.getPixelGreen(x+1, y)+pic2.getPixelGreen(x+1, y-1)+pic2.getPixelGreen(x, y-1)
            c=c/6
            return c
        elif y==0 :
            c=c+pic2.getPixelGreen(x-1, y)+pic2.getPixelGreen(x-1, y+1)+pic2.getPixelGreen(x, y+1)+pic2.getPixelGreen(x+1, y+1)+pic2.getPixelGreen(x+1, y)
            c=c/6
            return c
        elif x+y==2*w :
            c=c+pic2.getPixelGreen(x-1, y-1)+pic2.getPixelGreen(x-1, y)+pic2.getPixelGreen(x,y-1)
            c=c/4
            return c
        elif x==w :
            c=c+pic2.getPixelGreen(x-1, y-1)+pic2.getPixelGreen(x-1, y)+pic2.getPixelGreen(x-1, y+1)+pic2.getPixelGreen(x, y+1)+pic2.getPixelGreen(x, y-1)
            c=c/6
            return c
        elif y==h :
            c=c+pic2.getPixelGreen(x-1, y-1)+pic2.getPixelGreen(x-1, y)+pic2.getPixelGreen(x+1, y)+pic2.getPixelGreen(x+1, y-1)+pic2.getPixelGreen(x, y-1)
            c=c/6
            return c
        else :
            c=c+pic2.getPixelGreen(x-1, y-1)+pic2.getPixelGreen(x-1, y)+pic2.getPixelGreen(x-1, y+1)+pic2.getPixelGreen(x, y+1)+pic2.getPixelGreen(x+1, y+1)+pic2.getPixelGreen(x+1, y)+pic2.getPixelGreen(x+1,y-1)+pic2.getPixelGreen(x,y-1)
            c=c/9
            return c
            
    
    def avgBluePixel(x,y) : 
        c=pic2.getPixelBlue(x, y)
        if x+y==0 :
            c=c+pic2.getPixelBlue(x, y+1)+pic2.getPixelBlue(x+1, y+1)+pic2.getPixelBlue(x+1, y)
            c=c/4
            return c
        elif x==0:
            c=c+pic2.getPixelBlue(x, y+1)+pic2.getPixelBlue(x+1, y+1)+pic2.getPixelBlue(x+1, y)+pic2.getPixelBlue(x+1, y-1)+pic2.getPixelBlue(x, y-1)
            c=c/6
            return c
        elif y==0 :
            c=c+pic2.getPixelBlue(x-1, y)+pic2.getPixelBlue(x-1, y+1)+pic2.getPixelBlue(x, y+1)+pic2.getPixelBlue(x+1, y+1)+pic2.getPixelBlue(x+1, y)
            c=c/6
            return c
        elif x+y==2*w :
            c=c+pic2.getPixelBlue(x-1, y-1)+pic2.getPixelBlue(x-1, y)+pic2.getPixelBlue(x,y-1)
            c=c/4
            return c
        elif x==w :
            c=c+pic2.getPixelBlue(x-1, y-1)+pic2.getPixelBlue(x-1, y)+pic2.getPixelBlue(x-1, y+1)+pic2.getPixelBlue(x, y+1)+pic2.getPixelBlue(x, y-1)
            c=c/6
            return c
        elif y==h :
            c=c+pic2.getPixelBlue(x-1, y-1)+pic2.getPixelBlue(x-1, y)+pic2.getPixelBlue(x+1, y)+pic2.getPixelBlue(x+1, y-1)+pic2.getPixelBlue(x, y-1)
            c=c/6
            return c
        else :
            c=c+pic2.getPixelBlue(x-1, y-1)+pic2.getPixelBlue(x-1, y)+pic2.getPixelBlue(x-1, y+1)+pic2.getPixelBlue(x, y+1)+pic2.getPixelBlue(x+1, y+1)+pic2.getPixelBlue(x+1, y)+pic2.getPixelBlue(x+1,y-1)+pic2.getPixelBlue(x,y-1)
            c=c/9
            return c
    
   
    def picBlur() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=avgRedPixel(x,y)
                g=avgGreenPixel(x,y)
                b=avgBluePixel(x,y)
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
    
    def picRotate() : 
        for y in range(0,h-1) :
            for x in range(0,w-1) :
                r=pic2.getPixelRed(w-(x+1),h-(y+1))
                g=pic2.getPixelGreen(w-(x+1),h-(y+1))
                b=pic2.getPixelBlue(w-(x+1),h-(y+1))
                pic.setPixelColor(x,y,r,g,b)
        pic.display()
    
    def picStripe(): 
        for x in range(0,w-1) :
            for y in range(0,h-1) :
                if x%2==0 :
                    r=pic2.getPixelRed(x,y)
                    g=pic2.getPixelGreen(x,y)
                    b=pic2.getPixelBlue(x,y)
                    pic.setPixelColor(x,y,r,g,b)
                else :
                    r=pic2.getPixelRed(x,y)
                    g=pic2.getPixelGreen(x,y)
                    b=pic2.getPixelBlue(x,y)
                    c=(r+g+b)/3
                    pic.setPixelColor(x,y,c,c,c)
        pic.display()
    
    def picHmm() : 
        for x in range(0,w-1) :
            for y in range(0,h-1) :
                if x%3==0 :
                    r=pic2.getPixelRed(x,y)
                    g=pic2.getPixelGreen(x,y)
                    b=pic2.getPixelBlue(x,y)
                    pic.setPixelColor(x,y,r,g,b)
                elif x%2==0 :
                    r=pic2.getPixelRed(w-(x+1),h-(y+1))
                    g=pic2.getPixelGreen(w-(x+1),h-(y+1))
                    b=pic2.getPixelBlue(w-(x+1),h-(y+1))
                    pic.setPixelColor(x,y,r,g,b)
                else :
                    r=pic2.getPixelRed(w-(x+1),y)
                    g=pic2.getPixelGreen(w-(x+1),y)
                    b=pic2.getPixelBlue(w-(x+1),y)
                    pic.setPixelColor(x,y,r,g,b)
        pic.display()
     
    def picRed() :
        for x in range(0,w-1) :
            for y in range(0,h-1) :
                r=pic2.getPixelRed(x,y)
                g=pic2.getPixelGreen(x,y)
                b=pic2.getPixelBlue(x,y)
                pic.setPixelColor(x,y,r,g/1000,b/1000)
        pic.display()
   
    
    print ("Hi and welcome to my fantastic image editor!")
    goodInput=False
    while not goodInput:
        try:
            pic=raw_input ("Please upload the image (with filetype .bmp) you wish to edit: ")
            pic = picture2.Picture(pic)
            goodInput=True
            w = pic.getWidth()
            h= pic.getHeight()
            pic2=picture2.Picture(w,h)
            END=False
            while not END :    
                try :
                    picCopy()
                    pic.display()
                    print("Available Operations:")
                    print("1. Flip Horizontally")
                    print("2. Mirror Horizontally")
                    print("3. Scroll Horizontally")
                    print("4. Make Negative")
                    print("5. Make Grayscale")
                    print("6. Cycle Color Channels")
                    print("7. Zoom ")
                    print("8. Posterize")
                    print("9. Change Brightness")
                    print("10. Increase Contrast")
                    print("11. Blur")
                    print("12. Rotate 180 Degrees")
                    print("13. Mute Colors")
                    print("14. Make a Mess of Things")
                    print("15. Redden")
                    operation=0
                    operation=eval(raw_input("Enter the number of the desired operation: "))
                    if operation==1 :
                        picFlip()
                    elif operation==2 :
                        picMirror()
                    elif operation==3 :
                        picScroll()
                    elif operation==4 :
                        picNeg()
                    elif operation==5 :
                        picGreyscale()
                    elif operation==6 :
                        picColorCycle()
                    elif operation==7 :
                        picZoom()
                    elif operation==8 :
                        picPoster()
                    elif operation==9 :
                        picBright()
                    elif operation==10 :
                        picContrast()
                    elif operation==11 :
                        picBlur()
                    elif operation==12 :
                        picRotate()
                    elif operation==13 :
                        picStripe()
                    elif operation==14 :
                        picHmm()
                    elif operation==15 :
                        picRed()
                except TypeError:
                    print("I'm sorry that isn't a valid operation")
                except NameError :
                    print("I'm sorry that isn't a valid operation")
                except SyntaxError :
                    print("I'm sorry that isn't a valid operation")
                    
        except IOError :
            print("I'm sorry that file does not exist.")
    input()
    
    
    
    








main()