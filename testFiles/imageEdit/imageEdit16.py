






import picture2


def negative(crayons, W, H):
    for x in range(0,W-1):
        for y in range(0,H-1):
            RedVal = crayons.getPixelRed(x,y)
            crayons.setPixelRed(x,y, 255-RedVal)
            GreenVal = crayons.getPixelGreen(x,y)
            crayons.setPixelGreen(x,y, 255-GreenVal)
            BlueVal = crayons.getPixelBlue(x,y)
            crayons.setPixelBlue(x,y, 255-BlueVal)



def grey(crayons, W, H):
    for x in range(0, W-1):
        for y in range(0,H-1):
            OrigRed = crayons.getPixelRed(x,y)
            OrigGreen = crayons.getPixelGreen(x,y)
            OrigBlue = crayons.getPixelBlue(x,y)
            Red = (OrigRed + OrigGreen + OrigBlue)/3
            crayons.setPixelRed(x,y, Red)
            Green = (OrigRed + OrigGreen + OrigBlue)/3
            crayons.setPixelGreen(x,y, Green)
            Blue = (OrigRed + OrigGreen + OrigBlue)/3
            crayons.setPixelBlue(x,y, Blue)



def mirror(crayons, W, H):
    for x in range(0, W-1):
        for y in range(0, H-1):
            RedVal = crayons.getPixelRed(x,y)
            crayons.setPixelRed((W-1-x),y, RedVal)
            GreenVal = crayons.getPixelGreen(x,y)
            crayons.setPixelGreen((W-1-x),y, GreenVal)
            BlueVal = crayons.getPixelBlue(x,y)
            crayons.setPixelBlue((W-1-x),y, BlueVal)



def PictureCopy(crayons, W, H):
    CopyOfPic = picture2.Picture(W,H)
    for x in range(0, W-1):
        for y in range(0, H-1):
            Red = crayons.getPixelRed(x,y)
            CopyOfPic.setPixelRed(x,y,Red)
            Green = crayons.getPixelGreen(x,y)
            CopyOfPic.setPixelGreen(x,y,Green)
            Blue = crayons.getPixelBlue(x,y)
            CopyOfPic.setPixelBlue(x,y,Blue)
    return CopyOfPic 


def Flip(crayons, W, H):
    CopyOfPic = PictureCopy(crayons, W, H)
    for x in range(0, W-1):
        for y in range(0, H-1):
            OrigRed = CopyOfPic.getPixelRed(x,y)
            OrigGreen = CopyOfPic.getPixelGreen(x,y)
            OrigBlue = CopyOfPic.getPixelBlue(x,y)
            crayons.setPixelRed(W-1-x,y, OrigRed)
            crayons.setPixelGreen(W-1-x,y, OrigGreen)
            crayons.setPixelBlue(W-1-x,y, OrigBlue)

            


def Posterize(crayons, W, H):
    for x in range(0, W-1):
        for y in range(0, H-1):
            RedVal = crayons.getPixelRed(x,y)
            crayons.setPixelRed(x,y, (RedVal//32)*32)
            GreenVal = crayons.getPixelGreen(x,y)
            crayons.setPixelGreen(x,y, (GreenVal//32)*32)
            BlueVal = crayons.getPixelBlue(x,y)
            crayons.setPixelBlue(x,y, (BlueVal//32)*32)



def Cycle(crayons, W, H):
    for x in range(0, W-1):
        for y in range(0,H-1):
            OrigRed = crayons.getPixelRed(x,y)
            OrigGreen = crayons.getPixelGreen(x,y)
            OrigBlue = crayons.getPixelBlue(x,y)
            crayons.setPixelRed(x,y, OrigBlue)
            crayons.setPixelGreen(x,y, OrigRed)
            crayons.setPixelBlue(x,y, OrigGreen)



def Brightness(crayons,W,H):
    brightness = eval(raw_input("Please input a value to change the brightness: "))
    for x in range(0, W-1):
        for y in range(0,H-1):
            OrigRed = crayons.getPixelRed(x,y)
            OrigGreen = crayons.getPixelGreen(x,y)
            OrigBlue = crayons.getPixelBlue(x,y)
            if OrigRed + brightness > 255:
                crayons.setPixelRed(x, y, 255)
            elif OrigRed + brightness < 0:
                crayons.setPixelRed(x, y, 0)
            else:
                crayons.setPixelRed(x,y, OrigRed + brightness)
            if OrigGreen + brightness > 255:
                crayons.setPixelGreen(x,y,255)
            elif OrigGreen + brightness < 0:
                crayons.setPixelGreen(x, y, 0)
            else:
                crayons.setPixelGreen(x,y, OrigGreen + brightness)
            if OrigBlue + brightness > 255:
                crayons.setPixelBlue(x, y, 255)
            elif OrigBlue + brightness < 0:
                crayons.setPixelBlue(x, y, 0)
            else:
                crayons.setPixelBlue(x,y, OrigBlue + brightness)



def Contrast(crayons,W,H):
    for x in range(0, W-1):
        for y in range(0,H-1):
            OrigRed = crayons.getPixelRed(x,y)
            OrigGreen = crayons.getPixelGreen(x,y)
            OrigBlue = crayons.getPixelBlue(x,y)
            NewRed = 2*(OrigRed-128)
            NewGreen = 2*(OrigGreen-128)
            NewBlue = 2*(OrigBlue-128)
            if NewRed + 128 > 255:
                crayons.setPixelRed(x, y, 255)
            elif NewRed + 128 < 0:
                crayons.setPixelRed(x, y, 0)
            else:
                crayons.setPixelRed(x,y, 128 + NewRed)
            if NewGreen + 128 > 255:
                crayons.setPixelGreen(x,y,255)
            elif NewGreen + 128 < 0:
                crayons.setPixelGreen(x, y, 0)
            else:
                crayons.setPixelGreen(x,y, 128 + NewGreen)
            if NewBlue + 128 > 255:
                crayons.setPixelBlue(x, y, 255)
            elif NewBlue + 128 < 0:
                crayons.setPixelBlue(x, y, 0)
            else:
                crayons.setPixelBlue(x,y, 128 + NewBlue)


def Zoom(crayons, W, H):
    CopyOfPic = PictureCopy(crayons, W, H)
    for x in range(W/4, (3*W/4)-1):
        for y in range(H/4 + 1, (3*H/4)-1):
            OrigRed = CopyOfPic.getPixelRed(x,y)
            OrigGreen = CopyOfPic.getPixelGreen(x,y)
            OrigBlue = CopyOfPic.getPixelBlue(x,y)
            NewX = 2*(x - W/2) + W/2
            NewY = 2*(y - H/2) + H/2
            crayons.setPixelRed(NewX, NewY, OrigRed)
            crayons.setPixelRed(NewX+1, NewY, OrigRed)
            crayons.setPixelRed(NewX, NewY+1, OrigRed)
            crayons.setPixelRed(NewX+1, NewY+1, OrigRed)
            crayons.setPixelGreen(NewX, NewY, OrigGreen)
            crayons.setPixelGreen(NewX+1, NewY, OrigGreen)
            crayons.setPixelGreen(NewX, NewY+1, OrigGreen)
            crayons.setPixelGreen(NewX+1, NewY+1, OrigGreen)       
            crayons.setPixelBlue(NewX, NewY, OrigBlue)
            crayons.setPixelBlue(NewX+1, NewY, OrigBlue)
            crayons.setPixelBlue(NewX, NewY+1, OrigBlue)
            crayons.setPixelBlue(NewX+1, NewY+1, OrigBlue)          



def Blur(crayons, W, H):
    CopyOfPic = PictureCopy(crayons, W, H)
    for x in range(0, W-1):
        for y in range(0, H-1):
            Sum_Red = 0
            Sum_Green = 0
            Sum_Blue = 0
            counter = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if x + i >= 0 and x + i <= W-1 and y + j >=0 and y + j <= H-1:
                        Sum_Red = CopyOfPic.getPixelRed(x+i, y+j) + Sum_Red
                        Sum_Green = CopyOfPic.getPixelGreen(x+i, y+j) + Sum_Green
                        Sum_Blue = CopyOfPic.getPixelBlue(x+i, y+j) + Sum_Blue
                        counter = counter + 1
            crayons.setPixelRed(x, y, Sum_Red/counter)
            crayons.setPixelGreen(x, y, Sum_Green/counter)
            crayons.setPixelBlue(x, y, Sum_Blue/counter)



def Scroll(crayons, W, H):
    CopyOfPic = PictureCopy(crayons, W, H)
    d = eval(raw_input("Please give me a positive number: "))
    for x in range(0, W-1):
        for y in range(0, H-1):
            OrigRed = CopyOfPic.getPixelRed(x,y)
            OrigGreen = CopyOfPic.getPixelGreen(x,y)
            OrigBlue = CopyOfPic.getPixelBlue(x,y)
            crayons.setPixelRed((x+d)%W, y, OrigRed)
            crayons.setPixelGreen((x+d)%W, y, OrigGreen)
            crayons.setPixelBlue((x+d)%W, y, OrigBlue)



def Rotate(crayons, W, H):
    CopyOfPic = PictureCopy(crayons, W, H)
    for x in range(0, W-1):
        for y in range(0, H-1):
            OrigRed = CopyOfPic.getPixelRed(x,y)
            OrigGreen = CopyOfPic.getPixelGreen(x,y)
            OrigBlue = CopyOfPic.getPixelBlue(x,y)
            crayons.setPixelRed(x,H-1-y, OrigRed)
            crayons.setPixelGreen(x, H-1-y, OrigGreen)
            crayons.setPixelBlue(x, H-1-y, OrigBlue)
    Flip(crayons, W, H)
    

def Blue(crayons, W, H):
    for x in range(0,W-1):
        for y in range(0,H-1):
            OrigRed = crayons.getPixelRed(x,y)
            OrigGreen = crayons.getPixelGreen(x,y)
            OrigBlue = crayons.getPixelBlue(x,y)
            Red = (OrigRed + OrigGreen + OrigBlue)/3
            crayons.setPixelRed(x,y, Red)
            Green = (OrigRed + OrigGreen + OrigBlue)/3
            crayons.setPixelGreen(x,y, Green)
            crayons.setPixelBlue(x,y, OrigBlue)
            

def Zombie(crayons, W, H):
    for x in range(0, W-1):
        for y in range(0, H-1):
            OrigRed = crayons.getPixelRed(x,y)
            OrigGreen = crayons.getPixelGreen(x,y)
            OrigBlue = crayons.getPixelBlue(x,y)
            Red = (OrigRed + OrigGreen + OrigBlue)/3
            crayons.setPixelRed(x, y, Red)
            crayons.setPixelGreen(x, y, OrigGreen)
            crayons.setPixelBlue(x, y, OrigBlue)       
            
def main():
    print "Welcome to my Image Editor."
    print "If you want to make the image a negative, type: 1"
    print "If you want to make the image greyscale, type: 2"
    print "If you want to make the image mirrored, type: 3"
    print "If you want to make the image cycle color channels, type: 4"
    print "If you want to posterize the image, type: 5"
    print "If you want to flip the image, type: 6"
    print "If you want to change the brightness of the image, type: 7"
    print "If you want to change the contrast of the image, type: 8"
    print "If you want to zoom in on the image, type: 9"
    print "If you want to blur the image, type: 10"
    print "If you want to scroll the image to the right, type: 11"
    print "If you want to rotate the image, type: 12"
    print "If you want to get rid of the green and red in the image, type: 13"
    print "If you want to dull the image, type: 14"
    print "If you want to exit the program, type: 15"
    choice = eval(raw_input("Now choose your option (1-15): "))
    crayons = picture2.Picture("cole.bmp")
    W = crayons.getWidth()
    H = crayons.getHeight()
    while choice != 15:
        if choice == 1:
            negative(crayons, W, H)
        if choice == 2:
            grey(crayons, W, H)
        if choice == 3:
            mirror(crayons, W, H)
        if choice == 4:
            Cycle(crayons, W, H)
        if choice == 5:
            Posterize(crayons, W, H)
        if choice == 6:
            Flip(crayons, W, H)
        if choice == 7:
            Brightness(crayons, W, H)
        if choice == 8:
            Contrast(crayons, W, H)
        if choice == 9:
            Zoom(crayons, W, H)
        if choice == 10:
            Blur(crayons, W, H)
        if choice == 11:
            Scroll(crayons, W, H)
        if choice == 12:
            Rotate(crayons, W, H)
        if choice == 13:
            Blue(crayons, W, H)
        if choice == 14:
            Zombie(crayons, W, H)
        crayons.display()
        choice = eval(raw_input("Now choose your option (1-15): "))
        

main()