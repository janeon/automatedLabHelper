


















import picture2

        

def main():
    filename = raw_input("What file would you like to use?")
    pic = picture2.Picture(filename)
    pic.display()



    
    print"flip rotate180 playingcard mirror scroll negative grayscale cyclecolors zoom rearrange posterize brightness contrast blur"
    manipulation = raw_input("Which manipulation would you like to perform?") 
    manipulation.lower()







    



    
    
    
    
    
    
    
    

    
    

    if manipulation == "rotate180":
    
        width, height = bodyType(pic)
        piccopy = copy(pic)
        for i in range(width):
            for j in range(height):
                R,G,B = piccopy.getPixelColor(i,j)
                pic.setPixelColor(width-i-1,height-j-1,R,G,B)
        pic.display()
        input()
   

    if manipulation == "playingcard": 
        width, height = bodyType(pic)
        temp = picture2.Picture(width,height)
        for i in range(width//2):
            for j in range(height):
                R,G,B = pic.getPixelColor(i,j)
                pic.setPixelColor(width-i-1,height-j-1,R,G,B)
        pic.display()
        input()
        
    if manipulation == "mirror": 
        width, height = bodyType(pic)
        temp = picture2.Picture(width,height)
        for i in range(width//2):
            for j in range(height-1):
                R,G,B = pic.getPixelColor(i,j)
                pic.setPixelColor(width-i-1,j,R,G,B)
        pic.display()
        input()
        
    if manipulation == "scroll": 
        w, h = bodyType(pic)
        piccopy = copy(pic)
        d = eval(raw_input("How far would you like to scroll? "))
        for j in range (0, h):
            for i in range (0, w):
                red, green, blue = piccopy.getPixelColor(i,j)
                pic.setPixelColor((i+d)%w, j, red, green, blue)
        pic.display()
        input()
    if manipulation == "negative": 
        w,h = bodyType(pic)
        for r in range (0, h):
            for c in range (0, w):
                redvalue = pic.getPixelRed(c,r)
                pic.setPixelRed(c,r,(255-redvalue))
                greenvalue = pic.getPixelGreen(c,r)
                pic.setPixelGreen(c,r,(255-greenvalue))
                bluevalue = pic.getPixelBlue(c,r)
                pic.setPixelBlue(c,r,(255-bluevalue))
        pic.display()
        input()
    if manipulation == "grayscale": 
        w,h = bodyType(pic)
        for r in range (0, h):
            for c in range (0, w):
                redvalue = pic.getPixelRed(c,r)
                greenvalue = pic.getPixelGreen(c,r)
                bluevalue = pic.getPixelBlue(c,r)
                a = ((redvalue+greenvalue+bluevalue)/3)
                pic.setPixelRed(c,r,a)
                pic.setPixelGreen(c,r,a)
                pic.setPixelBlue(c,r,a)
        pic.display()
        input()
    if manipulation == "cyclecolors":
        w,h = bodyType(pic)
        for r in range (0, h):
                for c in range (0, w):
                    redvalue = pic.getPixelRed(c,r)
                    greenvalue = pic.getPixelGreen(c,r)
                    bluevalue = pic.getPixelBlue(c,r)
                    pic.setPixelRed(c,r,bluevalue)
                    pic.setPixelGreen(c,r,redvalue)
                    pic.setPixelBlue(c,r,greenvalue)
        pic.display()
        input()
    if manipulation == "zoom200":
        w,h = bodyType(pic)
        temp = picture2.Picture(w,h)
        for i in range(w//4,(3*w)//4):
            for j in range(h//4, (3*h)//4):
                R,G,B = temp.getPixelColor(i,j)
                for x in range(0,w-1,2):
                    for y in range(0,h-1,2):
                        pic.setPixelColor(x+1,y,R,G,B)
                        pic.setPixelColor(x,y+1,R,G,B)
                        pic.setPixelColor(x+1,y+1,R,G,B)
                        pic.setPixelColor(x,y,R,G,B)
        pic.display()
        input()
        
    if manipulation == "zoom":
        w,h = bodyType(pic)
        tem = copy(pic)
        a = w//4
        b = a*3
        c = h//4
        d = c*3
        for tx in range(a,b+1):
            for ty in range(c,d+1):
                red,green,blue = tem.getPixelColor(tx,ty)
                for i in range(0,w-1,2):
                    for j in range(0,h-1,2):
                        printtx,ty,i,j
                        pic.setPixelColor(i,j,red,green,blue)
        
    if manipulation == "rearrange":
        w,h = bodyType(pic)
        for r in range (0, h):
            for c in range (0, w):
                redvalue = pic.getPixelRed(c,r)
                pic.setPixelRed(c,r,(255-redvalue))
                greenvalue = pic.getPixelGreen(c,r)
                pic.setPixelGreen(c,r,(255-greenvalue))
                bluevalue = pic.getPixelBlue(c,r)
                pic.setPixelBlue(c,r,(255-bluevalue))
        for i in range (0, h):
                for p in range (0, w):
                    redvalue = pic.getPixelRed(p,i)
                    greenvalue = pic.getPixelGreen(p,i)
                    bluevalue = pic.getPixelBlue(p,i)
                    pic.setPixelRed(p,i,bluevalue)
                    pic.setPixelGreen(p,i,redvalue)
                    pic.setPixelBlue(p,i,greenvalue)
        print "Recognize I am different from negative"
        pic.display()
        input()
    
    if manipulation == "posterize":
        w,h = bodyType(pic)
        for r in range (0, h):
                for c in range (0, w):
                    redvalue = pic.getPixelRed(c,r)
                    greenvalue = pic.getPixelGreen(c,r)
                    bluevalue = pic.getPixelBlue(c,r)
                    pic.setPixelRed(c,r,myround(redvalue))
                    pic.setPixelGreen(c,r,myround(greenvalue))
                    pic.setPixelBlue(c,r,myround(bluevalue))







        pic.display()
        input()
        
    if manipulation == "brightness":
        d = eval(raw_input("How would you like to change the brightness?"))
        d = 5
        w,h = bodyType(pic)
        for i in range(w):
            for j in range(h):
                R,G,B = pic.getPixelColor(i,j)
                R += d
                G += d
                B += d
                if R > 255:
                    R = 255
                if R < 0:
                    R = 0
                if G > 255:
                    G = 255
                if G < 0:
                    G = 0
                if B > 255:
                    B = 255
                if B < 0:
                    B = 0
                pic.setPixelColor(i,j,R,G,B)
        pic.display()
        input()
        
    if manipulation == "contrast":
        w,h = bodyType(pic)
        for i in range(w):
            for j in range(h):
                R,G,B = pic.getPixelColor(i,j)
                R = 2*R-128
                G = 2*G-128
                B = 2*B-128
                if R > 255:
                    R = 255
                elif R < 0:
                    R = 0
                elif G > 255:
                    G = 255
                elif G < 0:
                    G = 0
                elif B > 255:
                    B = 255
                elif B < 0:
                    B = 0
                pic.setPixelColor(i,j,R,G,B)
        pic.display()
        input()
        
    if manipulation == "blur":
        w,h = bodyType(pic)
        temp = copy(pic)
        for i in range(1,w-2):
            for j in range(1,h-2):

                temp = copy(pic)
                red = 0
                green = 0
                blue = 0
                for x in range(-1,2,1):
                    for y in range(-1,2,1):
                        print i,j,x,y
                        r = temp.getPixelRed(i+x,j+y)
                        b = temp.getPixelBlue(i+x,j+y)
                        g = temp.getPixelGreen(i+x,j+y)
                        red += r
                        green += g 
                        blue += b
                red = red//9
                blue = blue//9
                green = green//9
                pic.setPixelColor(i,j,red,blue,green)
        print "yay"
        pic.display()
        input()
    if manipulation == "flip":
        w,h = bodyType(pic)
        temp = copy(pic)
        for i in range(w):
            for j in range(h):
                R,G,B = temp.getPixelColor(i,j)
                pic.setPixelColor(w-i-1,j,R,G,B)
                
                
        pic.display()
        input()
    else:
        print"You did not type in manipulation with no spaces. Run the program again."
























    
        
def bodyType(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    return w, h
    
def copy(pic):
    width,height = bodyType(pic)
    temp = picture2.Picture(width,height)
    for i in range(width):
        for j in range(height):
            R,G,B = pic.getPixelColor(i,j)
            temp.setPixelColor(i,j,R,G,B)
    return temp
def myround(x, base=32):
    return int(base * round(float(x)/base))
main()