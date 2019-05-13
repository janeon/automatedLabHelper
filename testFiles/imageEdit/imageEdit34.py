








import picture2
import random

def blackandwhite(pic, h, w):
    for i in range(0,w):
        for j in range(0,h):
            R,G,B = pic.getPixelColor(i,j)
            if R + G + B < 384:
                R,G,B = 0,0,0
            else:
                R,G,B = 255,255,255
            pic.setPixelColor(i,j,R,G,B)
    return pic

def Bright(pic, h, w):
    lighter = eval(raw_input("How much brighter would you like this picture? "))
    try:
        for i in range(0,w):
            for j in range(0,h):
                R, G, B = pic.getPixelColor(i, j)
                if R + lighter > 255:
                    R = 255
                elif R + lighter < 0:
                    R = 0
                else:
                    R = R+lighter
                if G + lighter > 255:
                    G = 255
                elif G < 0:
                    G = 0
                else:
                    G = G + lighter
                if B + lighter > 255:
                    B = 255
                elif B < 0:
                    B = 0
                else:
                    B = B+ lighter
                pic.setPixelColor(i,j,R,G,B)
    except NameError:
        print "Please use numbers."
    return pic

def Contrast(pic, h, w):
    for i in range(0,w):
        for j in range(0,h):
            R, G, B = pic.getPixelColor(i,j)
            if R != 128:
                if 128-R < 1:
                    R = (R-128)*2
                    R = R + 128
                    if R > 255:
                        R = 255
                else:
                    R = (128-R)*2
                    if R < 1:
                        R = 0
                    else:
                        R = 128-R
            if G != 128:
                if 128-G < 1:
                    G = (G-128)*2
                    G = G+128
                    if G > 255:
                        G = 255
                else:
                    G = (128-G)*2
                    if G < 1:
                        G = 0
                    else:
                        G = 128-G
            if B != 128:
                if 128-B < 1:
                    B = (B-128)*2
                    B = B+128
                    if B > 255:
                        B = 255
                else:
                    B = (128-R)*2
                    if B < 1:
                        B = 0
                    else:
                        B = 128-B
            pic.setPixelColor(i,j,R,G,B)
   
    return pic
                   
def Tiled(pic, h, w):
    return new_pic
                   
           
           
def Grainy(pic, h ,w):
    for i in range(0,w):
        for j in range(0,h):
            R, G, B = pic.getPixelColor(i,j)
            assign = int(random.randrange(1,4))
            assign2 = int(random.randrange(1,4))
            assign3 = int(random.randrange(1,4))
            if assign == 1:
                assign = R
            elif assign == 2:
                assign = G
            elif assign == 3:
                assign = B

            if assign2 == 1:
                assign2 = R
            elif assign2 == 2:
                assign2 = G
            elif assign2 == 3:
                assign2 = B
           
            if assign3 == 1:
                assign3 = R
            elif assign3 == 2:
                assign3 = G
            elif assign3 == 3:
                assign3 = B
            R,G,B = assign,assign2,assign3
            pic.setPixelColor(i,j,R,G,B)
    
        
    return pic
           

def Mirror(pic, h, w):
    for i in range(0, w):
        for j in range(0, h):
            R, G, B = pic.getPixelColor(i, j)
            pic.setPixelColor((w-1)-i, 0+j, R, G, B)
    return pic

def Scroll(pic, h, w, pic_copy):
    try:
        movement = eval(raw_input("How many pixels would you like to scroll over?"))
        if movement > w:
            movement = movement%w
        for i in range(0,w):
            for j in range(0,h):
                R, G, B = pic_copy.getPixelColor(i,j)
                if i + movement > w-1:
                    pic.setPixelColor((i+movement)-w, j, R, G, B)
                else:
                    pic.setPixelColor(i+movement, j, R, G, B)
    except NameError:
        print"Numbers you fool! NUMBERS!"
           
    return pic

def Posterize(pic, h, w):
    for i in range(0, w):
        for j in range(0,h):
            R, G, B = pic.getPixelColor(i, j)
            if R < 32:
                R = 0
            elif R%32 != 0:
                if R%32 < 16:
                    R = (R//32)*32
                else:
                    R = ((R//32)+1)*32
            if G < 32:
                G = 0
            elif G%32 != 0:
                if G%32 < 16:
                    G = (G//32)*32
                else:
                    G = ((G//32)+1)*32
            if B < 32:
                B = 0
            elif B%32 != 0:
                if B%32 < 16:
                    B = (B//32)*32
                else:
                    B = ((B//32)+1)*32
            pic.setPixelColor(i,j,R,G,B)
    return pic

def grayScale(pic):
    H = pic.getHeight()
    W = pic.getWidth()
  
    pic_Copy=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            R,G,B=pic.getPixelColor(j,i)
            new=((R+G+B)/3)
            pic_Copy.setPixelColor(j,i,new,new,new)
    return pic_Copy

def colorCycle(pic):
    H = pic.getHeight()
    W = pic.getWidth()
  
    
    pic_Copy=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            R,G,B=pic.getPixelColor(j,i)
            B,G,R=G,R,B
            
            pic_Copy.setPixelColor(j,i,R,G,B)
    return pic_Copy

def negative(pic):
    H = pic.getHeight()
    W = pic.getWidth()
    
    pic_Copy=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            R,G,B=pic.getPixelColor(j,i)
            newR=255-R
            newG=255-G
            newB=255-B
            pic_Copy.setPixelColor(j,i,newR,newG,newB)
    return pic_Copy

def blur(pic):
    H = pic.getHeight()
    W = pic.getWidth()
    print H,W
    pic_Copy=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            newR,newB,newG=0,0,0
            
            if not j-1==-1 and not i+1==H and not j+1==W and not i-1==-1: 
                R1,G1,B1=pic.getPixelColor(j-1,i-1)
                R2,G2,B2=pic.getPixelColor(j,i-1)
                R3,G3,B3=pic.getPixelColor(j+1,i-1)
                R4,G4,B4=pic.getPixelColor(j-1,i)
                R5,G5,B5=pic.getPixelColor(j,i)
                R6,G6,B6=pic.getPixelColor(j+1,i)
                R7,G7,B7=pic.getPixelColor(j-1,i+1)
                R8,G8,B8=pic.getPixelColor(j,i+1)
                R9,G9,B9=pic.getPixelColor(j+1,i+1)
                newR=(R1+R2+R3+R4+R5+R6+R7+R8+R9)/9
                newG=(G1+G2+G3+G4+G5+G6+G7+G8+G9)/9
                newB=(B1+B2+B3+B4+B5+B6+B7+B8+B9)/9

                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif not j-1==-1 and not i+1==H and not j+1==W and  i-1==-1 :
                R4,G4,B4=pic.getPixelColor(j-1,i)
                R5,G5,B5=pic.getPixelColor(j,i)
                R6,G6,B6=pic.getPixelColor(j+1,i)
                R7,G7,B7=pic.getPixelColor(j-1,i+1)
                R8,G8,B8=pic.getPixelColor(j,i+1)
                R9,G9,B9=pic.getPixelColor(j+1,i+1)
                newR=(R4+R5+R6+R7+R8+R9)/6
                newG=(G4+G5+G6+G7+G8+G9)/6
                newB=(B4+B5+B6+B7+B8+B9)/6
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif j-1==-1 and not i+1==H and not j+1==W and not i-1==-1:
                
                R2,G2,B2=pic.getPixelColor(j,i-1)
                R3,G3,B3=pic.getPixelColor(j+1,i-1)
                
                R5,G5,B5=pic.getPixelColor(j,i)
                R6,G6,B6=pic.getPixelColor(j+1,i)
                
                R8,G8,B8=pic.getPixelColor(j,i+1)
                R9,G9,B9=pic.getPixelColor(j+1,i+1)
                newR=(R2+R3+R5+R6+R8+R9)/6
                newG=(G2+G3+G5+G6+G8+G9)/6
                newB=(B2+B3+B5+B6+B8+B9)/6
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif not j-1>-1 and not i-1>-1:
                
                R5,G5,B5=pic.getPixelColor(j,i)
                R6,G6,B6=pic.getPixelColor(j+1,i)
                
                R8,G8,B8=pic.getPixelColor(j,i+1)
                R9,G9,B9=pic.getPixelColor(j+1,i+1)
                newR=(R5+R6+R8+R9)/4
                newG=(G5+G6+G8+G9)/4
                newB=(B5+B6+B8+B9)/4
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif i+1==W and not j+1==H and not j-1==1:
                R1,G1,B1=pic.getPixelColor(j-1,i-1)
                R2,G2,B2=pic.getPixelColor(j,i-1)
                
                R4,G4,B4=pic.getPixelColor(j-1,i)
                R5,G5,B5=pic.getPixelColor(j,i)
                
                R7,G7,B7=pic.getPixelColor(j-1,i+1)
                R8,G8,B8=pic.getPixelColor(j,i+1)
                
                newR=(R1+R2+R4+R5+R7+R8)/6
                newG=(G1+G2+G4+G5+G7+G8)/6
                newB=(B1+B2+B4+B5+B7+B8)/6
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif i+1<W and not j+1<H and not j-1>-1:
                R1,G1,B1=pic.getPixelColor(j-1,i-1)
                R2,G2,B2=pic.getPixelColor(j,i-1)
                R3,G3,B3=pic.getPixelColor(j+1,i-1)
                R4,G4,B4=pic.getPixelColor(j-1,i)
                R5,G5,B5=pic.getPixelColor(j,i)
                R6,G6,B6=pic.getPixelColor(j+1,i)
                newR=(R1+R2+R3+R4+R5+R6)/6
                newG=(G1+G2+G3+G4+G5+G6)/6
                newB=(B1+B2+B3+B4+B5+B6)/6
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif not i+1<W and not j+1<H:
                R1,G1,B1=pic.getPixelColor(j-1,i-1)
                R2,G2,B2=pic.getPixelColor(j,i-1)
                R4,G4,B4=pic.getPixelColor(j-1,i)
                R5,G5,B5=pic.getPixelColor(j,i)
                newR=(R1+R2+R4+R5)/4
                newG=(G1+G2+G4+G5)/4
                newB=(B1+B2+B4+B5)/4
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif i+1==W and not i-1==-1 and j-1==-1 and not j+1==H:
                R4,G4,B4=pic.getPixelColor(j-1,i)
                R5,G5,B5=pic.getPixelColor(j,i)
                R7,G7,B7=pic.getPixelColor(j-1,i+1)
                R8,G8,B8=pic.getPixelColor(j,i+1)
                newR=(R4+R5+R7+R8)/4
                newG=(G4+G5+G7+G8)/4
                newB=(B4+B5+B7+B8)/4
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            elif i-1==-1 and j+1==H :
                R2,G2,B2=pic.getPixelColor(j,i-1)
                R3,G3,B3=pic.getPixelColor(j+1,i-1)
                
                R5,G5,B5=pic.getPixelColor(j,i)
                R6,G6,B6=pic.getPixelColor(j+1,i)
                newR=(R2+R3+R5+R6)/4
                newG=(G2+G3+G5+G6)/4
                newB=(B2+B3+B5+B6)/4
                
                pic_Copy.setPixelColor(j,i,newR,newG,newB)
            
    return pic_Copy

def rotate180(pic):
    
    H = pic.getHeight()
    W = pic.getWidth()
    print H,W
    pic_Copy=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            R,G,B=pic.getPixelColor(j,i)
            print R,G,B
            newPixelX=W-j-1
            newPixelY=H-i-1
            pic_Copy.setPixelColor(newPixelX,newPixelY,R,G,B)
    return pic_Copy
    
def zoom(pic):
 
    
    H = pic.getHeight()
    W = pic.getWidth()
    pic_Copy=picture2.Picture(W,H)
    Hstart,Hend,Wstart,Wend=0,0,0,0
    Hstart=int(H*.25)
    Hend=int(H*.75)
    Wstart=int(W*.25)
    Wend=int(W*.75)
    
    X,Y=0,0
    for i in range (Hstart,Hend):
        X=0
        Y=Y+2
        for j in range(Wstart,Wend):
            if X>W-2:
                X=W-2
            if Y>H-2:
                Y=H-2
            R,G,B=pic.getPixelColor(j,i)
           
            pic_Copy.setPixelColor(X,Y,R,G,B)
            pic_Copy.setPixelColor(X+1,Y,R,G,B)
            pic_Copy.setPixelColor(X,Y+1,R,G,B)
            pic_Copy.setPixelColor(X+1,Y+1,R,G,B)
            X=X+2
    return pic_Copy


def flipHorizontally(pic):
    
    H = pic.getHeight()
    W = pic.getWidth()
    pic2=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            R,G,B=pic.getPixelColor(j,i)
            
            newPixelX=W-j-1
            
            pic2.setPixelColor(newPixelX,i,R,G,B)
            
    
    return pic2
def makeNew(pic):
    
    H = pic.getHeight()
    W = pic.getWidth()
    pic_Copy=picture2.Picture(W,H)
    for i in range (0,H):
        for j in range(0,W):
            R,G,B=pic.getPixelColor(j,i)
            
            pic_Copy.setPixelColor(j,i,R,G,B)
    return pic_Copy,H,W


def main():

    Continue=True
    INPUT=True
    while INPUT:
        Picture = raw_input("Please enter the image file you'd like loaded: ") 
        try:
            pic=picture2.Picture(Picture)
            INPUT=False
        except:
            print"Im sorry, i dont have that file"

    pic=picture2.Picture(Picture)
    pic.display()
    
    pic_Copy,h,w=makeNew(pic)
      
    while Continue:
        
       
        
        print "This is the picture your starting with"
        print""
        print "These are the possible modifications to the picture"
        print""
        print "Flip Horizontally, Mirror Horizontally, Scroll Horizontally, Make Negative"
        print ""
        print "Make Grayscale, Cycle Color Channels, Zoom, Posterize, Change Brightness"
        print""
        print "Increase Contrast, Blur, Rotate 180 degrees, Grainy, Black and White"
        Command="P"
        Command=raw_input("What would you like to do?: ")
        print Command
        if Command=="Rotate 180 degrees":
            pic_Copy=rotate180(pic_Copy)
            
        elif Command=="Flip Horizontally":
            pic_Copy=flipHorizontally(pic_Copy)
        elif Command=="Make Negative":
            pic_Copy=negative(pic_Copy)
        elif Command=="Make Grayscale":
            pic_Copy=grayScale(pic_Copy)
        elif Command=="Cycle Color Channels":
            pic_Copy=colorCycle(pic_Copy)
        elif Command=="Zoom":
            pic_Copy=zoom(pic_Copy) 
        elif Command=="Blur":
            pic_Copy=blur(pic_Copy)
        elif Command == "Mirror Horizontally":
            pic_Copy = Mirror(pic_Copy, h, w)
            
        elif Command == "Scroll Horizontally":
            pic_Copy = Scroll(pic_Copy, h, w,pic)
            
        elif Command == "Posterize":
            pic_Copy = Posterize(pic_Copy, h, w)
           
        elif Command == "Change Brightness":
            pic_Copy = Bright(pic_Copy, h, w)
            
        elif Command == "Increase Contrast":
            pic_Copy = Contrast(pic_Copy, h, w)
            
        elif Command == "Grainy":
            pic_Copy = Grainy(pic_Copy,h,w)
            
        elif Command == "Black and White":
            pic_Copy = blackandwhite(pic_Copy,h,w)
            
        
        else:
            print"I'm afraid i cant do that. Please use the"
            print "exact phrase used above"
        pic_Copy.display()
        
    


main()
        