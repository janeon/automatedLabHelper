





import picture2

def copy(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = picture2.Picture(w,h)
    for x in range(w):   
        for y in range(h):   
            color = pic.getPixelColor(x,y)
            setColor = piccopy.setPixelColor(x,y,color[0],color[1],color[2])
            
    return piccopy

def main():
    try:
        fileName = raw_input("Please enter file name: ")
        pic = picture2.Picture(fileName)
        w = pic.getWidth()
        h = pic.getHeight()
        operation = " "
        while operation != "":
            print("How would you like your picture changed, master?")
            print("Here are your options: flip, mirror, scroll, negative,")
            print("grayscale, colorcycle, zoom, posterize, brightness,")
            print("contrast, blur, rotate180, bluegemgreenvomit or craycray.")
            print("Just hit enter to exit.")
            operation = raw_input("Master's change: ")
            
            if operation == "flip" :
                flip(pic)
            elif operation == "mirror":
                mirror(pic)
            elif operation == "scroll":
                scroll(pic)
            elif operation == "negative":
                negative(pic)
            elif operation == "grayscale":
                grayscale(pic)
            elif  operation == "colorcycle":
                colorcycle(pic)
            elif operation == "zoom":
                zoom(pic)
            elif operation == "posterize":
                posterize(pic)
            elif operation == "brightness":
                brightness(pic)
            elif operation == "contrast":
                contrast(pic)
            elif operation == "blur":
                blur(pic)
            elif operation == "rotate180":
                rotate180(pic)
            elif operation == "bluegemgreenvomit":
                bluegemgreenvomit(pic)
            elif operation == "craycray":
                craycray(pic)
            elif operation == "":
                print("Goodbye!")
            else:
                print("Sorry, that is not a valid option. Please try again.")
            pic.display()
            
    except IOError:
        print("That is not a valid image. Please enter another.")
        main()
    
    
def flip(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic)

    for x in range((w-1),-1,-1):   
        for y in range((h-1),-1,-1):   
            color = piccopy.getPixelColor(w-1-x,y)
            setColor = pic.setPixelColor(x,y,color[0],color[1],color[2])


def mirror(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 
    
    for x in range((w-1),(w-1)//2,-1):
        for y in range((h-1),-1,-1):
            color = piccopy.getPixelColor(w-1-x,y)
            setColor = pic.setPixelColor(x,y,color[0],color[1],color[2])
    for x in range(0,(w-1)//2+1):
        for y in range(0,h):
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,color[0],color[1],color[2])


def scroll(pic):
    try:
        w = pic.getWidth()
        h = pic.getHeight()
        piccopy = copy(pic) 
        d = eval(raw_input("Enter number of pixels to scroll: "))
    
        for x in range(0,w-1):   
            for y in range(0,h-1):
                if x+d >= w:
                    color = piccopy.getPixelColor(x,y)
                    setColor = pic.setPixelColor(((x+d)-w),y,color[0],color[1],color[2])
                else:
                    color = piccopy.getPixelColor((x),y)
                    setColor = pic.setPixelColor((x+d),y,color[0],color[1],color[2])

    except NameError:
        print("That is not a valid number of pixels to scroll. Please try again.")
        scroll(pic)

def negative(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic)

    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,255-color[0],255-color[1],255-color[2])


def grayscale(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic)
    
    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,(color[0]+color[1]+color[2])/3,
            (color[0]+color[1]+color[2])/3,(color[0]+color[1]+color[2])/3)


def rotate180(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 

    for x in range((w-1),-1,-1):   
        for y in range((h-1),-1,-1):   
            color = piccopy.getPixelColor(w-1-x,h-1-y)
            setColor = pic.setPixelColor(x,y,color[0],color[1],color[2])


def colorcycle(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic)
    
    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,color[2],color[0],color[1])


def zoom(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 

    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor((w//4)+x//2,(h//4)+y//2)
            setColor = pic.setPixelColor(x,y,color[0],color[1],color[2])


def posterize(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 

    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,(color[0]//32)*32,
            (color[1]//32)*32,(color[2]//32*32))


def brightness(pic):
    try:
        w = pic.getWidth()
        h = pic.getHeight()
        piccopy = copy(pic) 
        b = eval(raw_input("Enter an integer to change the brightness by: "))
    
        for x in range(0,w):   
            for y in range(0,h):   
                color = piccopy.getPixelColor(x,y)
                if color[0] + b <= 0:
                    setColor = pic.setPixelColor(x,y,0,color[1]+b,color[2]+b)
                if color[1] + b <= 0:
                    setColor = pic.setPixelColor(x,y,color[0]+b,0,color[2]+b)
                if color[2] + b <= 0:
                    setColor = pic.setPixelColor(x,y,color[0]+b,color[1]+b,0)
                if color[0] + b >= 255:
                    setColor = pic.setPixelColor(x,y,255,color[1]+b,color[2]+b)
                if color[1] + b >= 255:
                    setColor = pic.setPixelColor(x,y,color[0]+b,255,color[2]+b)
                if color[2] + b >= 255:
                    setColor = pic.setPixelColor(x,y,color[0]+b,color[1]+b,255)
                else :
                    setColor = pic.setPixelColor(x,y,color[0]+b,color[1]+b,color[2]+b)

    except NameError:
        print("That is not a valid integer to change brightness by. Please try again.")
        brightness(pic)

def contrast(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 

    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,(((color[0]-128)*2)+128),
            (((color[1]-128)*2)+128),(((color[2]-128)*2)+128))


def blur(pic) :
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 
    
    for x in range(1,w-1):
        for y in range(1,h-1):
            color = piccopy.getPixelColor(x,y)
            color1 = piccopy.getPixelColor(x+1,y)
            color2 = piccopy.getPixelColor(x+1,y+1)
            color3 = piccopy.getPixelColor(x-1,y)
            color4 = piccopy.getPixelColor(x-1,y-1)
            color5 = piccopy.getPixelColor(x,y+1)
            color6 = piccopy.getPixelColor(x,y-1)
            color7 = piccopy.getPixelColor(x+1,y-1)
            color8 = piccopy.getPixelColor(x-1,y+1)
            setColor = pic.setPixelColor(x,y,(color[0]+color1[0]+color2[0]+color3[0]+color4[0]+color5[0]+color6[0]+color7[0]+color[0])/9,(color[1]+color1[1]+color[1]+color3[1]+color4[1]+color5[1]+color6[1]+color7[1]+color[1])/9, (color[2]+color1[2]+color2[2]+color3[2]+color4[2]+color5[2]+color6[2]+color7[2]+color[2])/9)

    
def craycray(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 

    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,128-((color[0]%128)*2)+30,128-((color[1]%128)*2)+30,
            128-((color[2]%128)*2)+30)


def bluegemgreenvomit(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    piccopy = copy(pic) 

    for x in range(0,w):   
        for y in range(0,h):   
            color = piccopy.getPixelColor(x,y)
            setColor = pic.setPixelColor(x,y,(color[0]+color[1]+color[2])/3,
           (color[0]+color[1]+color[2])/3,color[2])
        
        
main()