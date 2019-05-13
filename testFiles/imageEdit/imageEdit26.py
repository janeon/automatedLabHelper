





import picture2
import random

def copy(pic) :
    w=pic.getWidth()()
    h= pic.getHeight()()
    picCopy=picture2.Picture(w, h)
    for i in range (0, w) :
        for j in range (0, h) :
            r1,g1,b1= pic.getPixelColor(i,j)
            picCopy.setPixelColor(i,j,r1,g1,b1)
    return picCopy

def flip(pic, width, height) :
    for i in range (0, width/2) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            r2,g2,b2= pic.getPixelColor(width-i-1,j)
            pic.setPixelColor(i,j,r2,g2,b2)
            pic.setPixelColor(width-i-1,j,r1,g1,b1)
    return pic

def mirror(pic, width, height) :
    for i in range (0, width/2) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic.setPixelColor(width-i-1,j,r1,g1,b1)
    return pic

def scroll(pic, width, height) :
    shift=input("Enter a number of pixels to be scrolled: ")
    shift=shift%width
    pic2=copy(pic)
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            if i+shift < width :
                pic2.setPixelColor(i+shift,j,r1,g1,b1)
            else :
                pic2.setPixelColor((i+shift)-width,j,r1,g1,b1)
    return pic2

def negative(pic, width, height) :
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,255-r1,255-g1,255-b1)
    return pic

def gray(pic, width, height) :
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            avg=(r1+g1+b1)/3
            pic.setPixelColor(i,j,avg,avg,avg)
    return pic

def cycle(pic, width, height) :
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,b1,r1,g1)
    return pic

def zoom(pic, width, height) :
    pic2=copy(pic)
    for i in range (width/4, 3*width/4) :
        for j in range (height/4, 3*height/4) :
            r1,g1,b1= pic.getPixelColor(i,j)
            for k in range ((i-width/4)*2,(i-width/4)*2+2) :
                for l in range ((j-height/4)*2,(j-height/4)*2+2) :
                    pic2.setPixelColor(k,l,r1,g1,b1)
                
    return pic2

def posterize(pic, width, height) :
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,32*(r1//32),32*(g1//32),32*(b1//32))
    return pic

def brightness(pic, width, height) :
    change=input("Enter an integer for brightness change (positive or negative): ")
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,r1+change,g1+change,b1+change)
    return pic

def contrast(pic, width,height) :
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,(r1-128)*2+128,(g1-128)*2+128,(b1-128)*2+128)
    return pic

def blur(pic,width,height) :
    pic2=copy(pic)
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            try :
                for k in range (i-1, i+2) :
                    for l in range (j-1, j+2) :
                        rX,gX,bX= pic.getPixelColor(k,l)
                        r1,g1,b1=r1+rX,g1+gX,b1+bX
                r1,g1,b1= r1/9,g1/9,b1/9
                pic2.setPixelColor(i,j,r1,g1,b1)
            except IndexError :
                pic2.setPixelColor(i,j,r1,g1,b1)
    return pic2

def rotate(pic,width,height) :
    pic2=copy(pic)
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            pic2.setPixelColor(width-i-1,height-j-1,r1,g1,b1)
    return pic2

def tile(pic, width, height) :
    pic2=copy(pic)
    for i in range (0, width) :
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            for k in range (0,3) :
                for l in range (0,3) :
                    pic2.setPixelColor(i//3+(width//3)*k,j//3+(height//3)*l,r1,g1,b1)
    return pic2

def bizarre(pic, width, height) :
    pic2=copy(pic)
    accumList=[]
    for i in range (0, width):
        for j in range (0, height) :
            r1,g1,b1= pic.getPixelColor(i,j)
            if [r1,g1,b1] in accumList :
                indexVal= accumList.index([r1,g1,b1])
                blist= []
                blist= blist+accumList[indexVal+1]
                r2= blist.pop(0)
                g2= blist.pop(0)
                b2= blist.pop(0)
                pic2.setPixelColor(i,j,r2,g2,b2)
            else :
                r2= random.randrange(256)
                g2= random.randrange(256)
                b2= random.randrange(256)
                pic2.setPixelColor(i,j,r2,g2,b2)
                accumList.append([r1,g1,b1])
                accumList.append([r2,g2,b2])
    return pic2
    
def main():
    print "Welcome to the Image Editor"
    pic= picture2.Picture("crayons.bmp")
    print "Here are your editing options: "
    print "flip: flip the image horizontally!"
    print "mirror: mirror the image horizontally!"
    print "scroll: scroll the image your choice of pixels to the right!"
    print "negative: the negative coloration of the image, for your wonder and amazement."
    print "gray: the image in grayscale!"
    print "cycle: cycle the color values, Cycle-delic!"
    print "zoom: zoom in close... intimate..."
    print "posterize: simplify the colors. Looks cool."
    print "brightness: change the brightness to your liking."
    print "contrast: change the contrast to your liking."
    print "rotate: rotate the image 180 degrees."
    print "tile: tile the image."
    print "bizarre: who even knows what this does! I don't!"
    func= raw_input("Please enter your desired manipulation in all lowercase!:" )
    try:
        
        if func=="flip" :
            pic = flip(pic,pic.getWidth(),pic.getHeight())
        elif func=="mirror" :
            pic = mirror(pic,pic.getWidth(),pic.getHeight())
        elif func=="scroll" :
            pic = scroll(pic,pic.getWidth(),pic.getHeight())
        elif func=="negative" :
            pic = negative(pic,pic.getWidth(),pic.getHeight())
        elif func=="gray" :
            pic = gray(pic,pic.getWidth(),pic.getHeight())
        elif func=="cycle" :
            pic = cycle(pic,pic.getWidth(),pic.getHeight())
        elif func=="zoom" :
            pic = zoom(pic,pic.getWidth(),pic.getHeight())
        elif func=="posterize" :
            pic = posterize(pic,pic.getWidth(),pic.getHeight())
        elif func=="brightness" :
            pic = brightness(pic,pic.getWidth(),pic.getHeight())
        elif func=="contrast" :
            pic = contrast(pic,pic.getWidth(),pic.getHeight())
        elif func=="rotate" :
            pic = rotate(pic,pic.getWidth(),pic.getHeight())
        elif func=="tile" :
            pic = tile(pic,pic.getWidth(),pic.getHeight())
        elif func=="bizarre" :
            print "This one takes a while."
            pic = bizarre(pic,pic.getWidth(),pic.getHeight())
        else :
            print "I can't understand what you're asking for. Try again."
        
    except :
        print "I don't know what's wrong. Try again."
    pic.display()
    raw_input()
main()

