




import picture2

def main():
    fileName = raw_input("Please enter the image file you'd like loaded: ")
    pic = picture2.Picture(fileName)
    h=pic.getHeight()
    w=pic.getWidth()
    zed=0
    while zed<1:
        print "The list of available processes is as follows:"
        print "1. Flip Horizontally"
        print "2. Mirror Horizontally"
        print "3. Scroll Horizontally"
        print "4. Make Negative"
        print "5. Make Grayscale"
        print "6. Cycle Color Channels"
        print "7. Zoom"
        print "8. Posterize"
        print "9. Change Brightness"
        print "10. Increase Contrast"
        print "11. Blur"
        print "12. Rotate 180 Degrees"
        print "13. Tint"
        print "15. Exit Program"
        process=input("Which process should it undergo? Please use the number, rather than the name: ")
        if process==1:
            flip(fileName,w,h)
        elif process==2:
            mirror(fileName,w,h)
        elif process==3:
            scroll(fileName,w,h)
        elif process==4:
            negative(fileName,w,h)
        elif process==5:
            grayscale(fileName,w,h)
        elif process==6:
            channels(fileName,w,h)
        elif process==7:
            zoom(fileName,w,h)
        elif process==8:
            posterize(fileName,w,h)
        elif process==9:
            brightness(fileName,w,h)
        elif process==10:
            contrast(fileName,w,h)
        elif process==11:
            blur(fileName,w,h)
        elif process==12:
            rotate(fileName,w,h)
        elif process==13:
            tint(fileName,w,h)
        elif process==15:
            zed=1
        else:
            print "HA! You messed up sucka!"

def flip(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w/2):
        for y in range(h-1):
            red=pic.getPixelRed(x,y)
            red2=pic.getPixelRed(w-x-1,y)
            pic2.setPixelRed(x,y,red2)
            pic2.setPixelRed(w-x-1,y,red)
            green=pic.getPixelGreen(x,y)
            green2=pic.getPixelGreen(w-x-1,y)
            pic2.setPixelGreen(x,y,green2)
            pic2.setPixelGreen(w-x-1,y,green)
            blue=pic.getPixelBlue(x,y)
            blue2=pic.getPixelBlue(w-x-1,y)
            pic2.setPixelBlue(x,y,blue2)
            pic2.setPixelBlue(w-x-1,y,blue)
    pic2.display()
    raw_input()
    
    
def mirror(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for y in range(h):
        for x in range(w/2):
            red=pic.getPixelRed(x,y)
            pic2.setPixelRed(x,y,red)
            pic2.setPixelRed(w-x-1,y,red)
            green=pic.getPixelGreen(x,y)
            pic2.setPixelGreen(x,y,green)
            pic2.setPixelGreen(w-x-1,y,green)
            blue=pic.getPixelBlue(x,y)
            pic2.setPixelBlue(x,y,blue)
            pic2.setPixelBlue(w-x-1,y,blue)
    pic2.display()
    raw_input()
    
def scroll(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    d=input("How many pixels to the right should the image be scrolled? ")
    for x in range(w):
        for y in range(h):
            if(x+d)<(w):
                red=pic.getPixelRed(x,y)
                pic2.setPixelRed(x+d,y,red)
                green=pic.getPixelGreen(x,y)
                pic2.setPixelGreen(x+d,y,green)
                blue=pic.getPixelBlue(x,y)
                pic2.setPixelBlue(x+d,y,blue)
            else:
                red=pic.getPixelRed(x,y)
                pic2.setPixelRed(x+d-w,y,red)
                green=pic.getPixelGreen(x,y)
                pic2.setPixelGreen(x+d-w,y,green)
                blue=pic.getPixelBlue(x,y)
                pic2.setPixelBlue(x+d-w,y,blue)
    pic2.display()
    raw_input()
    
def negative(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            pic2.setPixelRed(x,y,256-red)
            green=pic.getPixelGreen(x,y)
            pic2.setPixelGreen(x,y,256-green)
            blue=pic.getPixelBlue(x,y)
            pic2.setPixelBlue(x,y,256-blue)
    pic2.display()
    raw_input()
    
def grayscale(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            green=pic.getPixelGreen(x,y)
            blue=pic.getPixelBlue(x,y)
            grey=(red+blue+green)//3
            pic2.setPixelRed(x,y,grey)
            pic2.setPixelGreen(x,y,grey)
            pic2.setPixelBlue(x,y,grey)
    pic2.display()
    raw_input()

def channels(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            green=pic.getPixelGreen(x,y)
            blue=pic.getPixelBlue(x,y)
            pic2.setPixelRed(x,y,blue)
            pic2.setPixelBlue(x,y,green)
            pic2.setPixelGreen(x,y,red)
    pic2.display()
    raw_input()

def zoom(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    deg=input("By what factor should the image be zoomed in? ")
    
def posterize(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            green=pic.getPixelGreen(x,y)
            blue=pic.getPixelBlue(x,y)
            rc=red%32
            if rc<16:
                red=red-rc
            else:
                red=red-rc+32
            pic2.setPixelRed(x,y,red)
            bc=blue%32
            if bc<16:
                blue=blue-bc
            else:
                blue=blue-bc+32
            pic2.setPixelBlue(x,y,blue)
            gc=green%32
            if gc<16:
                green=green-gc
            else:
                green=green-gc+32
            pic2.setPixelGreen(x,y,green)
    pic2.display()
    raw_input()
    
def brightness(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    change=input("How much should the brightness be altered? Positive and negative integers are both valid. ")
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            pic2.setPixelRed(x,y,red+change)
            blue=pic.getPixelBlue(x,y)
            pic2.setPixelBlue(x,y,blue+change)
            green=pic.getPixelGreen(x,y)
            pic2.setPixelGreen(x,y,green+change)
            if red > 256:
                red=256
            if red < 0:
                red=0
            if blue>256:
                blue=256
            if blue<0:
                blue=0
            if green>256:
                green=256
            if green<0:
                green=0
    pic2.display()
    raw_input()
    
def contrast(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            if red==128:
                red=red
            else:
                dif=red-128
                red=red+(2*dif)
            green=pic.getPixelGreen(x,y)
            if green==128:
                green=green
            else:
                dif=green-128
                green=green+(2*dif)
            blue=pic.getPixelBlue(x,y)
            if blue==128:
                blue=blue
            else:
                dif=blue-128
                blue=blue+(2*dif)
            if red>255:
                red=255
            if red<0:
                red=0
            if blue>255:
                blue=255
            if blue<0:
                blue=0
            if green>255:
                green=255
            if green<0:
                green=0
            pic2.setPixelRed(x,y,red)
            pic2.setPixelGreen(x,y,green)
            pic2.setPixelBlue(x,y,blue)
    pic2.display()
    raw_input()

def blur(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            try:
                num=9
                red1=pic.getPixelRed(x,y)
                red2=pic.getPixelRed(x-1,y)
                red3=pic.getPixelRed(x-1,y-1)
                red4=pic.getPixelRed(x,y-1)
                red5=pic.getPixelRed(x+1,y)
                red6=pic.getPixelRed(x+1,y+1)
                red7=pic.getPixelRed(x,y+1)
                red8=pic.getPixelRed(x+1,y-1)
                red9=pic.getPixelRed(x-1,y-1)
                red=(red1+red2+red3+red4+red5+red6+red7+red8+red9)//num
                pic2.setPixelRed(x,y,red)
                num=9
                Green1=pic.getPixelGreen(x,y)
                Green2=pic.getPixelGreen(x-1,y)
                Green3=pic.getPixelGreen(x-1,y-1)
                Green4=pic.getPixelGreen(x,y-1)
                Green5=pic.getPixelGreen(x+1,y)
                Green6=pic.getPixelGreen(x+1,y+1)
                Green7=pic.getPixelGreen(x,y+1)
                Green8=pic.getPixelGreen(x+1,y-1)
                Green9=pic.getPixelGreen(x-1,y-1)
                Green=(Green1+Green2+Green3+Green4+Green5+Green6+Green7+Green8+Green9)//num
                pic2.setPixelGreen(x,y,Green)
                num=9
                Blue1=pic.getPixelBlue(x,y)
                Blue2=pic.getPixelBlue(x-1,y)
                Blue3=pic.getPixelBlue(x-1,y-1)
                Blue4=pic.getPixelBlue(x,y-1)
                Blue5=pic.getPixelBlue(x+1,y)
                Blue6=pic.getPixelBlue(x+1,y+1)
                Blue7=pic.getPixelBlue(x,y+1)
                Blue8=pic.getPixelBlue(x+1,y-1)
                Blue9=pic.getPixelBlue(x-1,y-1)
                Blue=(Blue1+Blue2+Blue3+Blue4+Blue5+Blue6+Blue7+Blue8+Blue9)//num
                pic2.setPixelBlue(x,y,Blue)
            except Exception as wrong:
                type(wrong)
                str(wrong)
    pic2.display()
    raw_input()
    

def rotate(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    for x in range(w):
        for y in range(h):
            red=pic.getPixelRed(x,y)
            pic2.setPixelRed(w-x-1,h-y-1,red)
            blue=pic.getPixelBlue(x,y)
            pic2.setPixelBlue(w-x-1,h-y-1,blue)
            green=pic.getPixelGreen(x,y)
            pic2.setPixelGreen(w-x-1,h-y-1,green)
    pic2.display()
    raw_input()

def tint(fileName,w,h):
    pic=picture2.Picture(fileName)
    pic2=picture2.Picture(w,h)
    print"1: Red"
    print"2: Green"
    print"3: Blue"
    color=input("Choose a color: ")
    if color==1:
       for x in range(w):
            for y in range(h):
                red=pic.getPixelRed(x,y)
                red=red+100
                if red>255:
                    red=255
                green=pic.getPixelGreen(x,y)
                blue=pic.getPixelBlue(x,y)
                pic2.setPixelRed(x,y,red)
                pic2.setPixelGreen(x,y,green)
                pic2.setPixelBlue(x,y,blue)
    if color==2:
        for x in range(w):
            for y in range(h):
                red=pic.getPixelRed(x,y)
                green=pic.getPixelGreen(x,y)
                green=green+100
                if green>255:
                    green=255
                blue=pic.getPixelBlue(x,y)
                pic2.setPixelRed(x,y,red)
                pic2.setPixelGreen(x,y,green)
                pic2.setPixelBlue(x,y,blue)
    if color==3:
        for x in range(w):
            for y in range(h):
                red=pic.getPixelRed(x,y)
                green=pic.getPixelGreen(x,y)
                blue=pic.getPixelBlue(x,y)
                blue=blue+100
                if blue>255:
                    blue=255
                pic2.setPixelRed(x,y,red)
                pic2.setPixelGreen(x,y,green)
                pic2.setPixelBlue(x,y,blue)
    pic2.display()
    raw_input()
    
    


    


    
    
main()