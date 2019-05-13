


import picture2

def copy(pic, w, h):
    pic2 = picture2.Picture(w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            pic2.setPixelColor(i, j, r, g, b)
    return pic2

def flip(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            pic.setPixelColor((w-i-1), j, c[0], c[1], c[2])
    pic.display()
    raw_input()
    
def mirror(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w/2-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            pic.setPixelColor(i, j, c[0], c[1], c[2])
    for i in range(0, w/2-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            pic.setPixelColor((w-i-1), j, c[0], c[1], c[2])
    pic.display()
    raw_input()
    
def scroll(pic, w, h):
    scroll = input("Scroll by how many pixels? ")
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            i = i + scroll
            if i > w-1:
                i = abs(i-w)+1
            pic.setPixelColor(i, j, c[0], c[1], c[2])
    pic.display()
    raw_input()
            
    
def negative(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            r = abs(255-c[0])
            g = abs(255-c[1])
            b = abs(255-c[2])
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    raw_input()
                
    
def grayscale(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            avg = (c[0] + c[1] + c[2])/3
            pic.setPixelColor(i, j, avg, avg, avg)
    pic.display()
    raw_input()
            
    

def colorChannels(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            pic.setPixelColor(i, j, c[2], c[0], c[1])
    pic.display()
    raw_input()
    
def zoom(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c=cop.getPixelColor(w//4+i//2, h//4+j//2)
            pic.setPixelColor(i, j, c[0], c[1], c[2])          
    pic.display()
    raw_input()
        

def posterize(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = pic.getPixelColor(i, j)
            r = c[0]
            g = c[1]
            b = c[2]
            for l in range(0, 255, 32):
                if r-l in range(16, 0, -1):
                    r = l
                elif r-l in range(-16, 0):
                    r = l
                elif g-l in range(16, 0, -1):
                    g = l
                elif g-l in range(-16, 0):
                    g = l
                elif b-l in range(16, 0, -1):
                    b = l
                elif b-l in range(-16, 0):
                    b = l
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    raw_input()
    
            
   
def bright(pic, w, h):
    bright = input("Brightness change? ")
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = pic.getPixelColor(i, j)
            r = c[0] + bright
            g = c[1] + bright
            b = c[2] + bright
            if r < 0:
                r = 0
            elif r > 255:
                r = 255
            if g < 0:
                g = 0
            elif g > 255:
                g = 255
            if b < 0:
                b = 0
            elif b > 255:
                b = 255
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    raw_input()
                
                
            
    
def contrast(pic, w, h):
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = pic.getPixelColor(i, j)
            r = c[0] + 2*(c[0]-128)
            g = c[1] + 2*(c[1]-128)
            b = c[2] + 2*(c[2]-128)
            if r < 0:
                r = 0
            elif r > 255:
                r = 255
            if g < 0:
                g = 0
            elif g > 255:
                g = 255
            if b < 0:
                b = 0
            elif b > 255:
                b = 255
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    raw_input()            
      
def oneEighty(pic, w, h):
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(w-1-i, h-1-j)
            pic.setPixelColor(i, j, c[0], c[1], c[2])
    pic.display()
    raw_input()
 
def extremes(pic, w, h): 
                         
    cop = copy(pic, w, h)
    for i in range(0, w-1):
        for j in range(0, h-1):
            c = cop.getPixelColor(i, j)
            r = c[0]
            g = c[1]
            b = c[2]
            if r > g and b:
                r=255
                g=0
                b=0
            elif g > b and r:
                g=255
                r=0
                b=0
            elif b > g and r:
                b=255
                r=0
                g=0
            elif b == g:
                b=255
                g=255
                r=0
            elif r == b:
                r=255
                b=255
                g=0
            elif g == r:
                r=255
                g=255
                b=0
            pic.setPixelColor(i, j, r, g, b)
    pic.display()
    raw_input()
    
def border(pic, w, h): 
    bor = input("How many pixels is your border? ")
    for i in range(0, w):
        for j in range(0, bor+1):
            pic.setPixelColor(i, j, 0, 0, 0)
    for i in range(w-bor, w):
        for j in range(0, h-1):
            pic.setPixelColor(i, j, 0, 0, 0)
    for i in range(0, bor+1):
        for j in range(0, h):
            pic.setPixelColor(i, j, 0, 0, 0)
    for i in range(0, w):
        for j in range(h-bor, h):
            pic.setPixelColor(i, j, 0, 0, 0)
    pic.display()
    raw_input()




def main():
    pic = picture2.Picture("crayons.bmp")
    w = pic.getWidth()
    h = pic.getHeight()
    oneEighty(pic, w, h) 
                         
                         
                         
    
main()
