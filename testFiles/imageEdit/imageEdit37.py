




import picture2

def Copy(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    picCopy=picture2.Picture(W,H)
    for x in range (0,W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)
            picCopy.setPixelColor(x,y,r,g,b)
    return (picCopy)


def Flip(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    flip=picture2.Picture(W,H)
    for x in range (0,W-1):
        for y in range (0,H-1):
            (r,g,b)=pic.getPixelColor(((W-1)-x),y)
            flip.setPixelColor(x,y,r,g,b)
    return (flip)


def Mirror(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    mirror=picture2.Picture(W,H)
    for x in range ((W/2),W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor((W-x),y)
            mirror.setPixelColor(x,y,r,g,b)
    for x in range (0,((W/2)+1)):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)
            mirror.setPixelColor(x,y,r,g,b)
    return (mirror)
    
    

def Scroll(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    scroll=picture2.Picture(W,H)
    d= input ("How many pixels would you like to scroll?")
    for x in range (0,W-1):
        for y in range (0,H-1):
            (r,g,b)=pic.getPixelColor((x+d)%W,y)
            scroll.setPixelColor(x,y,r,g,b)
    return (scroll)


def Neg(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    neg=picture2.Picture(W,H)
    for x in range (0,W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)
            neg.setPixelColor(x,y,255-r,255-g,255-b)
    return (neg)


def Gray(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    gray=picture2.Picture(W,H)
    for x in range (0,W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)
            grayvalue=(r+g+b)/3
            gray.setPixelColor(x,y,grayvalue,grayvalue,grayvalue)
    return (gray)


def Cycle(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    cycle=picture2.Picture(W,H)
    for x in range (0,W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)
            cycle.setPixelColor(x,y,b,r,g)
    return (cycle)



def Zoom(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    zoom=picture2.Picture(W,H)
    for x in range (W//4,(3*W)//4):
        for y in range (H//4,(3*H)//4):
            (r,g,b)=pic.getPixelColor(x,y)
            zoom.setPixelColor(2*(x-(W//4)),2*(y-(H//4)),r,g,b)
            zoom.setPixelColor(2*(x-(W//4))+1,2*(y-(H//4)),r,g,b)
            zoom.setPixelColor(2*(x-(W//4)),2*(y-(H//4))+1,r,g,b)
            zoom.setPixelColor(2*(x-(W//4))+1,2*(y-(H//4))+1,r,g,b)
    return (zoom)



def Post(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    post=picture2.Picture(W,H)
    for x in range (0,W-1):
        for y in range (0,H-1):
            (r,g,b)=pic.getPixelColor(x,y)
            if r%32<16:
                R=(r//32)*32
            if r%32>=16:
                R=((r//32)+1)*32
            if g%32<16:
                G=(g//32)*32
            if g%32>=16:
                G=((g//32)+1)*32
            if b%32<16:
                B=(b//32)*32
            if b%32>=16:
                B=((b//32)+1)*32
           
            post.setPixelColor(x,y,R,G,B)
    return (post)


def Bright(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    bright=picture2.Picture(W,H)
    a=input("How much would you like to adjust the brightness?")
    for x in range (0,W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)


            if r+a<=0:
                R=0
            if r+a>=255:
                R=255
            else:
                R=r+a
            if b+a<=0:
                B=0
            if b+a>=255:
                B=255
            else:
                B=b+a
            if g+a<=0:
                G=0
            if g+a>=255:
                G=255
            else:
                G=g+a
            bright.setPixelColor(x,y,R,G,B)
    return (bright)


def Contrast(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    contrast=picture2.Picture(W,H)
    for x in range (0,W):
        for y in range (0,H):
            (r,g,b)=pic.getPixelColor(x,y)
            A=[]
            for i in [r,g,b]:
                if i==128:
                    A=A+[i]
                if i <128:
                    A=A+[128-2*(128-i)]
                if i >128:
                    A=A+[128+2*(i-128)]
                    
            contrast.setPixelColor(x,y,A[0],A[1],A[2])
    return (contrast)









def Blur(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    blur=picture2.Picture(W,H)
    copy=Copy(pic)
    for x in range (0,W-1):
        for y in range (0,H-1):
            if x==0 and y==0:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r2,g2,b2)=copy.getPixelColor(x+1,y)
                (r3,g3,b3)=copy.getPixelColor(x,y+1)
                (r4,g4,b4)=copy.getPixelColor(x+1,y+1)
                rAvg=((r1+r2+r3+r4)//4)
                gAvg=((g1+g2+g3+g4)//4)
                bAvg=((b1+b2+b3+b4)//4)
            if x==0 and y==H:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r2,g2,b2)=copy.getPixelColor(x+1,y)
                (r6,g6,b6)=copy.getPixelColor(x,y-1)
                (r8,g8,b8)=copy.getPixelColor(x+1,y-1)
                rAvg=((r1+r2+r6+r8)//4)
                gAvg=((g1+g2+g6+g8)//4)
                bAvg=((b1+b2+b6+b8)//4)
            if x==W and y==0:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r3,g3,b3)=copy.getPixelColor(x,y+1)
                (r5,g5,b5)=copy.getPixelColor(x-1,y)
                (r9,g9,b9)=copy.getPixelColor(x-1,y+1)
                rAvg=((r1+r3+r5+r9)//4)
                gAvg=((g1+g3+g5+g9)//4)
                bAvg=((b1+b3+b5+b9)//4)
            if x==W and y==H:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r5,g5,b5)=copy.getPixelColor(x-1,y)
                (r6,g6,b6)=copy.getPixelColor(x,y-1)
                (r7,g7,b7)=copy.getPixelColor(x-1,y-1)
                rAvg=((r1+r5+r6+r7)//4)
                gAvg=((g1+g5+g6+g7)//4)
                bAvg=((b1+b5+b6+b7)//4)
            if x==0 and y>0 and y<H:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r2,g2,b2)=copy.getPixelColor(x+1,y)
                (r3,g3,b3)=copy.getPixelColor(x,y+1)
                (r4,g4,b4)=copy.getPixelColor(x+1,y+1)
                (r6,g6,b6)=copy.getPixelColor(x,y-1)
                (r8,g8,b8)=copy.getPixelColor(x+1,y-1)
                rAvg=((r1+r2+r3+r4+r6+r8)//6)
                gAvg=((g1+g2+g3+g4+g6+g8)//6)
                bAvg=((b1+b2+b3+b4+b6+b8)//6)
            if x==W and y>0 and y<H:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r3,g3,b3)=copy.getPixelColor(x,y+1)
                (r5,g5,b5)=copy.getPixelColor(x-1,y)
                (r6,g6,b6)=copy.getPixelColor(x,y-1)
                (r7,g7,b7)=copy.getPixelColor(x-1,y-1)
                (r9,g9,b9)=copy.getPixelColor(x-1,y+1)
                rAvg=((r1+r3+r5+r6+r7+r9)//6)
                gAvg=((g1+g3+g5+g6+g7+g9)//6)
                bAvg=((b1+b3+b5+b6+b7+b9)//6)
            if x>0 and x<W and y==0:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r2,g2,b2)=copy.getPixelColor(x+1,y)
                (r3,g3,b3)=copy.getPixelColor(x,y+1)
                (r4,g4,b4)=copy.getPixelColor(x+1,y+1)
                (r5,g5,b5)=copy.getPixelColor(x-1,y)
                (r9,g9,b9)=copy.getPixelColor(x-1,y+1)
                rAvg=((r1+r2+r3+r4+r5+r9)//6)
                gAvg=((g1+g2+g3+g4+g5+g9)//6)
                bAvg=((b1+b2+b3+b4+b5+b9)//6)
            if x>0 and x<W and y==H:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r2,g2,b2)=copy.getPixelColor(x+1,y)
                (r5,g5,b5)=copy.getPixelColor(x-1,y)
                (r6,g6,b6)=copy.getPixelColor(x,y-1)
                (r7,g7,b7)=copy.getPixelColor(x-1,y-1)
                (r8,g8,b8)=copy.getPixelColor(x+1,y-1)
                rAvg=((r1+r2+r5+r6+r7+r8)//6)
                gAvg=((g1+g2+g5+g6+g7+g8)//6)
                bAvg=((b1+b2+b5+b6+b7+b8)//6)
            if x>0 and x<W and y>0 and y<H:
                (r1,g1,b1)=copy.getPixelColor(x,y)
                (r2,g2,b2)=copy.getPixelColor(x+1,y)
                (r3,g3,b3)=copy.getPixelColor(x,y+1)
                (r4,g4,b4)=copy.getPixelColor(x+1,y+1)
                (r5,g5,b5)=copy.getPixelColor(x-1,y)
                (r6,g6,b6)=copy.getPixelColor(x,y-1)
                (r7,g7,b7)=copy.getPixelColor(x-1,y-1)
                (r8,g8,b8)=copy.getPixelColor(x+1,y-1)
                (r9,g9,b9)=copy.getPixelColor(x-1,y+1)
                rAvg=((r1+r2+r3+r4+r5+r6+r7+r8+r9)//9)
                gAvg=((g1+g2+g3+g4+g5+g6+g7+g8+g9)//9)
                bAvg=((b1+b2+b3+b4+b5+b6+b7+b8+b9)//9)
            
            
            
            
            blur.setPixelColor(x,y,rAvg,gAvg,bAvg)
    return (blur)


def Rotate(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    rotate=picture2.Picture(W,H)
    for x in range (0,W-1):
        for y in range (0,H-1):
            (r,g,b)=pic.getPixelColor((W-1)-x,(H-1)-y)
            rotate.setPixelColor(x,y,r,g,b)
    return (rotate)


def Shadows(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    shadow=picture2.Picture(W,H)
    for x in range (0,W-1):
        for y in range (0,H-1):
            (r,g,b)=pic.getPixelColor(x,y)
            if r<100 and g<100 and b<100:
                r=r//2
                b=b//2
                g=g//2
            shadow.setPixelColor(x,y,r,g,b)
    return (shadow)


def RGB(pic):
    W=pic.getWidth()
    H=pic.getHeight()
    rgb=picture2.Picture(W,H)
    for x in range (0,W-1):
        for y in range (0,H-1):
            (r,g,b)=pic.getPixelColor(x,y)
            if r>=g and r>=b:
                b=0
                g=0
            if g>=r and g>=b:
                r=0
                b=0
            if b>=r and b>=g:
                r=0
                g=0
            rgb.setPixelColor(x,y,r,g,b)
    return (rgb)

def options():
    try:
        print
        print "This program can do the following:"
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
        print "13. Darken Shadows"
        print "14. Red Green Blue"
        print
        number = input("Please enter the number of what you would like to do: ")
        return (number)
    except NameError:
        print "I'm sorry I didn't understand that."
        print()
        return(0)


def main():
    try:
        print "Welcome. This is an image editor."
        filename=raw_input("Please enter the image file you would like loaded: ")
        pic=picture2.Picture(filename)
        original=Copy(pic)
        more = False
        while not more:
            cont=raw_input("Would you like to edit the image?")
            if cont == "yes":
                function=options()
                if function==0:
                    function=options()
                if function==1:
                    pic=Flip(pic)
                if function==2:
                    pic=Mirror(pic)
                if function==3:
                    pic=Scroll(pic)
                if function==4:
                    pic=Neg(pic)
                if function==5:
                    pic=Gray(pic)
                if function==6:
                    pic=Cycle(pic)
                if function==7:
                    pic=Zoom(pic)
                if function==8:
                    pic=Post(pic)
                if function==9:
                    pic=Bright(pic)
                if function==10:
                    pic=Contrast(pic)
                if function==11:
                    pic=Blur(pic)
                if function==12:
                    pic=Rotate(pic)
                if function==13:
                    pic=Shadows(pic)
                if function==14:
                    pic=RGB(pic)
                print "When you are done viewing the image hit enter."
                pic.display()
                raw_input()
            elif cont == "no":
                more = True
        print "Thank you for editing! Here's your original image:"
        print "Hit enter for your edited image!"
        original.display()
        raw_input()

        print
        print "To exit the program hit enter."
        pic.display()       
        raw_input()
       
    except IOError:
        print "I'm sorry. We cannot find that file. Please try again."
        print
        print
        main()

main()

