





import picture2

def flip(pic,w,h) : 
        
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(w-1-i,j,R)
            pic2.setPixelGreen(w-1-i,j,G)
            pic2.setPixelBlue(w-1-i,j,B)
            
    return pic2
    
def mirhor(pic,w,h) : 
        
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w/2) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            pic2
            pic2.setPixelRed((w/2)-i,j,R)
            pic2.setPixelGreen((w/2)-i,j,G)
            pic2.setPixelBlue((w/2)-i,j,B)
            
            pic2.setPixelRed((w/2)+i,j,R)
            pic2.setPixelGreen((w/2)+i,j,G)
            pic2.setPixelBlue((w/2)+i,j,B)

    return pic2

def scrhor(pic,w,h) : 
    n= int(raw_input("How many pixels would you like to scroll this over by? "))
    
    pic2 = picture2.Picture(w,h)

    for i in range (0, w-1):
        for j in range (0,h-1): 
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            Rx=i+n
            if Rx > w-1:
                Rx=Rx -(w-1)
            
            pic2.setPixelRed(Rx,j,R) 
            
            Gx=i+n
            if Gx > w-1:
                Gx=Gx-(w-1)
            
            pic2.setPixelGreen(Gx,j,G)
            
            Bx=i+n
            if Bx > w-1:
                Bx=Bx-(w-1)
            
            pic2.setPixelBlue(Bx,j,B)
            
    return pic2
    
def neg(pic,w,h) : 
    
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1):
        for j in range (0,h-1): 
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
             
            pic2.setPixelRed(i,j,(255-R))
            pic2.setPixelGreen(i,j,(255-G))
            pic2.setPixelBlue(i,j,(255-B))
    
    return pic2
    
def gray (pic,w,h) : 
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(i,j,((R+G+B)/3))
            pic2.setPixelGreen(i,j,((R+G+B)/3))
            pic2.setPixelBlue(i,j,((R+G+B)/3))
            
    return pic2

def cycle (pic,w,h) : 
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(i,j,B)
            pic2.setPixelGreen(i,j,R)
            pic2.setPixelBlue(i,j,G)

    return pic2

def zoom (pic,w,h) : 
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i/2,j/2)
            G = pic.getPixelGreen(i/2,j/2)
            B = pic.getPixelBlue(i/2,j/2)
            
            pic2.setPixelRed(i,j,R)
            pic2.setPixelGreen(i,j,G)
            pic2.setPixelBlue(i,j,B)
            
    return pic2

def post (pic,w,h) : 
    pic2 = picture2.Picture(w,h)

    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(i,j,(R//32)*32)
            pic2.setPixelGreen(i,j,(G//32)*32)
            pic2.setPixelBlue(i,j,(B//32)*32)
            
    return pic2

def brit (pic,w,h) : 
    n= int(raw_input("How much do you want to change the brightness? scale of -5 to 5 "))
    pic2 = picture2.Picture(w,h)

    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            
            Rm = R+(n*25)
            if Rm > 255 :
                Rm==255
            if Rm < 0 :
                Rm==0
       
            pic2.setPixelRed(i,j, Rm)
            
            Gm = G+(n*25)
            if Gm > 255 :
                Gm==255
            if Gm < 0 :
                Gm==0
  

            pic2.setPixelGreen(i,j,(Gm))
            
            Bm = B+(n*25)
            if Bm > 255 :
                Bm==255
            if Bm < 0 :
                Bm==0
            
                
            pic2.setPixelBlue(i,j, Bm)         
    
    return pic2
    
def cont (pic,w,h) : 
    
    pic2 = picture2.Picture(w,h)
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            Rm=R
            
            if R > 128 :
                Rm= 128 - (128-R)*2
            if R < 128 :
                Rm= 128 + (R-128)*2

            if Rm > 255 :
                Rm==255
            if Rm < 0 :
                Rm==0
       
            pic2.setPixelRed(i,j, Rm)
            
            Gm=G
            if R > 128 :
                Gm= 128 - (128-G)*2
            if G < 128 :
                Gm= 128 + (G-128)*2

            if Gm > 255 :
                Gm==255
            if Gm < 0 :
                Gm==0

            pic2.setPixelGreen(i,j,(Gm))
            
            Bm=B
            if B > 128 :
                Bm= 128 - (128-B)*2
            if B < 128 :
                Bm= 128 + (B-128)*2

            if Bm > 255 :
                Bm==255
            if Bm < 0 :
                Bm==0
            
            pic2.setPixelBlue(i,j, Bm)
            
    return pic2

def blur (pic,w,h) : 
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(i,j,R)
            pic2.setPixelGreen(i,j,G)
            pic2.setPixelBlue(i,j,B)
                           
    return pic2

def rota (pic,w,h) : 
    pic2 = picture2.Picture(h,w)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(j,i,R)
            pic2.setPixelGreen(j,i,G)
            pic2.setPixelBlue(j,i,B)
                           
    return pic2            

def yell (pic,w,h) : 
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            n=4
            Rm = R+(n*25)
            if Rm > 255 :
                Rm==255
            if Rm < 0 :
                Rm==0
       
            pic2.setPixelRed(i,j, Rm)
            
            Gm = G+(n*25)
            if Gm > 255 :
                Gm==255
            if Gm < 0 :
                Gm==0
  

            pic2.setPixelGreen(i,j,(Gm))
            
            Bm = B+(n*25)
            if Bm > 255 :
                Bm==255
            if Bm < 0 :
                Bm==0
            
                
            pic2.setPixelRed(i,j, Bm)         
    
    return pic2
    
def blin(pic,w,h) : 
    
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1,10) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(i,j,R)
            pic2.setPixelGreen(i,j,G)
            pic2.setPixelBlue(i,j,B)
    return pic2
    
def fun(pic,w,h) : 
    
    pic2 = picture2.Picture(w,h)
    
    for i in range (0, w-1) :
        for j in range (0, h-1) :
            R = pic.getPixelRed(i,j)
            G = pic.getPixelGreen(i,j)
            B = pic.getPixelBlue(i,j)
            
            pic2.setPixelRed(i,j,R)
            pic2.setPixelGreen(i,j,G)
            pic2.setPixelBlue(i,j,B)
            
    return pic2

def main ():
    pic = picture2.Picture("crayons.bmp")
    w = pic.getWidth()
    h = pic.getHeight()
    pic2 = fun(pic,w,h)
    
    comm= 0 
    
    print "We're going to edit an image!"
    fileName = raw_input("Please enter the image file you'd like loaded: ")
    
    pic.display()
    input() 
    
    while comm > -1 :
        print "The possible manipulations are :\n(1)Flip Horizontally\n(2)Mirror Horizontally\n(3)Scroll Horizontally\n(4)Make Negative\n(5)Make Grayscale\n(6)Cycle Color Channels\n(7)Zoom\n(8)Posterize\n(9)Change Brightness\n(10)Increase Contrast\n(11)Blur\n(12)Rotate 180 Degrees\n(13)Yellowize\n(14)Blinds"
    
        comm = int(raw_input("Enter what manipulation you'd like according to the number listed: "))
        
        if comm == 1 :
            pic2=flip(pic2,w,h) 
        if comm == 2 :
            pic2=mirhor(pic2,w,h) 
        if comm == 3 :
            pic2=scrhor(pic2,w,h) 
        if comm == 4 :
            pic2=neg(pic2,w,h) 
        if comm == 5 :
            pic2=gray(pic2,w,h) 
        if comm == 6 :
            pic2=cycle(pic2,w,h) 
        if comm == 7 :
            pic2=zoom(pic2,w,h) 
        if comm == 8 :
            pic2=post(pic2,w,h) 
        if comm == 9:
            pic2=brit(pic2,w,h) 
        if comm == 10 :
            pic2=cont(pic2,w,h) 
        if comm == 11 :
            pic2=blur(pic2,w,h) 
        if comm == 12 :
            pic2=rota(pic2,w,h) 
        if comm == 13 :
            pic2=yell(pic2,w,h)
        if comm == 14:
            pic2=blin(pic2,w,h)
                
        print "What's next?"
        pic2.display()
        input()
        
main ()


