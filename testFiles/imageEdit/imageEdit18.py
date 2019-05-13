





import picture2



















def copy(image):
    w = image.getWidth()
    h = image.getHeight()
    
    newImage = picture2.Picture(w,h)
    
    for i in range(w):
        for j in range(h):
            newImage.setPixelRed(i,j,image.getPixelRed(i,j))
            newImage.setPixelGreen(i,j,image.getPixelGreen(i,j))
            newImage.setPixelBlue(i,j,image.getPixelBlue(i,j))
            
    return newImage

def flip(image):
    w = image.getWidth()
    h = image.getHeight()
    
    otherImage = copy(image)
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(w - 1 - i,j,otherImage.getPixelRed(i,j))
            image.setPixelGreen(w - 1 - i,j,otherImage.getPixelGreen(i,j))
            image.setPixelBlue(w - 1 - i,j,otherImage.getPixelBlue(i,j))
            
    return image

def mirror(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w/2):
        for j in range(h):
            image.setPixelRed(w/2 + i,j,image.getPixelRed(w/2 - i,j))
            image.setPixelGreen(w/2 + i,j,image.getPixelGreen(w/2 - i,j))
            image.setPixelBlue(w/2 + i,j,image.getPixelBlue(w/2 - i,j))
            
    return image

def scroll(image):
    w = image.getWidth()
    h = image.getHeight()
    
    shift = input("By how many pixels would you like to scroll the image? ")
    
    shift %= w
    
    otherImage = copy(image)
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(i,j,otherImage.getPixelRed(wrap(i - shift,w),j))
            image.setPixelGreen(i,j,otherImage.getPixelGreen(wrap(i - shift,w),j))
            image.setPixelBlue(i,j,otherImage.getPixelBlue(wrap(i - shift,w),j))
            
    return image

def wrap(num,width):
    if(num < 0):
        num = width + num
        
    return num

def neg(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(i,j,dontYouWantAbs(image.getPixelRed(i,j)))
            image.setPixelGreen(i,j,dontYouWantAbs(image.getPixelGreen(i,j)))
            image.setPixelBlue(i,j,dontYouWantAbs(image.getPixelBlue(i,j)))
            
    return image
            
def dontYouWantAbs(c):
    c = abs(c - 255)
    return c

def grey(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w):
        for j in range(h):
            average = (image.getPixelRed(i,j) + image.getPixelGreen(i,j) + image.getPixelBlue(i,j))/3
            
            image.setPixelRed(i,j,average)
            image.setPixelGreen(i,j,average)
            image.setPixelBlue(i,j,average)
            
    return image

def cycle(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w):
        for j in range(h):
            r = image.getPixelRed(i,j)
            g = image.getPixelGreen(i,j)
            b = image.getPixelBlue(i,j)
            
            image.setPixelRed(i,j,b)
            image.setPixelGreen(i,j,r)
            image.setPixelBlue(i,j,g)
            
    return image

def zoom(image):
    w = image.getWidth()
    h = image.getHeight()
    
    otherImage = copy(image)
    
    for i in range(w/2):
        for j in range(h/2):
            r = otherImage.getPixelRed(i + w/4, j + h/4)
            g = otherImage.getPixelGreen(i + w/4, j + h/4)
            b = otherImage.getPixelBlue(i + w/4, j + h/4)
            
            image.setPixelRed(i * 2,j * 2,r)
            image.setPixelRed(i * 2 + 1,j * 2,r)
            image.setPixelRed(i * 2,j * 2 + 1,r)
            image.setPixelRed(i * 2 + 1,j * 2 + 1,r)
            
            image.setPixelGreen(i * 2,j * 2,g)
            image.setPixelGreen(i * 2 + 1,j * 2,g)
            image.setPixelGreen(i * 2,j * 2 + 1,g)
            image.setPixelGreen(i * 2 + 1,j * 2 + 1,g)
            
            image.setPixelBlue(i * 2,j * 2,b)
            image.setPixelBlue(i * 2 + 1,j * 2,b)
            image.setPixelBlue(i * 2,j * 2 + 1,b)
            image.setPixelBlue(i * 2 + 1,j * 2 + 1,b)
    
    return image

def post(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(i,j,round32(image.getPixelRed(i,j)))
            image.setPixelGreen(i,j,round32(image.getPixelGreen(i,j)))
            image.setPixelBlue(i,j,round32(image.getPixelBlue(i,j)))
    
    return image

def round32(num):
    if(num%32 < 16):
        num -= num%32
        
    else:
        num += 32 - num%32
    
    return num

def bound(num):
    if(num > 255):
        num = 255
    
    elif(num < 0):
        num = 0
    
    return num

def bright(image):
    w = image.getWidth()
    h = image.getHeight()
    
    change = input("By how much would you like to increase the brightness? ")
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(i,j,bound(image.getPixelRed(i,j) + change))
            image.setPixelGreen(i,j,bound(image.getPixelGreen(i,j) + change))
            image.setPixelBlue(i,j,bound(image.getPixelBlue(i,j) + change))
    
    return image

def contrast(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(i,j,bound(128 - 2 * (128 - image.getPixelRed(i,j))))
            image.setPixelGreen(i,j,bound(128 - 2 * (128 - image.getPixelGreen(i,j))))
            image.setPixelBlue(i,j,bound(128 - 2 * (128 - image.getPixelBlue(i,j))))
    
    return image

def blur(image):
    w = image.getWidth()
    h = image.getHeight()
    
    otherImage = copy(image)
    
    for i in range(1,w - 1):
        for j in range(1,h - 1):
            image.setPixelRed(i,j,(otherImage.getPixelRed(i,j) + otherImage.getPixelRed(i,j - 1) + otherImage.getPixelRed(i + 1,j -1) + otherImage.getPixelRed(i + 1,j) + otherImage.getPixelRed(i + 1,j + 1) + otherImage.getPixelRed(i,j + 1) + otherImage.getPixelRed(i - 1,j + 1) + otherImage.getPixelRed(i - 1,j) + otherImage.getPixelRed(i - 1,j - 1))/9)
            image.setPixelGreen(i,j,(otherImage.getPixelGreen(i,j) + otherImage.getPixelGreen(i,j - 1) + otherImage.getPixelGreen(i + 1,j -1) + otherImage.getPixelGreen(i + 1,j) + otherImage.getPixelGreen(i + 1,j + 1) + otherImage.getPixelGreen(i,j + 1) + otherImage.getPixelGreen(i - 1,j + 1) + otherImage.getPixelGreen(i - 1,j) + otherImage.getPixelGreen(i - 1,j - 1))/9)
            image.setPixelBlue(i,j,(otherImage.getPixelBlue(i,j) + otherImage.getPixelBlue(i,j - 1) + otherImage.getPixelBlue(i + 1,j -1) + otherImage.getPixelBlue(i + 1,j) + otherImage.getPixelBlue(i + 1,j + 1) + otherImage.getPixelBlue(i,j + 1) + otherImage.getPixelBlue(i - 1,j + 1) + otherImage.getPixelBlue(i - 1,j) + otherImage.getPixelBlue(i - 1,j - 1))/9)
    
    for i in range(1,w - 1):
        image.setPixelRed(i,0,(otherImage.getPixelRed(i,0) + otherImage.getPixelRed(i + 1,0) + otherImage.getPixelRed(i + 1,1) + otherImage.getPixelRed(i,1) + otherImage.getPixelRed(i - 1,1) + otherImage.getPixelRed(i - 1,0))/6)
        image.setPixelGreen(i,0,(otherImage.getPixelGreen(i,0) + otherImage.getPixelGreen(i + 1,0) + otherImage.getPixelGreen(i + 1,1) + otherImage.getPixelGreen(i,1) + otherImage.getPixelGreen(i - 1,1) + otherImage.getPixelGreen(i - 1,0))/6)
        image.setPixelBlue(i,0,(otherImage.getPixelBlue(i,0) + otherImage.getPixelBlue(i + 1,0) + otherImage.getPixelBlue(i + 1,1) + otherImage.getPixelBlue(i,1) + otherImage.getPixelBlue(i - 1,1) + otherImage.getPixelBlue(i - 1,0))/6)
    
    for i in range(1,w - 1):
        image.setPixelRed(i,h - 1,(otherImage.getPixelRed(i,h - 1) + otherImage.getPixelRed(i + 1,h - 1) + otherImage.getPixelRed(i + 1,h - 2) + otherImage.getPixelRed(i,h - 2) + otherImage.getPixelRed(i - 1,h - 2) + otherImage.getPixelRed(i - 1,h - 1))/6)
        image.setPixelGreen(i,h - 1,(otherImage.getPixelGreen(i,h - 1) + otherImage.getPixelGreen(i + 1,h - 1) + otherImage.getPixelGreen(i + 1,h - 2) + otherImage.getPixelGreen(i,h - 2) + otherImage.getPixelGreen(i - 1,h - 2) + otherImage.getPixelGreen(i - 1,h - 1))/6)
        image.setPixelBlue(i,h - 1,(otherImage.getPixelBlue(i,h - 1) + otherImage.getPixelBlue(i + 1,h - 1) + otherImage.getPixelBlue(i + 1,h - 2) + otherImage.getPixelBlue(i,h - 2) + otherImage.getPixelBlue(i - 1,h - 2) + otherImage.getPixelBlue(i - 1,h - 1))/6)
    
    for j in range(1,h - 1):
        image.setPixelRed(0,j,(otherImage.getPixelRed(0,j) + otherImage.getPixelRed(0,j - 1) + otherImage.getPixelRed(1,j + 1) + otherImage.getPixelRed(1,j) + otherImage.getPixelRed(1,j - 1) + otherImage.getPixelRed(0,j + 1))/6)
        image.setPixelGreen(0,j,(otherImage.getPixelGreen(0,j) + otherImage.getPixelGreen(0,j - 1) + otherImage.getPixelGreen(1,j + 1) + otherImage.getPixelGreen(1,j) + otherImage.getPixelGreen(1,j - 1) + otherImage.getPixelGreen(0,j + 1))/6)    
        image.setPixelBlue(0,j,(otherImage.getPixelBlue(0,j) + otherImage.getPixelBlue(0,j - 1) + otherImage.getPixelBlue(1,j + 1) + otherImage.getPixelBlue(1,j) + otherImage.getPixelBlue(1,j - 1) + otherImage.getPixelBlue(0,j + 1))/6)
        
    for j in range(1,h - 1):
        image.setPixelRed(w - 1,j,(otherImage.getPixelRed(w - 1,j) + otherImage.getPixelRed(w - 1,j - 1) + otherImage.getPixelRed(w - 2,j - 1) + otherImage.getPixelRed(w - 2,j) + otherImage.getPixelRed(w - 2,j + 1) + otherImage.getPixelRed(w - 1,j + 1))/6)
        image.setPixelGreen(w - 1,j,(otherImage.getPixelGreen(w - 1,j) + otherImage.getPixelGreen(w - 1,j - 1) + otherImage.getPixelGreen(w - 2,j - 1) + otherImage.getPixelGreen(w - 2,j) + otherImage.getPixelGreen(w - 2,j + 1) + otherImage.getPixelGreen(w - 1,j + 1))/6)    
        image.setPixelBlue(w - 1,j,(otherImage.getPixelBlue(w - 1,j) + otherImage.getPixelBlue(w - 1,j - 1) + otherImage.getPixelBlue(w - 2,j -1) + otherImage.getPixelBlue(w - 2,j) + otherImage.getPixelBlue(w - 2,j + 1) + otherImage.getPixelBlue(w - 1,j + 1))/6)
    
    image.setPixelRed(0,0,(otherImage.getPixelRed(0,0) + otherImage.getPixelRed(1,0) + otherImage.getPixelRed(0,1) + otherImage.getPixelRed(1,1))/4)
    image.setPixelGreen(0,0,(otherImage.getPixelGreen(0,0) + otherImage.getPixelGreen(1,0) + otherImage.getPixelGreen(0,1) + otherImage.getPixelGreen(1,1))/4)
    image.setPixelBlue(0,0,(otherImage.getPixelBlue(0,0) + otherImage.getPixelBlue(1,0) + otherImage.getPixelBlue(0,1) + otherImage.getPixelBlue(1,1))/4)
    
    image.setPixelRed(0,h - 1,(otherImage.getPixelRed(0,h - 1) + otherImage.getPixelRed(1,h - 1) + otherImage.getPixelRed(0,h - 2) + otherImage.getPixelRed(1,h - 2))/4)
    image.setPixelGreen(0,h - 1,(otherImage.getPixelGreen(0,h - 1) + otherImage.getPixelGreen(1,h - 1) + otherImage.getPixelGreen(0,h - 2) + otherImage.getPixelGreen(1,h - 2))/4)
    image.setPixelBlue(0,h - 1,(otherImage.getPixelBlue(0,h - 1) + otherImage.getPixelBlue(1,h - 1) + otherImage.getPixelBlue(0,h - 2) + otherImage.getPixelBlue(1,h - 2))/4)
    
    image.setPixelRed(w - 1,0,(otherImage.getPixelRed(w - 1,0) + otherImage.getPixelRed(w - 2,0) + otherImage.getPixelRed(w - 1,1) + otherImage.getPixelRed(w - 2,1))/4)
    image.setPixelGreen(w - 1,0,(otherImage.getPixelGreen(w - 1,0) + otherImage.getPixelGreen(w - 2,0) + otherImage.getPixelGreen(w - 1,1) + otherImage.getPixelGreen(w - 2,1))/4)
    image.setPixelBlue(w - 1,0,(otherImage.getPixelBlue(w - 1,0) + otherImage.getPixelBlue(w - 2,0) + otherImage.getPixelBlue(w - 1,1) + otherImage.getPixelBlue(w - 2,1))/4)
    
    image.setPixelRed(w - 1,h - 1,(otherImage.getPixelRed(w - 1,h - 1) + otherImage.getPixelRed(w - 2,h - 1) + otherImage.getPixelRed(w - 1,h - 2) + otherImage.getPixelRed(w - 2,h - 2))/4)
    image.setPixelGreen(w - 1,h - 1,(otherImage.getPixelGreen(w - 1,h - 1) + otherImage.getPixelGreen(w - 2,h - 1) + otherImage.getPixelGreen(w - 1,h - 2) + otherImage.getPixelGreen(w - 2,h - 2))/4)
    image.setPixelBlue(w - 1,h - 1,(otherImage.getPixelBlue(w - 1,h - 1) + otherImage.getPixelBlue(w - 2,h - 1) + otherImage.getPixelBlue(w - 1,h - 2) + otherImage.getPixelBlue(w - 2,h - 2))/4)
    
    return image

def rotate180(image):
    w = image.getWidth()
    h = image.getHeight()
    
    otherImage = copy(image)
    
    for i in range(w):
        for j in range(h):
            image.setPixelRed(i,j,otherImage.getPixelRed(w - 1 - i, h - 1 - j))
            image.setPixelGreen(i,j,otherImage.getPixelGreen(w - 1 - i, h - 1 - j))
            image.setPixelBlue(i,j,otherImage.getPixelBlue(w - 1 - i, h - 1 - j))
    
    return image

def Lemley(image):
    w = image.getWidth()
    h = image.getHeight()
    x = raw_input("Which value do you want to tint the image- red, green, or blue? ")
    
    try:
        if x == "red":
            for i in range(w):
                for j in range(h):
                    image.setPixelRed(i,j,bound(image.getPixelRed(i,j)+50))
        
        elif x == "green":
            for i in range(w):
                for j in range(h):
                    image.setPixelGreen(i,j,bound(image.getPixelGreen(i,j)+50))
                    
        elif x == "blue":
            for i in range(w):
                for j in range(h):
                    image.setPixelBlue(i,j,bound(image.getPixelBlue(i,j)+50))
    
    except:
        print"That is an unacceptable input." 
    
    return image

def Addison(image):
    w = image.getWidth()
    h = image.getHeight()
    
    for i in range(w):
        for j in range(h):
            r,g,b = AddisonFunction(image.getPixelRed(i,j),image.getPixelGreen(i,j),image.getPixelBlue(i,j))
            
            image.setPixelRed(i,j,bound(r))
            image.setPixelGreen(i,j,bound(g))
            image.setPixelBlue(i,j,bound(b))
    
    return image

def AddisonFunction(a,b,c):
    if a == b == c:
        return a,b,c
        
    elif a == b > c:
        return 255,255,0
    
    elif b == c > a:
        return 0,255,255
    
    elif a == c > b:
        return 255,0,255
    
    elif max(a,b,c) == a:
        return 255,0,0
    
    elif max(a,b,c) == b:
        return 0,255,0
    
    elif max(a,b,c) == c:
        return 0,0,255

def main():
    worked = False
    while worked == False:
        try:
            imageInput = raw_input("Please input a filename: ")
            image = picture2.Picture(imageInput)
            worked = True
            
        except:
            print "That filename was not valid."
        
    nextFunction = "0"
    
    print "\nHere are your choices for image manipulation!\n\nType '1' to flip the image horizontally\nType '2' to mirror the image\nType '3' to scroll the image\nType '4' to display the image with negative colors\nType '5' to display the image in greyscale\nType '6' to cycle the color channels\nType '7' to zoom in on the image\nType '8' to posterize the image\nType '9' to increase the image's brightness\nType '10' to increase the contrast of the image\nType '11' to blur the image\nType '12' to rotate the image 180 degrees\nType '13' to tint the image red, green, or blue\nType '14' to separate the image into its red, green, and blue components\nType 'done' if you are finished."
    
    image.display()
    
    while(nextFunction != "done"):
        nextFunction = raw_input("\nHow would you like to edit this image? ")
        
        if(nextFunction == "1"):
            image = flip(image)
        
        elif(nextFunction == "2"):
            image = mirror(image)
            
        elif(nextFunction == "3"):
            image = scroll(image)
            
        elif(nextFunction == "4"):
            image = neg(image)
            
        elif(nextFunction == "5"):
            image = grey(image)
            
        elif(nextFunction == "6"):
            image = cycle(image)
            
        elif(nextFunction == "7"):
            image = zoom(image)
            
        elif(nextFunction == "8"):
            image = post(image)
            
        elif(nextFunction == '9'):
            image = bright(image)
            
        elif(nextFunction == '10'):
            image = contrast(image)
            
        elif(nextFunction == '11'):
            image = blur(image)
            
        elif(nextFunction == '12'):
            image = rotate180(image)
            
        elif(nextFunction == '13'):
            image = Lemley(image)
            
        elif(nextFunction == '14'):
            image = Addison(image)
            
        
        image.display()
    
main()