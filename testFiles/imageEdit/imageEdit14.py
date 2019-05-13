





import picture2
import math

def FlipHorizontal( pic, width, height ):           
    picCopy = CopyPic( pic, width, height )
    for x in range( width ):
        for y in range( height ):
            red, blue, green = picCopy.getPixelColor( (width-1-x), y )
            pic.setPixelColor( x, y, red, blue, green )
    
def MirrorHorizontal( pic, width, height ):         
    for x in range( (width/2) ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            pic.setPixelColor( (width-1-x), y, red, blue, green )

def ScrollHorizontal( pic, width, height, shift ):  
    pic2 = CopyPic( pic, width, height )
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic2.getPixelColor( x, y )
            x = (x + shift)%(width-1)
            pic.setPixelColor( x, y, red, blue, green )

def MakeNegative( pic, width, height ):             
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            red = 255 - red
            blue = 255 - blue
            green = 255 - green
            pic.setPixelColor( x, y, red, blue, green )

def MakeGrayscale( pic, width, height ):            
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            ave = (red + blue + green)//3
            pic.setPixelColor( x, y, ave, ave, ave )

def CycleColorChannels( pic, width, height ):       
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            red, blue, green = blue, green, red
            pic.setPixelColor( x, y, red, blue, green )

def Zoom( pic, width, height ):                     
    pic2 = CopyPic( pic, width ,height )
    for x in range( 0, width-1, 2 ):
        for y in range( 0, height-1, 2 ):
            x2 = (width/4)+(x/2)
            y2 = (height/4)+(y/2)
            red, blue, green = pic2.getPixelColor( x2, y2 )
            pic.setPixelColor( x, y, red, blue, green )
            pic.setPixelColor( x+1, y, red, blue, green )
            pic.setPixelColor( x, y+1, red, blue, green )
            pic.setPixelColor( x+1, y+1, red, blue, green )

def Posterize( pic, width, height ):                
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            red = (red//32)*32
            blue = (blue//32)*32
            green = (green//32)*32
            pic.setPixelColor( x, y, red, blue, green )

def ChangeBrightness( pic, width, height, shift ):  
    for x in range( width ):
        for y in range( height ):
            red, green, blue = pic.getPixelColor( x, y )
            red = red + shift
            blue = blue + shift
            green = green + shift
            if red > 255:
                red = 255
            elif red < 0:
                red = 0
            if blue > 255:
                blue = 255
            elif blue < 0:
                blue = 0
            if green > 255:
                green = 255
            elif green < 0:
                green = 0
            pic.setPixelColor( x, y, red, blue, green )           

def IncreaseContrast( pic, width, height ):         
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            if red > 125:
                red = 125+((red-125)*2)
            elif red < 125:
                red = 125-((125-red)*2)
            if red > 255:
                red = 255
            elif red < 0:
                red = 0
            if blue > 125:
                blue = 125+((blue-125)*2)
            elif blue < 125:
                blue = 125-((125-blue)*2)
            if blue > 255:
                blue = 255
            elif blue < 0:
                ble = 0
            if green > 125:
                green = 125+((green-125)*2)
            elif green < 125:
                green = 125-((125-green)*2)
            if green > 255:
                green = 255
            elif green < 0:
                green = 0
            pic.setPixelColor( x, y, red, blue, green )

def Blur( pic, width, height ):                     
    pic2 = CopyPic( pic, width, height )
    for x in range( 1, width-2 ):
        for y in range( 1, height-2 ):  
            r1, b1, g1 = pic2.getPixelColor( x-1, y-1 )
            r2, b2, g2 = pic2.getPixelColor( x, y-1 )
            r3, b3, g3 = pic2.getPixelColor( x+1, y-1 )
            r4, b4, g4 = pic2.getPixelColor( x-1, y )
            r5, b5, g5 = pic2.getPixelColor( x, y )
            r6, b6, g6 = pic2.getPixelColor( x+1, y )
            r7, b7, g7 = pic2.getPixelColor( x-1, y+1 )
            r8, b8, g8 = pic2.getPixelColor( x, y+1 )
            r9, b9, g9 = pic2.getPixelColor( x+1, y+1 )
            red = (r1+r2+r3+r4+r5+r6+r7+r8+r9)//9
            blue = (b1+b2+b3+b4+b5+b6+b7+b8+b9)//9
            green = (g1+g2+g3+g4+g5+g6+g7+g8+g9)//9
            pic.setPixelColor( x, y, red, blue, green )

def Rotate180( pic, width, height ):                
    picCopy = CopyPic( pic, width, height )
    for x in range( width ):
        for y in range( height ):
            red, blue, green = picCopy.getPixelColor( (width-1-x), (height-1-y) )
            pic.setPixelColor( x, y, red, blue, green )

def CopyPic( pic, width, height ):                  
    picCopy = picture2.Picture( width, height )
    for x in range( width ):
        for y in range( height ):
            red, blue, green = pic.getPixelColor( x, y )
            picCopy.setPixelColor( x, y, red, blue, green )
    return picCopy

def LoadPic( name ):                                
    pic = picture2.Picture( name )
    return pic

def Main():
    print "Welcome, ladies and germs, to the last image editor you shall ever use!"
    
    done = False
    while not done:
        try:
            name = raw_input( "Please enter the filename of the picture you would like to import: ")
            pic = LoadPic( name )
            done = True
        except:
            print "Sorry, file not found."
    
    width = pic.getWidth()
    height = pic.getHeight()
    

    print "The following operation are available for you to use:"
    print "1: Flip the image on the horizontal axis"
    print "2: Mirror the image on the horizontal axis"
    print "3: Scroll along the horizontal axis"
    print "4: Make a negative of the image"
    print "5: Convert the image to grayscale"
    print "6: Cycle the color channels of the image"
    print "7: Zoom 2x on the center of the image"
    print "8: 'Posterize' the image"
    print "9: Change the brightness of the image"
    print "10: Increase the contrast of the image"
    print "11: Blur the image"
    print "12: Rotate the image 180 degrees"
    print "13: Reset image"
    print "14: Open new image"
    print "15: Finish"
    
    done = False
    while not done:
        operation = input( "Please enter the number corresponding to the operation you would like to perform: " )
        if operation == 1:
            FlipHorizontal( pic, width, height )
        elif operation == 2:
            MirrorHorizontal( pic, width, height )
        elif operation == 3:
            shift = input( "Enter the number of pixels you would like it shifted: " )
            ScrollHorizontal( pic, width, height, shift )
        elif operation == 4:
            MakeNegative( pic, width, height )
        elif operation == 5:
            MakeGrayscale( pic, width, height)
        elif operation == 6:
            CycleColorChannels( pic, width, height )
        elif operation == 7:
            Zoom( pic, width, height )
        elif operation == 8:
            Posterize( pic, width, height )
        elif operation == 9:
            shift = input( "Enter the integer amount you would like it changed by: " )
            ChangeBrightness( pic, width, height, shift )
        elif operation == 10:
            IncreaseContrast( pic, width, height )
        elif operation == 11:
            Blur( pic, width, height )
        elif operation == 12:
            Rotate180( pic, width, height )
        elif operation ==13:
            pic = LoadPic( name )
        elif operation == 14:
            found = False
            while not found:
                try:
                    name = raw_input( "Please enter the filename of the picture you would like to import: " )
                    pic = LoadPic( name )
                    found = True
                except:
                    print "Sorry, file not found."
        elif operation == 15:
            done = True
            print "Thanks! Have a good day!"

        pic.display()
        
    input()

    
    
Main()