







import picture2

def CopyPic(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    copyPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(i,j)
            copyPic.setPixelRed(i,j,red)
            green=pic.getPixelGreen(i,j)
            copyPic.setPixelGreen(i,j,green)
            blue=pic.getPixelBlue(i,j)
            copyPic.setPixelBlue(i,j,blue)
    return copyPic

def Flip_Horizontally(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(WIDTH-1-i,j)
            newPic.setPixelRed(i,j,red)
            green=pic.getPixelGreen(WIDTH-1-i,j)
            newPic.setPixelGreen(i,j,green)
            blue=pic.getPixelBlue(WIDTH-1-i,j)
            newPic.setPixelBlue(i,j,blue)
    return newPic
    
    
def Mirror_Horizontally(pic):
    WIDTH=pic.getWidth
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,(WIDTH)//2):
        for j in range(0,HEIGHT):
            red=pic.getPixelRed(i,j)
            newPic.setPixelRed(i,j,red)
            green=pic.getPixelGreen(i,j)
            newPic.setPixelGreen(i,j,green)
            blue=pic.getPixelBlue(i,j)
            newPic.setPixelBlue(i,j,blue)
    for i in range ((WIDTH)//2,WIDTH):
        for j in range(0,HEIGHT):
            red=pic.getPixelRed(WIDTH-i,j)
            newPic.setPixelRed(i,j,red)
            green=pic.getPixelGreen(WIDTH-i,j)
            newPic.setPixelGreen(i,j,green)
            blue=pic.getPixelBlue(WIDTH-i,j)
            newPic.setPixelBlue(i,j,blue)
    return newPic

def Scroll_Horizontally(pic):
    scrollingNumber=eval(raw_input("Please enter the number of pixels you would like your image to be shifted to the left: "))
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            if i+scrollingNumber<WIDTH:
                red=pic.getPixelRed(i+scrollingNumber,j)
            else:
                red=pic.getPixelRed(i+scrollingNumber-WIDTH,j)
            newPic.setPixelRed(i,j,red)
            if i+scrollingNumber<WIDTH:
                blue=pic.getPixelBlue(i+scrollingNumber,j)
            else:
                blue=pic.getPixelBlue(i+scrollingNumber-WIDTH,j)
            newPic.setPixelBlue(i,j,blue)
            if i+scrollingNumber<WIDTH:
                green=pic.getPixelGreen(i+scrollingNumber,j)
            else:
                green=pic.getPixelGreen(i+scrollingNumber-WIDTH,j)
            newPic.setPixelGreen(i,j,green)
    return newPic
    
def Make_Negative(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(i,j)
            newPic.setPixelRed(i,j,250-red)
            green=pic.getPixelGreen(i,j)
            newPic.setPixelGreen(i,j,250-green)
            blue=pic.getPixelBlue(i,j)
            newPic.setPixelBlue(i,j,250-blue)
    return newPic
    
def Make_Grayscale(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range(0,HEIGHT):
            red=pic.getPixelRed(i,j)
            green=pic.getPixelGreen(i,j)
            blue=pic.getPixelBlue(i,j)
            avg=(red+green+blue)/3
            newPic.setPixelRed(i,j,avg)
            newPic.setPixelGreen(i,j,avg)
            newPic.setPixelBlue(i,j,avg)
    return newPic
    
def Cycle_Color_Channels(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range(0,HEIGHT):
            red=pic.getPixelRed(i,j)
            green=pic.getPixelGreen(i,j)
            blue=pic.getPixelBlue(i,j)
            newPic.setPixelBlue(i,j,green)
            newPic.setPixelRed(i,j,blue)
            newPic.setPixelGreen(i,j,red)
    return newPic














            

def Posterize(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(i,j)
            green=pic.getPixelGreen(i,j)
            blue=pic.getPixelBlue(i,j)
            red=(red//32)*32
            green=(green//32)*32
            blue=(blue//32)*32
            newPic.setPixelRed(i,j,red)
            newPic.setPixelGreen(i,j,green)
            newPic.setPixelBlue(i,j,blue)
    return newPic
    

def Change_Brightness(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    scalingInteger=eval(raw_input("Please enter an integer value between -250 and 250: "))
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(i,j)
            green=pic.getPixelGreen(i,j)
            blue=pic.getPixelBlue(i,j)
            red=red+scalingInteger
            if red>255:
                red=255
            elif red<0:
                red=0
            else:
                red=red
            newPic.setPixelRed(i,j,red)
            blue=blue+scalingInteger
            if blue>255:
                blue=255
            elif blue<0:
                blue=0
            else:
                blue=blue
            newPic.setPixelBlue(i,j,blue)
            green=green+scalingInteger
            if green>255:
                green=255
            elif green<0:
                green=0
            else:
                green=green
            newPic.setPixelGreen(i,j,green)
    return newPic

def Increase_Contrast(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(i,j)
            green=pic.getPixelGreen(i,j)
            blue=pic.getPixelBlue(i,j)
            if red==128:
                newPic.setPixelRed(i,j,red)
            elif red<128:
                red=red-(128-red)*2
                newPic.setPixelRed(i,j,red)
            else:
                red=red+(red-128)*2
                newPic.setPixelRed(i,j,red)
            if green==128:
                newPic.setPixelGreen(i,j,green)
            elif green<128:
                green=green-(128-green)*2
                newPic.setPixelGreen(i,j,green)
            else:
                green=green+(green-128)*2
                newPic.setPixelGreen(i,j,green)
            if blue==128:
                newPic.setPixelBlue(i,j,blue)
            elif blue<128:
                blue=blue-(128-blue)*2
                newPic.setPixelBlue(i,j,blue)
            else:
                blue=blue+(blue-128)*2
                newPic.setPixelBlue(i,j,blue)
    return newPic

def Blur(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newpic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red1=pic.getPixelRed(i-1,j-1)
            red2=pic.getPixelRed(i,j-1)
            red3=pic.getPixelRed(i+1,j-1)
            red4=pic.getPixelRed(i-1,j)
            red5=pic.getPixelRed(i,j)
            red6=pic.getPixelRed(i+1,j)
            red7=pic.getPixelRed(i-1,j+1)
            red8=pic.getPixelRed(i,j+1)
            red9=pic.getPixelRed(i+1,j+1)
            green1=pic.getPixelGreen(i-1,j-1)
            green2=pic.getPixelGreen(i,j-1)
            green3=pic.getPixelGreen(i+1,j-1)
            green4=pic.getPixelGreen(i-1,j)
            green5=pic.getPixelGreen(i,j)
            green6=pic.getPixelGreen(i+1,j)
            green7=pic.getPixelGreen(i-1,j+1)
            green8=pic.getPixelGreen(i,j+1)
            green9=pic.getPixelGreen(i+1,j+1)
            blue1=pic.getPixelBlue(i-1,j-1)
            blue2=pic.getPixelBlue(i,j-1)
            blue3=pic.getPixelBlue(i+1,j-1)
            blue4=pic.getPixelBlue(i-1,j)
            blue5=pic.getPixelBlue(i,j)
            blue6=pic.getPixelBlue(i+1,j)
            blue7=pic.getPixelBlue(i-1,j+1)
            blue8=pic.getPixelBlue(i,j+1)
            blue9=pic.getPixelBlue(i+1,j+1)
            if i==0:
                if j==0:
                    red1a=(red5+red8+red6+red9)//4
                    blue1a=(blue5+blue8+blue6+blue9)//4
                    green1a=(green5+green8+green6+green9)//4
                    newpic.setPixelRed(i,j,red1a)
                    newpic.setPixelGreen(i,j,green1a)
                    newpic.setPixelBlue(i,j,blue1a)
                elif j==HEIGHT-1:
                    red1b=(red5+red2+red6+red3)//4
                    green1b=(green5+green2+green6+green3)//4
                    blue1b=(blue5+blue2+blue6+blue3)//4
                    newpic.setPixelRed(i,j,red1b)
                    newpic.setPixelGreen(i,j,green1b)
                    newpic.setPixelBlue(i,j,blue1b)
                else:
                    red1c=(pic.getPixelRed(i,j)+pic.getPixelRed(i,j-1)+pic.getPixelRed(i,j+1)+pic.getPixelRed(i+1,j-1)+pic.getPixelRed(i+1,j)+pic.getPixelRed(i+1,j+1))//6
                    green1c=(pic.getPixelGreen(i,j)+pic.getPixelGreen(i,j-1)+pic.getPixelGreen(i,j+1)+pic.getPixelGreen(i+1,j-1)+pic.getPixelGreen(i+1,j)+pic.getPixelGreen(i+1,j+1))//6
                    blue1c=(pic.getPixelBlue(i,j)+pic.getPixelBlue(i,j-1)+pic.getPixelBlue(i,j+1)+pic.getPixelBlue(i+1,j-1)+pic.getPixelBlue(i+1,j)+pic.getPixelBlue(i+1,j+1))//6
                    newpic.setPixelRed(i,j,red1c)
                    newpic.setPixelGreen(i,j,green1c)
                    newpic.setPixelBlue(i,j,blue1c)
            elif i==WIDTH-1:
                if j==0:
                    red1=(pic.getPixelRed(i,j)+pic.getPixelRed(i-1,j)+pic.getPixelRed(i-1,j+1)+pic.getPixelRed(i,j+1))//4
                    green1=(pic.getPixelGreen(i,j)+pic.getPixelGreen(i-1,j)+pic.getPixelGreen(i-1,j+1)+pic.getPixelGreen(i,j+1))//4
                    blue1=(pic.getPixelBlue(i,j)+pic.getPixelBlue(i-1,j)+pic.getPixelBlue(i-1,j+1)+pic.getPixelBlue(i,j+1))//4
                    newpic.setPixelRed(i,j,red1)
                    newpic.setPixelGreen(i,j,green1)
                    newpic.setPixelBlue(i,j,blue1)
                elif j==HEIGHT-1:
                    red1=(pic.getPixelRed(i,j)+pic.getPixelRed(i-1,j)+pic.getPixelRed(i-1,j-1)+pic.getPixelRed(i,j-1))//4
                    green1=(pic.getPixelGreen(i,j)+pic.getPixelGreen(i-1,j)+pic.getPixelGreen(i-1,j-1)+pic.getPixelGreen(i,j-1))//4
                    blue1=(pic.getPixelBlue(i,j)+pic.getPixelBlue(i-1,j)+pic.getPixelBlue(i-1,j-1)+pic.getPixelBlue(i,j-1))//4
                    newpic.setPixelRed(i,j,red1)
                    newpic.setPixelGreen(i,j,green1)
                    newpic.setPixelBlue(i,j,blue1)
                else:
                    red1=(pic.getPixelRed(i,j)+pic.getPixelRed(i,j-1)+pic.getPixelRed(i,j+1)+pic.getPixelRed(i-1,j-1)+pic.getPixelRed(i-1,j)+pic.getPixelRed(i-1,j+1))//6
                    green1=(pic.getPixelGreen(i,j)+pic.getPixelGreen(i,j-1)+pic.getPixelGreen(i,j+1)+pic.getPixelGreen(i-1,j-1)+pic.getPixelGreen(i-1,j)+pic.getPixelGreen(i-1,j+1))//6
                    blue1=(pic.getPixelBlue(i,j)+pic.getPixelBlue(i,j-1)+pic.getPixelBlue(i,j+1)+pic.getPixelBlue(i-1,j-1)+pic.getPixelBlue(i-1,j)+pic.getPixelBlue(i-1,j+1))//6
                    newpic.setPixelRed(i,j,red1)
                    newpic.setPixelGreen(i,j,green1)
                    newpic.setPixelBlue(i,j,blue1)
            elif j==0:
                red1=(pic.getPixelRed(i,j)+pic.getPixelRed(i-1,j)+pic.getPixelRed(i+1,j)+pic.getPixelRed(i-1,j+1)+pic.getPixelRed(i,j+1)+pic.getPixelRed(i+1,j+1))//6
                green1=(pic.getPixelGreen(i,j)+pic.getPixelGreen(i-1,j)+pic.getPixelGreen(i+1,j)+pic.getPixelGreen(i-1,j+1)+pic.getPixelGreen(i,j+1)+pic.getPixelGreen(i+1,j+1))//6 
                blue1=(pic.getPixelBlue(i,j)+pic.getPixelBlue(i-1,j)+pic.getPixelBlue(i+1,j)+pic.getPixelBlue(i-1,j+1)+pic.getPixelBlue(i,j+1)+pic.getPixelBlue(i+1,j+1))//6
                newpic.setPixelRed(i,j,red1)
                newpic.setPixelGreen(i,j,green1)
                newpic.setPixelBlue(i,j,blue1)
            elif j==WIDTH-1:
                red1=(pic.getPixelRed(i,j)+pic.getPixelRed(i-1,j)+pic.getPixelRed(i+1,j)+pic.getPixelRed(i-1,j-1)+pic.getPixelRed(i,j-1)+pic.getPixelRed(i+1,j-1))//6
                green1=(pic.getPixelGreen(i,j)+pic.getPixelGreen(i-1,j)+pic.getPixelGreen(i+1,j)+pic.getPixelGreen(i-1,j-1)+pic.getPixelGreen(i,j-1)+pic.getPixelGreen(i+1,j-1))//6
                blue1=(pic.getPixelBlue(i,j)+pic.getPixelBlue(i-1,j)+pic.getPixelBlue(i+1,j)+pic.getPixelBlue(i-1,j-1)+pic.getPixelBlue(i,j-1)+pic.getPixelBlue(i+1,j-1))//6
                newpic.setPixelRed(i,j,red1)
                newpic.setPixelGreen(i,j,green1)
                newpic.setPixelBlue(i,j,blue1)
            else:
                red1=(pic.getPixelRed(i-1,j-1)+pic.getPixelRed(i,j-1)+pic.getPixelRed(i+1,j-1)+pic.getPixelRed(i-1,j)+pic.getPixelRed(i,j)+pic.getPixelRed(i+1,j)+pic.getPixelRed(i-1,j+1)+pic.getPixelRed(i,j+1)+pic.getPixelRed(i+1,j+1))//9
                green1=(pic.getPixelGreen(i-1,j-1)+pic.getPixelGreen(i,j-1)+pic.getPixelGreen(i+1,j-1)+pic.getPixelGreen(i-1,j)+pic.getPixelGreen(i,j)+pic.getPixelGreen(i+1,j)+pic.getPixelGreen(i-1,j+1)+pic.getPixelGreen(i,j+1)+pic.getPixelGreen(i+1,j+1))//9
                blue1=(pic.getPixelBlue(i-1,j-1)+pic.getPixelBlue(i,j-1)+pic.getPixelBlue(i+1,j-1)+pic.getPixelBlue(i-1,j)+pic.getPixelBlue(i,j)+pic.getPixelBlue(i+1,j)+pic.getPixelBlue(i-1,j+1)+pic.getPixelBlue(i,j+1)+pic.getPixelBlue(i+1,j+1))//9
            return newpic
        
def Rotate_180_Degrees(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range(0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(WIDTH-1-i,HEIGHT-1-j)
            green=pic.getPixelGreen(WIDTH-1-i,HEIGHT-1-j)
            blue=pic.getPixelBlue(WIDTH-1-i,HEIGHT-1-j)
            newPic.setPixelRed(i,j,red)
            newPic.setPixelGreen(i,j,green)
            newPic.setPixelBlue(i,j,blue)
    return newPic

def Border_Effect(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    R,G,B=eval(raw_input("Choose the color of your boarder by inputting the values of the R,G,B: "))
    borderThickness=eval(raw_input("Enter an integer between zero and half of the smallest dimension of the picture to be the thickness of your border: "))
    for i in range (0,borderThickness):
        for j in range(0,HEIGHT):
            newPic.setPixelRed(i,j,R)
            newPic.setPixelGreen(i,j,G)
            newPic.setPixelBlue(i,j,B)
    for i in range (WIDTH-borderThickness,WIDTH):
        for j in range(0,HEIGHT):
            newPic.setPixelRed(i,j,R)
            newPic.setPixelGreen(i,j,G)
            newPic.setPixelBlue(i,j,B)
    for j in range (0,borderThickness):
        for i in range (borderThickness,WIDTH-borderThickness):
            newPic.setPixelRed(i,j,R)
            newPic.setPixelGreen(i,j,G)
            newPic.setPixelBlue(i,j,B)
    for j in range (HEIGHT-borderThickness,HEIGHT):
        for i in range (borderThickness,WIDTH-borderThickness):
            newPic.setPixelRed(i,j,R)
            newPic.setPixelGreen(i,j,G)
            newPic.setPixelBlue(i,j,B)
    for i in range(borderThickness,WIDTH-borderThickness):
        for j in range(borderThickness,HEIGHT-borderThickness):
            red=pic.getPixelRed(i,j)
            newPic.setPixelRed(i,j,red)
            green=pic.getPixelGreen(i,j)
            newPic.setPixelGreen(i,j,green)
            blue=pic.getPixelBlue(i,j)
            newPic.setPixelBlue(i,j,blue)
            
    return newPic
            
    
def Antique(pic):
    WIDTH=pic.getWidth()
    HEIGHT=pic.getHeight()
    newPic=picture2.Picture(WIDTH,HEIGHT)
    for i in range (0,WIDTH):
        for j in range (0,HEIGHT):
            red=pic.getPixelRed(i,j)
            green=pic.getPixelGreen(i,j)
            blue=pic.getPixelBlue(i,j)
            red=red+green+blue
            green=green+blue
            blue=blue
            if red>255:
                red=255
            if green>255:
                green=255
            newPic.setPixelRed(i,j,red)
            newPic.setPixelGreen(i,j,green)
            newPic.setPixelBlue(i,j,blue)
    
    return newPic
    
def main():
    goodInput=False
    print"Welcome to this image editing program!"
    fileName=raw_input("Please enter the image file you'd like loaded: ")
    originalPic=picture2.Picture(fileName)
    cPic=CopyPic(originalPic)
    cPic.display()
    while not goodInput:
        x=raw_input("Would you like to keep editting? Please type yes or no. ")
        y="no"
        if x[1]==y[1]:
            break
        else:
            z=raw_input("What effect would you like to use? Please choose between a.) Flip Horizontally b.) Mirror Horizontally c.) Scroll Horizontally d.) Make Negative e.) Make Grayscale f.) Cycle Color Channel g.) Zoom h.) Posterize i.) Change Brightness j.) Increase Contrast k.) Blur l.) Rotate 180 Degrees m.) Add Border n.) Antique: ")
        a="a"
        b="b"
        c='c'
        d='d'
        e='e'
        f='f'
        g='g'
        h='h'
        i='i'
        j='j'
        k='k'
        l='l'
        m='m'
        n='n'
        if z[0]==a[0]:
            dPic=Flip_Horizontally(cPic)
            dPic.display()
        elif z[0]==b[0]:
            dPic=Mirror_Horizontally(cPic)
            dPic.display()
        elif z[0]==c[0]:
            dPic=Scroll_Horizontally(cPic)
            dPic.display()
        elif z[0]==d[0]:
            dPic=Make_Negative(cPic)
            dPic.display()
        elif z[0]==e[0]:
            dPic=Make_Grayscale(cPic)
            dPic.display()
        elif z[0]==f[0]:
            dPic=Cycle_Color_Channels(cPic)
            dPic.display()
        elif z[0]==g[0]:
            dPic=Zoom(cPic)
            dPic.display()
        elif z[0]==h[0]:
            dPic=Posterize(cPic)
            dPic.display()
        elif z[0]==i[0]:
            dPic=Change_Brightness(cPic)
            dPic.display()
        elif z[0]==j[0]:
            dPic=Increase_Contrast(cPic)
            dPic.display()
        elif z[0]==k[0]:
            dPic=Blur(cPic)
            dPic.display()
        elif z[0]==l[0]:
            dPic=Rotate_180_Degrees(cPic)
            dPic.display()
        elif z[0]==m[0]:
            dPic=Border_Effect(cPic)
            dPic.display()
        else:
            dPic=Antique(cPic)
            dPic.display()
    
main()






