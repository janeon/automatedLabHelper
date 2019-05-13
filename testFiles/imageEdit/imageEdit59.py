






import picture2
import math


def main():
    
    print "Welcome to a very basic image editing program. "
    pic=picture2.Picture(raw_input("Please type in a bmp file name: "))
    w=pic.getWidth()
    h=pic.getHeight()
    print "You have some choices to make."
    print "The following commands are possible (please enter in lowercase):"
    print "o 'flip' will flip the image horizontally."
    print "o 'mirror' will reflect the left half of the image."
    print "o 'scroll' will push the image a given number of pixels and" '\n' "wrap it."
    print "o 'negate' will create a photo negative of the image."
    print "o 'grayscale' will create a greyscale version of the image."
    print "o 'cycle color channels' will replace all red with blue," '\n' "all blue with green, and all green with red."
    print "o 'zoom' will zoom into the image."
    print "o 'blur' will blur the image."
    print "o 'posterize' will reduce the number of colors used in the image."
    print "o 'change brightness' will either increase or decrease" '\n' "brightness by a certain degree."
    print "o 'contrast' will change the contrast in the image."
    print "o 'rotate' will rotate the image 180 degrees."
    print "o 'highlight color' will allow you to keep only" '\n' "blotches of a certain color."
    print "o 'funhouse mirror' will create a pair of reflected images " '\n' "laid on top of each other."
    
    moredata="yes"
    while moredata=="yes":
        command=raw_input("What would you like to do to the photo? ")
        if command=="flip":
            pic2=picture2.Picture(w,h)
            picCopy(w,h,pic2)
            flip(w,h,pic,pic2)
            pic.display()
        if command=="negate":
            negative(w,h,pic)
            pic.display()
        if command=="grayscale":
            grayscale(w,h,pic)
            pic.display()
        if command=="cycle color channels":
            colorChannels(w,h,pic)
            pic.display()
        if command=="posterize":
            posterize(w,h,pic)
            pic.display()
        if command=="change brightness":
            brightness(w,h,pic)
            pic.display()
        if command=="contrast":
            contrast(w,h,pic)
            pic.display()
        if command=="blur":
            pic2=picture2.Picture(w,h)
            picCopy(w,h,pic2)
            w=pic2.getWidth()
            h=pic2.getHeight()
            blur(w,h,pic,pic2)
            pic.display()
        if command=="highlight color":
            colorhighlight(w,h,pic)
            pic.display()
        if command=="funhouse mirror":
            funhouseMirror(w,h,pic)
            pic.display()
        if command=="mirror":
            mirror(w,h,pic)
            pic.display()
        if command=="scroll":
            pic2=picture2.Picture(w,h)
            picCopy(w,h,pic2)
            horizScroll(w,h,pic,pic2)
            pic.display()
        if command=="rotate":
            pic2=picture2.Picture(w,h)
            picCopy(w,h,pic2)
            rotate180(w,h,pic,pic2)
            pic.display()
        if command=="zoom":
            pic2=picture2.Picture(w,h)
            picCopy(w,h,pic2)
            w=pic2.getWidth()
            h=pic2.getHeight()
            zoom(w,h,pic,pic2)
            pic.display()
        moredata=raw_input("Would you like to do something else to the photo? ")
    print "You're done. Enjoy your photo edited with the blood, " '\n' "sweat and tears."

def negative(w,h,pic): 
    for x in range (0,(w-1)):
        for y in range (0,(h-1)):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,abs(255-R))
            pic.setPixelGreen(x,y,abs(255-G))
            pic.setPixelBlue(x,y,abs(255-B))

def grayscale(w,h,pic): 
    for x in range (0,(w-1)):
        for y in range (0, h-1):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,(R+G+B)/3)
            pic.setPixelGreen(x,y,(R+G+B)/3)
            pic.setPixelBlue(x,y,(R+G+B)/3)

def colorChannels(w,h,pic): 
    for x in range (0,(w-1)):
        for y in range (0, h-1):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,B)
            pic.setPixelGreen(x,y,R)
            pic.setPixelBlue(x,y,G)

def xround(x, base=32): 
    return int(base * round(float(x)/base))

def posterize(w,h,pic): 
    for x in range (0,(w-1)):
        for y in range (0,(h-1)):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,xround(R))
            pic.setPixelGreen(x,y,xround(G))
            pic.setPixelBlue(x,y,xround(B))
  
def brightness(w,h,pic): 
    bright=eval(raw_input("By how much would you like the picture brightened? "))
    for x in range (0,(w-1)):
        for y in range (0,(h-1)):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            if (R+bright)>255:
                pic.setPixelRed(x,y,255)
            elif(R+bright)<0:
                pic.setPixelRed(x,y,0)
            else:    
                pic.setPixelRed(x,y,R+bright)
            if (G+bright)>255:
                pic.setPixelGreen(x,y,255)
            elif(G+bright)<0:
                pic.setPixelGreen(x,y,0)
            else:    
                pic.setPixelGreen(x,y,G+bright)
            if (B+bright)>255:
                pic.setPixelBlue(x,y,255)
            elif(B+bright)<0:
                pic.setPixelBlue(x,y,0)
            else:    
                pic.setPixelBlue(x,y,B+bright)
 
def contrast(w,h,pic): 
    contrastvalue=eval(raw_input("By what factor would you like to increase contrast? "))
    for x in range (0, w-1):
        for y in range (0,(h-1)):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            pic.setPixelRed(x,y,((R-128)*contrastvalue)+R)
            pic.setPixelGreen(x,y,((G-128)*contrastvalue)+G)
            pic.setPixelBlue(x,y,((B-128)*contrastvalue)+B)


def picCopy(w,h,pic2): 
    pic=picture2.Picture("crayons.bmp")
    for x in range (0,w-1):
        for y in range (0,h-1):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            pic2.setPixelColor(x,y,R,G,B)


  
def blur(w,h,pic,pic2):
    for x in range (0,w):
       for y in range (0,h):
            if x==0 and y==0: 
                C1=pic2.getPixelColor(x+1,y)
                C2=pic2.getPixelColor(x,y+1)
                C3=pic2.getPixelColor(x+1,y+1)
                C4=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0])/4
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1])/4
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2])/4
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif x==0 and y==h-1: 
                C1=pic2.getPixelColor(x,y-1)
                C2=pic2.getPixelColor(x+1,y-1)
                C3=pic2.getPixelColor(x+1,y)
                C4=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0])/4
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1])/4
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2])/4
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif x==w-1 and y==0: 
                C1=pic2.getPixelColor(x-1,y)
                C2=pic2.getPixelColor(x-1,y+1)
                C3=pic2.getPixelColor(x,y+1)
                C4=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0])/4
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1])/4
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2])/4
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif x==w-1 and y==h-1: 
                C1=pic2.getPixelColor(x-1,y-1)
                C2=pic2.getPixelColor(x,y-1)
                C3=pic2.getPixelColor(x-1,y)
                C4=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0])/4
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1])/4
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2])/4
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif y==0: 
                C1=pic2.getPixelColor(x-1,y)
                C2=pic2.getPixelColor(x+1,y)
                C3=pic2.getPixelColor(x-1,y+1)
                C4=pic2.getPixelColor(x,y+1)
                C5=pic2.getPixelColor(x+1,y+1)
                C6=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0]+C5[0]+C6[0])/6
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1]+C5[1]+C6[1])/6
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2]+C5[2]+C6[2])/6
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif x==0: 
                C1=pic2.getPixelColor(x,y-1)
                C2=pic2.getPixelColor(x+1,y-1)
                C3=pic2.getPixelColor(x+1,y)
                C4=pic2.getPixelColor(x,y+1)
                C5=pic2.getPixelColor(x+1,y+1)
                C6=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0]+C5[0]+C6[0])/6
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1]+C5[1]+C6[1])/6
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2]+C5[2]+C6[2])/6
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif x==w-1: 
                C1=pic2.getPixelColor(x-1,y-1)
                C2=pic2.getPixelColor(x,y-1)
                C3=pic2.getPixelColor(x-1,y)
                C4=pic2.getPixelColor(x-1,y+1)
                C5=pic2.getPixelColor(x,y+1)
                C6=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0]+C5[0]+C6[0])/6
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1]+C5[1]+C6[1])/6
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2]+C5[2]+C6[2])/6
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            elif y==h-1: 
                C1=pic2.getPixelColor(x-1,y-1)
                C2=pic2.getPixelColor(x-1,y)
                C3=pic2.getPixelColor(x,y-1)
                C4=pic2.getPixelColor(x+1,y-1)
                C5=pic2.getPixelColor(x+1,y)
                C6=pic2.getPixelColor(x,y)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0]+C5[0]+C6[0])/6
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1]+C5[1]+C6[1])/6
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2]+C5[2]+C6[2])/6
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)
            else:
                C1=pic2.getPixelColor(x-1,y-1)
                C2=pic2.getPixelColor(x-1,y)
                C3=pic2.getPixelColor(x-1,y+1)
                C4=pic2.getPixelColor(x,y-1)
                C5=pic2.getPixelColor(x,y)
                C6=pic2.getPixelColor(x,y+1)
                C7=pic2.getPixelColor(x+1,y-1)
                C8=pic2.getPixelColor(x+1,y)
                C9=pic2.getPixelColor(x+1,y+1)
                NewColorRed=(C1[0]+C2[0]+C3[0]+C4[0]+C5[0]+C6[0]+C7[0]+C8[0]+C9[0])/9
                NewColorGreen=(C1[1]+C2[1]+C3[1]+C4[1]+C5[1]+C6[1]+C7[1]+C8[1]+C9[1])/9
                NewColorBlue=(C1[2]+C2[2]+C3[2]+C4[2]+C5[2]+C6[2]+C7[2]+C8[2]+C9[2])/9
                pic.setPixelRed(x,y,NewColorRed)
                pic.setPixelBlue(x,y,NewColorBlue)
                pic.setPixelGreen(x,y,NewColorGreen)


  
def rotate180(w,h,pic,pic2):
    for x in range (0,(w-1)):
        for y in range (0,h-1):
            tempcolors=pic2.getPixelColor(x,y)
            xval=w-1-x
            yval=h-1-y
            pic.setPixelColor(xval,yval,tempcolors[0],tempcolors[1],tempcolors[2])

def zoom(w,h,pic,pic2):
    for x in range (0,w-1):
        for y in range (0,h-1):
            color=pic2.getPixelColor (((x//2)+(w/4)), ((y//2)+(h/4)))
            pic.setPixelColor(x,y,color[0],color[1],color[2])
            

def mirror(w,h,pic):
    for x in range (0,(w-1)):
        for y in range (0,h-1):
            
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            val=(w-1)-x
            pic.setPixelRed(val,y,R)
            pic.setPixelBlue(val,y,B)
            pic.setPixelGreen(val,y,G)  
   
def horizScroll(w,h,pic,pic2):
    d=eval(raw_input("How many pixels to the right would you like to scroll the photo? "))
    for x in range (0,w-1):
        for y in range (0,h-1):
            val=(x+d)%w
            colors=pic2.getPixelColor(x,y)
            pic.setPixelColor(val,y,colors[0],colors[1],colors[2])



def flip(w,h,pic,pic2):
    for x in range (0,(w-1)):
        for y in range (0,h-1):
            tempcolors=pic2.getPixelColor(x,y)
            xval=(w-1)-x
            pic.setPixelColor(xval,y,tempcolors[0],tempcolors[1],tempcolors[2])


def colorhighlight(w,h,pic): 
    color=raw_input("What color would you like to keep in the photo? " )
    for x in range (0,(w-1)):
        for y in range (0, h-1):
            R=pic.getPixelRed(x,y)
            G=pic.getPixelGreen(x,y)
            B=pic.getPixelBlue(x,y)
            if color=="red":
                if R>100:
                    R=255
                    G=50
                    B=50
                    pic.setPixelRed(x,y,R)
                    pic.setPixelGreen(x,y,(R+G+B)/3)
                    pic.setPixelBlue(x,y,(R+G+B)/3)
                else:
                    pic.setPixelRed(x,y,(R+G+B)/3)
                    pic.setPixelGreen(x,y,(R+G+B)/3)
                    pic.setPixelBlue(x,y,(R+G+B)/3)
            if color=="green":
                if G>100:
                    G=255
                    R=50
                    B=50
                    pic.setPixelRed(x,y,(R+G+B)/3)
                    pic.setPixelGreen(x,y,G)
                    pic.setPixelBlue(x,y,(R+G+B)/3)
                else:
                    pic.setPixelRed(x,y,(R+G+B)/3)
                    pic.setPixelGreen(x,y,(R+G+B)/3)
                    pic.setPixelBlue(x,y,(R+G+B)/3)
            if color=="blue":
                if B>100:
                    B=255
                    R=50
                    G=50
                    pic.setPixelRed(x,y,(R+G+B)/3)
                    pic.setPixelGreen(x,y,(R+G+B)/3)
                    pic.setPixelBlue(x,y,B)
                else:
                    pic.setPixelRed(x,y,(R+G+B)/3)
                    pic.setPixelGreen(x,y,(R+G+B)/3)
                    pic.setPixelBlue(x,y,(R+G+B)/3)
                    
def funhouseMirror(w,h,pic):
    for x in range (0,(w-1)/2):
        for y in range (0,h-1):
            colors=pic.getPixelColor(x,y)
            x=w-1-x
            pic.setPixelColor(x,y,colors[0],colors[1],colors[2])
main()