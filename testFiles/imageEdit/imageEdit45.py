







import picture2


def picCopy(pic):
    w = getWidth(pic)
    h = getHeight(pic)
    for x in range(0, w-1):
        for y in range(0, h-1):
            r, g, b = pic.getPixelColor(w, h)
            newpic = pic.setPixelColor(x, y, r, g, b)
    return newpic
    
def HorizontalFlip(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w/2):
        for z in range(0, h-1):
            swap = pic.getPixelColor(y, z)
            color = pic.getPixelColor((w-1)-y, z)
            setColor = pic.setPixelColor(y, z, color[0], color[1], color[2])
            swapColor = pic.setPixelColor((w-1)-y, z, swap[0], swap[1], swap[2])
    pic.display()
    return pic

def HorizontalMirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):  
        for z in range(0, h-1):
            color = pic.getPixelColor(y, z)
            setColor = pic.setPixelColor((w-1)-y, z, color[0], color[1], color[2])
    pic.display()
    return pic

def Scroll(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    roll = input("How many pixels would you like to move the image by? ")
    for y in range(0, w+roll):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z) 
        newImage = pic.setPixelColor((y + roll), z, r, g, b)
    pic.display()  

def Negative(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z) 
            pic.setPixelColor(y, z, 255-r, 255-g, 255-b)
    pic.display()
    input()

def GrayScale(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z)
            avg = r+g+b/3
            pic.setPixelColor(y, z, avg, avg, avg)
    pic.display()
    input()

def ColorCycle(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z)
            pic.setPixelRed(y, z, b)
            pic.setPixelGreen(y, z, r)
            pic.setPixelBlue(y, z, g)
    pic.display()

def Zoom(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(w/4, (3*w)/4):
        for z in range(h/4, (3*h)/4):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z)
            NewR = pic.setPixelRed((3*y)/4, (3*z)/4, r)
            NewG = pic.setPixelGreen((3*y)/4, (3*z)/4, g)  
            NewB = pic.setPixelBlue((3*y)/4, (3*z)/4, b)
    pic.display()

def Posterize(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z)
            newRedvalue = pic.setPixelRed(y, z, r-((r+16)%32))
            newGreenValue = pic.setPixelGreen(y, z, g-((g+16)%32))
            newBlueValue = pic.setPixelBlue(y, z, b-((b+16)%32)) 
    pic.display()

def ChangeBrightness(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    print("Brightness currently at 100%.")
    light = input("How much do you want to increase the brightness? ")
    for y in range(0, w-1):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z)
            BrightRed = pic.setPixelRed(y, z, (100%light)+r)
            BrightGreen = pic.setPixelGreen(y, z, (100%light)+g)
            BrightBlue = pic.setPixelBlue(y, z, (100%light)+b) 
    pic.display()
    input()

def IncreaseContrast(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):
        for z in range(0, h-1):
            r, g, b = pic.getPixelColor(y, z)
            if r % 2 != 0: 
                newRed = pic.setPixelRed(y, z, r-1)
            elif g % 2 != 0:
                newGreen = pic.setPixelGreen(y, z, g-1)
            elif b % 2 != 0:
                newBlue = pic.setPixelBlue(y, z, b-1)
    pic.display()

def Blur(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):
        for z in range(0, h-1):
            r = pic.getPixelRed(y, z)
            g = pic.getPixelGreen(y, z)
            b = pic.getPixelBlue(y, z)
            Redavg = r(y, z) + r(y+1, z+1) + r(y+2, z+2)/3
            Greenavg = g(y,z) + g(y+1, z+1) + g(y+2, z+2)/3
            BlueAvg = b(y,z) + b(y+1, z+1) + b(y+2, z+2)/3
            newColor = pic.setPixelColor(y*3, z*3, Redavg, Greenavg, Blueavg)
                  
    pic.display()

def Rotate(pic):
    vertflippic = VerticalFlip(pic)
    hpic = HorizontalFlip(vertflippic) 
    hpic.display()

def VerticalMirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0, w-1):  
        for z in range(0, h-1):
            color = pic.getPixelColor(y, (h-1)-z)
            setColor = pic.setPixelColor(y, z, color[0], color[1], color[2])
    pic.display()
    return pic

def VerticalFlip(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    for z in range(0, h/2):
        for y in range(0, w-1):
            swap = pic.getPixelColor(y, z)
            color = pic.getPixelColor(y, (h-1)-z)
            setColor = pic.setPixelColor(y, z, color[0], color[1], color[2])
            swapColor = pic.setPixelColor(y, (h-1)-z, swap[0], swap[1], swap[2])
    pic.display()
    return pic


def main():
    print("Welcome to Photoslop 2.0!")
    print("We handle all kinds of photo altering effects!")
    print("Here are the options available:")
    print("")
    print("Horizontal/Vertical Flip")
    print("Horizontal/Vertical Mirror")
    print("Scrolling")
    print("Negative")
    print("Grayscale")
    print("Cycle Color Channels")
    print("Zoom")
    print("Posterize")
    print("Change Brightness")
    print("Increase Contrast")
    print("Blur")
    print("Rotate 180 degrees")
    print("")
    x = raw_input("What photo would you like to edit? ")
    y = raw_input("How would you like to change the photo? ")
    pic = picture2.Picture(x)
    w = pic.getWidth()
    h = pic.getHeight()
    r = pic.getPixelRed(w-1, h-1)
    g = pic.getPixelGreen(w-1, h-1)
    b = pic.getPixelBlue(w-1, h-1)
    
    pic.display()
    try:
        if y == "Horizontal Flip":
            HorizontalFlip(pic)
        elif y == "Vertical Flip":
            VerticalFlip(pic)
        elif y == "Horizontal Mirror":
            HorizontalMirror(pic)
        elif y == "Vertical Mirror":
            VerticalMirror(pic)
        elif y == "Negative":
            Negative(pic)
        elif y == "Grayscale":
            GrayScale(pic)
        elif y == "Cycle Color Channels":
            ColorCycle(pic)
        elif y == "Scroll":
            Scroll(pic)
        elif y == "Zoom":
            
            Zoom(pic)
        elif y == "Posterize":
            Posterize(pic)
        elif y == "Change Brightness":
            ChangeBrightness(pic)
        elif y == "Increase Contrast":
            
            IncreaseContrast(pic)
        elif y == "Blur":
            
            Blur(pic)
        elif y == "Rotate":
            Rotate(pic)
    except SyntaxError:
        print("Sorry, that is not a valid command. Try again.")
    except ImportError:
        print("Sorry, the program cannot display this file. Try again.")
    input()
        
main()
    