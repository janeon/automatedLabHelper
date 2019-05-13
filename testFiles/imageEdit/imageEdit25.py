






import picture2

def colorCycle(pic, w, h):
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, B, R, G)
    return pic
            
def grayscale(pic, w, h):
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(i, j)
            avg = (R+G+B)/3
            pic.setPixelColor(i, j, avg, avg, avg)
    return pic
            
def negatives(pic, w, h):
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(i, j)
            pic.setPixelColor(i, j, 255-R, 255-G, 255-B)
    return pic
            
def scrolling(pic, w, h):
    n = input("Please enter the number of pixels you wish to scroll over to the right: ")
    pic2 = picture2.Picture(w, h)
    for j in range(h):
        for i in range(w):
            R, G, B = pic.getPixelColor((i-n)%w, j)
            pic2.setPixelColor(i, j, R, G, B)
    return pic2
            
def zoom(pic, w, h): 
    pic2 = picture2.Picture(w, h)
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(w/4 + i//2, h/4 + j//2)
            pic2.setPixelColor(i, j, R, G, B)
    return pic2
            

def posterize(pic, w, h):
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(i, j)
            R = R//32*32
            G = G//32*32
            B = B//32*32
            pic.setPixelColor(i, j, R, G, B)
    return pic
            
def changeBrightness(pic, w, h):
    n = input("Please enter a number from -256 to 256: ")
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(i, j)
            if (R+n) <= 255 and (R+n) >= 0:
                pic.setPixelRed(i, j, R+n)
            elif (R+n) < 0:
                pic.setPixelRed(i, j, 0)
            else:
                pic.setPixelRed(i, j, 255)
            if (G+n) <= 255 and (G+n) >= 0:
                pic.setPixelGreen(i, j, G+n)
            elif (G+n) < 0:
                pic.setPixelGreen(i, j, 0)
            else:
                pic.setPixelGreen(i, j, 255)
            if (B+n) <= 255 and (B+n) >= 0:
                pic.setPixelBlue(i, j, B+n)
            elif (B+n) < 0:
                pic.setPixelBlue(i, j, 0)
            else:
                pic.setPixelBlue(i, j, 255)
    return pic
                
def increaseContrast(pic, w, h):
    for i in range(w):
        for j in range(h):
            R, G, B = pic.getPixelColor(i, j)
            if R >= 64 and R <= 191.5:
                pic.setPixelRed(i, j, 2*R-128)
            elif R > 191.5:
                pic.setPixelRed(i, j, 255)
            else:
                pic.setPixelRed(i, j, 0)
            if G >= 64 and G <= 191.5:
                pic.setPixelGreen(i, j, 2*G-128)
            elif G > 191.5:
                pic.setPixelGreen(i, j, 255)
            else:
                pic.setPixelGreen(i, j, 0)
            if B >= 64 and B <= 191.5:
                pic.setPixelBlue(i, j, 2*B-128)
            elif B > 191.5:
                pic.setPixelBlue(i, j, 255)
            else:
                pic.setPixelBlue(i, j, 0)
    return pic

def flip(pic, w, h):
    pic2 = picture2.Picture(w, h)
    for j in range(h):
        for i in range(w):
            R, G, B = pic.getPixelColor(w-1-i, j)
            pic2.setPixelColor(i, j, R, G, B)
    return pic2

def rotate180degrees(pic, w, h):
    pic = flip(pic, w, h)
    pic2 = picture2.Picture(w, h)
    for i in range(w):
        for j in range(h):
            R, G, B, = pic.getPixelColor(i, h-1-j)
            pic2.setPixelColor(i, j, R, G, B)
    return pic2
    
def mirror(pic, w, h):
    pic2 = picture2.Picture(w, h)
    for j in range(h):
        for i in range(0, w//2):
            R, G, B = pic.getPixelColor(i, j)
            pic2.setPixelColor(i, j, R, G, B)
        for i in range(w//2, w-1):
            R, G, B = pic.getPixelColor((w-1)//2-(i-((w-1)//2)), j)
            pic2.setPixelColor(i, j, R, G, B)
    return pic2

def blur(pic, w, h):
    pic2 = picture2.Picture(w, h)
    for i in range(w):
        for j in range(h):
            if i == 0 and j == 0:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i+1, j)
                R2, G2, B2 = pic.getPixelColor(i, j+1)
                R3, G3, B3 = pic.getPixelColor(i+1, j+1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3)/4, (G+G1+G2+G3)/4, (B+B1+B2+B3)/4)
            elif i == 0 and j == h-1:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i+1, j)
                R2, G2, B2 = pic.getPixelColor(i, j-1)
                R3, G3, B3 = pic.getPixelColor(i+1, j-1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3)/4, (G+G1+G2+G3)/4, (B+B1+B2+B3)/4)
            elif i == w-1 and j == 0:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i-1, j)
                R2, G2, B2 = pic.getPixelColor(i, j+1)
                R3, G3, B3 = pic.getPixelColor(i-1, j+1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3)/4, (G+G1+G2+G3)/4, (B+B1+B2+B3)/4)
            elif i == w-1 and j == h-1:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i-1, j)
                R2, G2, B2 = pic.getPixelColor(i, j-1)
                R3, G3, B3 = pic.getPixelColor(i-1, j-1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3)/4, (G+G1+G2+G3)/4, (B+B1+B2+B3)/4)
            elif i == 0:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i, j+1)
                R2, G2, B2 = pic.getPixelColor(i+1, j+1)
                R3, G3, B3 = pic.getPixelColor(i+1, j)
                R4, G4, B4 = pic.getPixelColor(i+1, j-1)
                R5, G5, B5 = pic.getPixelColor(i, j-1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3+R4+R5)/6, (G+G1+G2+G3+G4+G5)/6, (B+B1+B2+B3+B4+B5)/6)
            elif i == w-1:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i, j+1)
                R2, G2, B2 = pic.getPixelColor(i-1, j+1)
                R3, G3, B3 = pic.getPixelColor(i-1, j)
                R4, G4, B4 = pic.getPixelColor(i-1, j-1)
                R5, G5, B5 = pic.getPixelColor(i, j-1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3+R4+R5)/6, (G+G1+G2+G3+G4+G5)/6, (B+B1+B2+B3+B4+B5)/6)
            elif j == 0:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i-1, j)
                R2, G2, B2 = pic.getPixelColor(i-1, j+1)
                R3, G3, B3 = pic.getPixelColor(i, j+1)
                R4, G4, B4 = pic.getPixelColor(i+1, j+1)
                R5, G5, B5 = pic.getPixelColor(i+1, j)
                pic2.setPixelColor(i, j, (R+R1+R2+R3+R4+R5)/6, (G+G1+G2+G3+G4+G5)/6, (B+B1+B2+B3+B4+B5)/6)
            elif j == h-1:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i-1,j)
                R2, G2, B2 = pic.getPixelColor(i-1, j-1)
                R3, G3, B3 = pic.getPixelColor(i, j-1)
                R4, G4, B4 = pic.getPixelColor(i+1, j-1)
                R5, G5, B5 = pic.getPixelColor(i+1, j)
                pic2.setPixelColor(i, j, (R+R1+R2+R3+R4+R5)/6, (G+G1+G2+G3+G4+G5)/6, (B+B1+B2+B3+B4+B5)/6)
            else:
                R, G, B = pic.getPixelColor(i, j)
                R1, G1, B1 = pic.getPixelColor(i-1, j+1)
                R2, G2, B2 = pic.getPixelColor(i, j+1)
                R3, G3, B3 = pic.getPixelColor(i+1, j+1)
                R4, G4, B4 = pic.getPixelColor(i-1, j)
                R5, G5, B5 = pic.getPixelColor(i+1, j)
                R6, G6, B6 = pic.getPixelColor(i-1, j-1)
                R7, G7, B7 = pic.getPixelColor(i, j-1)
                R8, G8, B8 = pic.getPixelColor(i+1, j-1)
                pic2.setPixelColor(i, j, (R+R1+R2+R3+R4+R5+R6+R7+R8)/9, (G+G1+G2+G3+G4+G5+G6+G7+G8)/9, (B+B1+B2+B3+B4+B5+B6+B7+B8)/9)
    return pic2

def colorFilter(pic, w, h):
    accent = raw_input("Would you like to make the picture more Red, Green, or Blue? ")
    if accent == "Red":
        for i in range(w):
            for j in range(h):
                R, G, B = pic.getPixelColor(i, j)
                pic.setPixelColor(i, j, R, 0, 0)
    elif accent == "Green":
        for i in range(w):
            for j in range(h):
                R, G, B = pic.getPixelColor(i, j)
                pic.setPixelColor(i, j, 0, G, 0)
    elif accent == "Blue":
        for i in range(w):
            for j in range(h):
                R, G, B = pic.getPixelColor(i, j)
                pic.setPixelColor(i, j, 0, 0, B)
    else:
        print "Make sure to capitalize the color properly."
        print ""
        colorFilter(pic, w, h)
    return pic

def tiled(pic, w, h):
    pic2 = picture2.Picture(w, h)
    for i in range(0, w/3):
        for j in range(0, h/3):
            R, G, B = pic.getPixelColor(3*i, 3*j)
            pic2.setPixelColor(i, j, R, G, B)
            pic2.setPixelColor(i+(w/3), j, R, G, B)
            pic2.setPixelColor(i+(2*w/3), j, R, G, B)
            pic2.setPixelColor(i, j+(h/3), R, G, B)
            pic2.setPixelColor(i+(w/3), j+(h/3), R, G, B)
            pic2.setPixelColor(i+(2*w/3), j+(h/3), R, G, B)
            pic2.setPixelColor(i, j+(2*h/3), R, G, B)
            pic2.setPixelColor(i+(w/3), j+(2*h/3), R, G, B)
            pic2.setPixelColor(i+(2*w/3), j+(2*h/3), R, G, B)
    return pic2     

def main():
    print "Hi! Welcome to my Image Edit!"
    print ""
    try:
        pic = picture2.Picture(raw_input("Please enter a file name (ex: crayons.bmp): "))
    except:
        print "The computer can't seem to find that file."
        print "Make sure you saved the file under the right directory."
        print "Try again."
        main()
    print "Here's your picture! Press 'Enter' once you're ready to move to the next step."
    pic.display()
    raw_input()
    print ""
    print "There are a number of functions for you to try"
    print "on your picture in any combination and order you desire!"
    print ""
    response = "Y"
    while response == "Y":
        print "Here is a list of possible functions:"
        print "Flip Horizontally, Mirror Horizontally, Scroll Horizontally,"
        print "Make Negative, Make Grayscale, Cycle Color Channels, Zoom,"
        print "Posterize, Change Brightness, Increase Contrast, Blur,"
        print "Rotate 180 Degrees, Color Filter, and Tiled. So have some fun!"
        print ""
        w = pic.getWidth()
        h = pic.getHeight()
        function = raw_input("Enter a function (as formatted above): ")
        if function == "Flip Horizontally":
            pic = flip(pic, w, h)
        elif function == "Mirror Horizontally":
            pic = mirror(pic, w, h)
        elif function == "Scroll Horizontally":
            pic = scrolling(pic, w, h)
        elif function == "Make Negative":
            pic = negatives(pic, w, h)
        elif function == "Make Grayscale":
            pic = grayscale(pic, w, h)
        elif function == "Cycle Color Channels":
            pic = colorCycle(pic, w, h)
        elif function == "Zoom":
            pic = zoom(pic, w, h)
        elif function == "Posterize":
            pic = posterize(pic, w, h)
        elif function == "Change Brightness":
            pic = changeBrightness(pic, w, h)
        elif function == "Increase Contrast":
            pic = increaseContrast(pic, w, h)
        elif function == "Blur":
            pic = blur(pic, w, h)
        elif function == "Rotate 180 Degrees":
            pic = rotate180degrees(pic, w, h)
        elif function == "Color Filter":
            pic = colorFilter(pic, w, h)
        elif function == "Tiled":
            pic = tiled(pic, w, h)
        else:
            print "Make sure you formatted the function with"
            print "correct capitalization and spacing."
            main()
        pic.display()
        response = raw_input("Would you like to continue editing your picture (Y or N)? ")
        print ""

main()