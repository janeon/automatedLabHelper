





import picture2
import random

def Flip(x, y, pic, copy):
    for i in range(0, y-1):
        for j in range(0, x-1):
            r, g, b = pic.getPixelColor(j, i)
            n = (x-1)-j
            copy.setPixelColor(n, i, r, g, b)
    copy.display()
    raw_input()
            
def Mirror(x, y, pic, copy):
    for i in range(0, y-1):
       for j in range(0, x/2+1):
            r, g, b = pic.getPixelColor(j, i)
            copy.setPixelColor(j, i, r, g, b)
    for k in range(0, y-1):
        for l in range(0, x/2+1):
            r, g, b = pic.getPixelColor(l,k)
            n = (x-1)-l
            copy.setPixelColor(n, k, r, g, b)
    copy.display()
    raw_input()
    
def Scroll(x, y, pic, copy):
    n = input("Enter number of pixels to scroll: ")
    for i in range(0, y-1):
        for j in range(0, x-1):
            r, g, b = pic.getPixelColor(j, i)
            p = j+n
            l = p//x
            if p > x:
                u = p-(l*x)
                copy.setPixelColor(u, i, r, g, b)
            elif p < x:
                copy.setPixelColor(p, i, r, g, b)
    copy.display()
    raw_input()
    
def Negative(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            new_r = copy.setPixelRed(i, j, 255-r)
            new_g = copy.setPixelGreen(i, j, 255-g)
            new_b = copy.setPixelBlue(i, j, 255-b)
    copy.display()
    raw_input()
    
def Gray(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            av = (r+g+b)/3
            new_r = copy.setPixelRed(i, j, av)
            new_g = copy.setPixelGreen(i, j, av)
            new_b = copy.setPixelBlue(i, j, av)
    copy.display()
    raw_input()
    
def Cycle(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            new_r = copy.setPixelRed(i, j, b)
            new_g = copy.setPixelGreen(i, j, r)
            new_b = copy.setPixelBlue(i, j, g)
    copy.display()
    raw_input()
            
def Zoom(x, y, pic, copy):
    for k in range(0, y-1):
        for p in range(0, x-1):
            r, g, b = pic.getPixelColor(x/4+p//2, y/4+k//2)
            copy.setPixelColor(p, k, r, g, b)
    copy.display()
    raw_input()
    
def Posterize(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            new_r = copy.setPixelRed(i, j, Round(r))
            new_g = copy.setPixelGreen(i, j, Round(g))
            new_b = copy.setPixelBlue(i, j, Round(b))
    copy.display()
    raw_input()
    
def Bright(x, y, pic, copy):
    change = input("Enter a value: ")
    for i in range(0, x-1):
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            new_r = r + change
            new_g = g + change
            new_b = b + change
            if new_r > 255:
                new_r = 255
            elif new_r < 0:
                new_r = 0
            if new_g > 255:
                new_g = 255
            elif new_g < 0:
                new_g = 0
            if new_b > 255:
                new_b = 255
            elif new_b < 0:
                new_b = 0
            copy.setPixelColor(i, j, new_r, new_g, new_b)
    copy.display()
    raw_input()

def Contrast(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            if r != 128:
                diff_r = r - 128
                new_r = 128+(diff_r*2)
                if new_r > 255:
                    new_r = 255
                elif new_r < 0:
                    new_r = 0
            if g != 128:
                diff_g = g - 128
                new_g = 128+(diff_g*2)
                if new_g > 255:
                    new_g = 255
                elif new_g < 0:
                    new_g = 0
            if b != 128:
                diff_b = b - 128
                new_b = 128+(diff_b*2)
                if new_b > 255:
                    new_b = 255
                elif new_b < 0:
                    new_b = 0
            copy.setPixelColor(i, j, new_r, new_g, new_b)
    copy.display()
    raw_input()
    
def Blur(x, y, pic, copy):
    for i in range(1,y-1):
        for j in range(1,x-1):
            r1,g1,b1=pic.getPixelColor(j,i)
            r2,g2,b2=pic.getPixelColor(j+1,i)
            r3,g3,b3=pic.getPixelColor(j+1,i+1)
            r4,g4,b4=pic.getPixelColor(j+1,i-1)
            r5,g5,b5=pic.getPixelColor(j,i-1)
            r6,g6,b6=pic.getPixelColor(j,i+1)
            r7,g7,b7=pic.getPixelColor(j-1,i)
            r8,g8,b8=pic.getPixelColor(j-1,i+1)
            r9,g9,b9=pic.getPixelColor(j-1,i-1)
            rultimate=(r1+r2+r3+r4+r5+r6+r7+r8+r9)/9
            gultimate=(g1+g2+g3+g4+g5+g6+g7+g8+g9)/9
            bultimate=(b1+b2+b3+b4+b5+b6+b7+b8+b9)/9
            copy.setPixelColor(j,i,rultimate,gultimate,bultimate)
    for y in range(1,y-1):
        redgey1,gedgey1,bedgey1=pic.getPixelColor(0,y)
        redgey2,gedgey2,bedgey2=pic.getPixelColor(1,y)
        redgey3,gedgey3,bedgey3=pic.getPixelColor(1,y+1)
        redgey4,gedgey4,bedgey4=pic.getPixelColor(1,y-1)
        redgey5,gedgey5,bedgey5=pic.getPixelColor(0,y+1)
        redgey6,gedgey6,bedgey6=pic.getPixelColor(0,y-1)
        rultimatedge=(redgey1+redgey2+redgey3+redgey4+redgey5+redgey6)/6
        gultimatedge=(gedgey1+gedgey2+gedgey3+gedgey4+gedgey5+gedgey6)/6
        bultimatedge=(bedgey1+bedgey2+bedgey3+bedgey4+bedgey5+bedgey6)/6
        copy.setPixelColor(0,y,rultimatedge,gultimatedge,bultimatedge)
    for y in range(1,y+1):
        redgey1,gedgey1,bedgey1=pic.getPixelColor(x-1,y)
        redgey2,gedgey2,bedgey2=pic.getPixelColor(x-2,y)
        redgey3,gedgey3,bedgey3=pic.getPixelColor(x-2,y+1)
        redgey4,gedgey4,bedgey4=pic.getPixelColor(x-2,y-1)
        redgey5,gedgey5,bedgey5=pic.getPixelColor(x-1,y+1)
        redgey6,gedgey6,bedgey6=pic.getPixelColor(x-1,y-1)
        rultimatedge=(redgey1+redgey2+redgey3+redgey4+redgey5+redgey6)/6
        gultimatedge=(gedgey1+gedgey2+gedgey3+gedgey4+gedgey5+gedgey6)/6
        bultimatedge=(bedgey1+bedgey2+bedgey3+bedgey4+bedgey5+bedgey6)/6
        copy.setPixelColor(x-1,y,rultimatedge,gultimatedge,bultimatedge)
    for x in range(1,x-1):
        rtop1,gtop1,btop1=pic.getPixelColor(x,0)
        rtop2,gtop2,btop2=pic.getPixelColor(x,1)
        rtop3,gtop3,btop3=pic.getPixelColor(x-1,1)
        rtop4,gtop4,btop4=pic.getPixelColor(x+1,1)
        rtop5,gtop5,btop5=pic.getPixelColor(x-1,0)
        rtop6,gtop6,btop6=pic.getPixelColor(x+1,0)
        rtopultimate=(rtop1+rtop2+rtop3+rtop4+rtop5+rtop6)/6
        gtopultimate=(gtop1+gtop2+gtop3+gtop4+gtop5+gtop6)/6
        btopultimate=(btop1+btop2+btop3+btop4+btop5+btop6)/6
        copy.setPixelColor(x,0,rtopultimate,gtopultimate,btopultimate)
    for x in range(1,x-1):
        rbottom1,gbottom1,bbottom1=pic.getPixelColor(x,y-1)
        rbottom2,gbottom2,bbottom2=pic.getPixelColor(x,y-2)
        rbottom3,gbottom3,bbottom3=pic.getPixelColor(x-1,y-2)
        rbottom4,gbottom4,bbottom4=pic.getPixelColor(x+1,y-2)
        rbottom5,gbottom5,bbottom5=pic.getPixelColor(x-1,y-1)
        rbottom6,gbottom6,bbottom6=pic.getPixelColor(x+1,y-1)
        rtopultimate=(rbottom1+rbottom2+rbottom3+rbottom4+rbottom5+rbottom6)/6
        gtopultimate=(gbottom1+gbottom2+gbottom3+gbottom4+gbottom5+gbottom6)/6
        btopultimate=(bbottom1+bbottom2+bbottom3+bbottom4+bbottom5+bbottom6)/6
        copy.setPixelColor(x,y+1,rtopultimate,gtopultimate,btopultimate)
    rhorn5,ghorn5,bhorn5=pic.getPixelColor(x+3,0)
    rhorn6,ghorn6,bhorn6=pic.getPixelColor(x+3,1)
    rhorn7,ghorn7,bhorn7=pic.getPixelColor(x+2,1)
    rhorn8,ghorn8,bhorn8=pic.getPixelColor(x+2,0)
    rhornultimate=(rhorn5+rhorn6+rhorn7+rhorn8)/4
    ghornultimate=(ghorn5+ghorn6+ghorn7+ghorn8)/4
    bhornultimate=(bhorn5+bhorn6+bhorn7+bhorn8)/4
    copy.setPixelColor(x+3,0,rhornultimate,ghornultimate,bhornultimate)
    rcorn1,gcorn1,bcorn1=pic.getPixelColor(0,0)
    rcorn2,gcorn2,bcorn2=pic.getPixelColor(0,1)
    rcorn3,gcorn3,bcorn3=pic.getPixelColor(1,1)
    rcorn4,gcorn4,bcorn4=pic.getPixelColor(1,0)
    rcornultimate=(rcorn1+rcorn2+rcorn3+rcorn4)/4
    gcornultimate=(gcorn1+gcorn2+gcorn3+gcorn4)/4
    bcornultimate=(bcorn1+bcorn2+bcorn3+bcorn4)/4
    copy.setPixelColor(0,0,rcornultimate,gcornultimate,bcornultimate)
    rdcorn1,gdcorn1,bdcorn1=pic.getPixelColor(x+3,y+1)
    rdcorn2,gdcorn2,bdcorn2=pic.getPixelColor(x+2,y+1)
    rdcorn3,gdcorn3,bdcorn3=pic.getPixelColor(x+3,y)
    rdcorn4,gdcorn4,bdcorn4=pic.getPixelColor(x+2,y)
    rdcornultimate=(rdcorn1+rdcorn2+rdcorn3+rdcorn4)/4
    gdcornultimate=(gdcorn1+gdcorn2+gdcorn3+gdcorn4)/4
    bdcornultimate=(bdcorn1+bdcorn2+bdcorn3+bdcorn4)/4
    copy.setPixelColor(x+3,y+1,rdcornultimate,gdcornultimate,bdcornultimate)
    rccorn1,gccorn1,bccorn1=pic.getPixelColor(1,y+1)
    rccorn2,gccorn2,bccorn2=pic.getPixelColor(0,y+1)
    rccorn3,gccorn3,bccorn3=pic.getPixelColor(1,y)
    rccorn4,gccorn4,bccorn4=pic.getPixelColor(0,y)
    rccornultimate=(rccorn1+rccorn2+rccorn3+rccorn4)/4
    gccornultimate=(gccorn1+gccorn2+gccorn3+gccorn4)/4
    bccornultimate=(bccorn1+bccorn2+bccorn3+bccorn4)/4
    copy.setPixelColor(0,y+1,rccornultimate,gccornultimate,bccornultimate)
   
    copy.display()
    raw_input()
    
def Rotate(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r, g, b = pic.getPixelColor(i, j)
            n = (y-1)-j
            copy.setPixelColor(i, n, r, g, b)
    copy.display()
    raw_input()
    
def Watermark(x, y, pic, copy):
    awesome=picture2.Picture("tom.bmp")
   
    o=awesome.getWidth()
    m=awesome.getHeight()
   
    for i in range(0,y-1):
            for j in range(0,x-1):
           
                r,g,b=pic.getPixelColor(j,i)
                copy.setPixelColor(j,i,r,g,b)
    for i in range(0,m-1):
        for j in range(0,o-1):
           
            n,m,l=awesome.getPixelColor(j,i)
            if n<150:
                if m<150:
                    if l<150:
                        copy.setPixelColor(j+x/4,i+y/4,r-n,g-m,b-l)
    
    copy.display()
    raw_input()
    
def BlackAndWhite(x, y, pic, copy):
    for i in range(0, x-1):
        for j in range(0, y-1):
            r, g, b = pic.getPixelColor(i, j)
            if r<100:
                if g<100:
                    if b<100:
                        copy.setPixelColor(i, j, 0, 0, 0)
            else:
                copy.setPixelColor(i, j, 255, 255, 255)
    copy.display()
    raw_input()

def JustForDashie(x, y, pic, copy):
    for i in range(0, x-1):  
        for j in range(0, y-1):
            r = pic.getPixelRed(i, j)
            g = pic.getPixelGreen(i, j)
            b = pic.getPixelBlue(i, j)
            if r != 255 and g != 255 and b != 255:
                r = random.randrange(256)
                g = random.randrange(256)
                b = random.randrange(256)
            copy.setPixelColor(i, j, r, g, b)
    copy.display()
    raw_input()

def Round(n):
    if n >= 0 and n <= 15:
        return 0
    elif n >= 16 and n <= 47:
        return 32
    elif n >= 48 and n <= 79:
        return 64
    elif n >= 80 and n <= 111:
        return 96
    elif n >= 112 and n <= 143:
        return 128
    elif n >= 144 and n <= 175:
        return 160
    elif n >= 176 and n <= 207:
        return 192
    elif n >= 208 and n <= 239:
        return 224
    else:
        return 255
        
def main():
    print("Welcome, User!  I'd like to inform you just how fortunate you are to have upon this, your very own image editor!")
    print
    done = False
    while not done:
        try:
            image = raw_input("Now, which image would you like to edit? ")
            pic = picture2.Picture(image)
            x = pic.getWidth()
            y = pic.getHeight()
            copy = picture2.Picture(x, y)
            done = True
        except Exception as e:
            print("I couldn't find that file, and I looked really hard.  Pick another one, please.")
    pic.display()
    raw_input()
    print
    print("Purdy, idn't it? Now about those editing commands...")
    print
    done = False
    while not done:
        try:
            print("The commands available for editing your image are:")
            print("Flip, Mirror, Scroll, Negative, Grayscale, Cycle Colors, Zoom, Posterize,")
            print("Brightness, Contrast, Blur, Rotate, Black and White, and Watermark.")
            print
            command = raw_input("How would you like to edit your image? ")
            if command == "flip":
                Flip(x, y, pic, copy)
            elif command.lower() == "mirror":
                Mirror(x, y, pic, copy)
            elif command.lower() == "scroll":
                Scroll(x, y, pic, copy)
            elif command.lower() == "negative":
                Negative(x, y, pic, copy)
            elif command.lower() == "grayscale":
                Gray(x, y, pic, copy)
            elif command.lower() == "cycle colors":
                Cycle(x, y, pic, copy)
            elif command.lower() == "zoom":
                Zoom(x, y, pic, copy)
            elif command.lower() == "posterize":
                Posterize(x, y, pic, copy)
            elif command.lower() == "brightness":
                Bright(x, y, pic, copy)
            elif command.lower() == "contrast":
                Contrast(x, y, pic, copy)
            elif command.lower() == "blur":
                Blur(x, y, pic, copy)
            elif command.lower() == "rotate":
                Rotate(x, y, pic, copy)
            elif command.lower() == "black and white":
                BlackAndWhite(x, y, pic, copy)
            elif command.lower() == "watermark":
                Watermark(x, y, pic, copy)
        except Exception as e:
            print("See, that's why I gave you the list of possible commands.  Try to pick one of those, eh?")
        print("Behold, %s!") % command
        pic = copy
        more = raw_input("Would you care to further edit your image? ")
        print
        if more.lower() == "no":
            print("Okay, byesies!")
            done = True
        else:
            print("Well in that case, what would you like to change next?")
    
main()
    

