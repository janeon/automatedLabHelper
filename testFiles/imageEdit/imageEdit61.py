






import picture2

def flip(x):
    height = x.getHeight()
    width = x.getWidth()
    picFlip = picture2.Picture(width,height)
    for flipHeight in range(0,height):
        for flipWidth in range(0,width):
            r,g,b = x.getPixelColor(flipWidth,flipHeight)
            picFlip.setPixelColor(width-1-flipWidth,flipHeight,r,g,b)
    return picFlip
def mirror(x):
    height = x.getHeight()
    width = x.getWidth()
    picMirror = picture2.Picture(width,height)
    for flipHeight in range(0,height):
        for flipWidth in range(width//2,0,-1):
            r,g,b = x.getPixelColor(flipWidth,flipHeight)
            picMirror.setPixelColor(width-1-flipWidth,flipHeight,r,g,b)
    for flipHeight in range(0,height):
        for flipWidth in range(0,width//2):
            r,g,b = x.getPixelColor(flipWidth,flipHeight)
            picMirror.setPixelColor(flipWidth,flipHeight,r,g,b)
    return picMirror
def scroll(x):
    height = x.getHeight()
    width = x.getWidth()
    picScroll = picture2.Picture(width,height)
    scrollValue = eval(raw_input("Input the pixel value you want the image scrolled: "))
    for scrollHeight in range(0,height-1):
        for scrollWidth in range(scrollValue,width-1):
            r,g,b = x.getPixelColor(scrollWidth-scrollValue,scrollHeight)
            picScroll.setPixelColor(scrollWidth,scrollHeight,r,g,b)
    for scrollHeight in range(0,height-1):
        for scrollWidth in range(0,scrollValue-1):
            r,g,b = x.getPixelColor(width-1+scrollWidth-scrollValue,scrollHeight)
            picScroll.setPixelColor(scrollWidth,scrollHeight,r,g,b)
    return picScroll
def neg(x):
    height = x.getHeight()
    width = x.getWidth()
    picNeg = picture2.Picture(width,height)
    for negHeight in range(0,height):
        for negWidth in range(0,width):
            r,g,b = x.getPixelColor(negWidth,negHeight)
            picNeg.setPixelColor(negWidth,negHeight,255-r,255-g,255-b)
    return picNeg
def gray(x):
    height = x.getHeight()
    width = x.getWidth()
    picGray = picture2.Picture(width,height)
    for grayHeight in range(0,height):
        for grayWidth in range(0,width):
            r,g,b = x.getPixelColor(grayWidth,grayHeight)
            picGray.setPixelColor(grayWidth,grayHeight,(r+g+b)//3,(r+g+b)//3,(r+g+b)//3)
    return picGray
def cycle(x):
    height = x.getHeight()
    width = x.getWidth()
    picCycle = picture2.Picture(width,height)
    for cycleHeight in range(0,height):
        for cycleWidth in range(0,width):
            r,g,b = x.getPixelColor(cycleWidth,cycleHeight)
            picCycle.setPixelColor(cycleWidth,cycleHeight,g,b,r)
    return picCycle
def zoom(x):
    height = x.getHeight()
    width = x.getWidth()
    picZoom = picture2.Picture(width,height)
    for zoomHeight in range(0,height,2):
        for zoomWidth in range(0,width,2):
            r,g,b = x.getPixelColor(zoomWidth/2+(width-1)//4,zoomHeight/2+(height-1)//4)
            picZoom.setPixelColor(zoomWidth,zoomHeight,r,g,b)
            picZoom.setPixelColor(zoomWidth+1,zoomHeight,r,g,b)
            picZoom.setPixelColor(zoomWidth,zoomHeight+1,r,g,b)
            picZoom.setPixelColor(zoomWidth+1,zoomHeight+1,r,g,b)
    return picZoom
def poster(x):
    height = x.getHeight()
    width = x.getWidth()
    picPoster = picture2.Picture(width,height)
    for posterHeight in range(0,height):
        for posterWidth in range(0,width):
            r,g,b = x.getPixelColor(posterWidth,posterHeight)
            if r%32>=16:
                r=(r//32)*32+32
            else:
                r=(r//32)*32
            if g%32>=16:
                g=(g//32)*32+32
            else:
                g=(g//32)*32
            if b%32>=16:
                b=(b//32)*32+32
            else:
                b=(b//32)*32
            picPoster.setPixelColor(posterWidth,posterHeight,r,g,b)
    return picPoster
def bright(x):
    height = x.getHeight()
    width = x.getWidth()
    picBright = picture2.Picture(width,height)
    brightValue = eval(raw_input("Input the rgb value you want the brightness increased or decreased: "))    
    for brightHeight in range(0,height):
        for brightWidth in range(0,width):
            r,g,b = x.getPixelColor(brightWidth,brightHeight)
            if 0<=r+brightValue<=255:
                if r+brightValue>=0:
                    r=r+brightValue
            elif r+brightValue>255:
                r=255
            elif r+brightValue<0:
                r=0
            if 0<=g+brightValue<=255:
                if g+brightValue>=0:
                    g=g+brightValue
            elif g+brightValue>255:
                g=255
            elif g+brightValue<0:
                g=0
            if 0<=b+brightValue<=255:
                if b+brightValue>=0:
                    b=b+brightValue
            elif b+brightValue>255:
                b=255
            elif b+brightValue<0:
                b=0
            picBright.setPixelColor(brightWidth,brightHeight,r,g,b)
    return picBright
def rotate(x):
    height = x.getHeight()
    width = x.getWidth()
    picRotate = picture2.Picture(width,height)
    for rotateHeight in range(0,height):
        for rotateWidth in range(0,width):
            r,g,b = x.getPixelColor(rotateWidth,rotateHeight)
            picRotate.setPixelColor(width-1-rotateWidth,height-1-rotateHeight,r,g,b)
    return picRotate
def blur(x):
    height = x.getHeight()
    width = x.getWidth()
    picBlur = picture2.Picture(width,height)
    for blurHeight in range(0,height):
        for blurWidth in range(0,width):
            if not blurHeight==0 and not blurHeight==(height-1) and not blurWidth==0 and not blurWidth==(width-1):
                r1,g1,b1 = x.getPixelColor(blurWidth-1,blurHeight-1)
                r2,g2,b2 = x.getPixelColor(blurWidth-1,blurHeight)
                r3,g3,b3 = x.getPixelColor(blurWidth-1,blurHeight+1)
                r4,g4,b4 = x.getPixelColor(blurWidth,blurHeight-1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r6,g6,b6 = x.getPixelColor(blurWidth,blurHeight+1)
                r7,g7,b7 = x.getPixelColor(blurWidth+1,blurHeight-1)
                r8,g8,b8 = x.getPixelColor(blurWidth+1,blurHeight)
                r9,g9,b9 = x.getPixelColor(blurWidth+1,blurHeight+1)
                picBlur.setPixelColor(blurWidth,blurHeight,(r1+r2+r3+r4+r5+r6+r7+r8+r9)/9,(g1+g2+g3+g4+g5+g6+g7+g8+g9)/9,(b1+b2+b3+b4+b5+b6+b7+b8+b9)/9)
            elif not blurHeight==0 and not blurHeight==(height-1) and blurWidth==0:
                r4,g4,b4 = x.getPixelColor(blurWidth,blurHeight-1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r6,g6,b6 = x.getPixelColor(blurWidth,blurHeight+1)
                r7,g7,b7 = x.getPixelColor(blurWidth+1,blurHeight-1)
                r8,g8,b8 = x.getPixelColor(blurWidth+1,blurHeight)
                r9,g9,b9 = x.getPixelColor(blurWidth+1,blurHeight+1)
                picBlur.setPixelColor(blurWidth,blurHeight,(r4+r5+r6+r7+r8+r9)/6,(g4+g5+g6+g7+g8+g9)/6,(b4+b5+b6+b7+b8+b9)/6)
            elif not blurHeight==0 and not blurHeight==(height-1) and blurWidth==(width-1):
                r1,g1,b1 = x.getPixelColor(blurWidth-1,blurHeight-1)
                r2,g2,b2 = x.getPixelColor(blurWidth-1,blurHeight)
                r3,g3,b3 = x.getPixelColor(blurWidth-1,blurHeight+1)
                r4,g4,b4 = x.getPixelColor(blurWidth,blurHeight-1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r6,g6,b6 = x.getPixelColor(blurWidth,blurHeight+1)
                picBlur.setPixelColor(blurWidth,blurHeight,(r1+r2+r3+r4+r5+r6)/9,(g1+g2+g3+g4+g5+g6)/9,(b1+b2+b3+b4+b5+b6)/9)
            elif blurHeight==0 and not blurWidth==0 and not blurWidth==(width-1):
                r2,g2,b2 = x.getPixelColor(blurWidth-1,blurHeight)
                r3,g3,b3 = x.getPixelColor(blurWidth-1,blurHeight+1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r6,g6,b6 = x.getPixelColor(blurWidth,blurHeight+1)
                r8,g8,b8 = x.getPixelColor(blurWidth+1,blurHeight)
                r9,g9,b9 = x.getPixelColor(blurWidth+1,blurHeight+1)
                picBlur.setPixelColor(blurWidth,blurHeight,(r2+r3+r5+r6+r8+r9)/9,(g2+g3+g5+g6+g8+g9)/9,(b2+b3+b5+b6+b8+b9)/6)
            elif blurHeight==(height-1) and not blurWidth==0 and not blurWidth==(width-1):
                r1,g1,b1 = x.getPixelColor(blurWidth-1,blurHeight-1)
                r2,g2,b2 = x.getPixelColor(blurWidth-1,blurHeight)
                r4,g4,b4 = x.getPixelColor(blurWidth,blurHeight-1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r7,g7,b7 = x.getPixelColor(blurWidth+1,blurHeight-1)
                r8,g8,b8 = x.getPixelColor(blurWidth+1,blurHeight)
                picBlur.setPixelColor(blurWidth,blurHeight,(r1+r2+r4+r5+r7+r8)/6,(g1+g2+g4+g5+g7+g8)/6,(b1+b2+b4+b5+b7+b8)/6)
            if blurHeight==0 and blurWidth==0:
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r6,g6,b6 = x.getPixelColor(blurWidth,blurHeight+1)
                r8,g8,b8 = x.getPixelColor(blurWidth+1,blurHeight)
                r9,g9,b9 = x.getPixelColor(blurWidth+1,blurHeight+1)
                picBlur.setPixelColor(blurWidth,blurHeight,(r5+r6+r8+r9)/6,(g5+g6+g8+g9)/6,(b5+b6+b8+b9)/4)
            elif blurHeight==(height-1) and blurWidth==0:
                r4,g4,b4 = x.getPixelColor(blurWidth,blurHeight-1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r7,g7,b7 = x.getPixelColor(blurWidth+1,blurHeight-1)
                r8,g8,b8 = x.getPixelColor(blurWidth+1,blurHeight)
                picBlur.setPixelColor(blurWidth,blurHeight,(r4+r5+r7+r8)/4,(g4+g5+g7+g8)/4,(b4+b5+b7+b8)/4)
            elif blurHeight==0 and blurWidth==(width-1):
                r2,g2,b2 = x.getPixelColor(blurWidth-1,blurHeight)
                r3,g3,b3 = x.getPixelColor(blurWidth-1,blurHeight+1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                r6,g6,b6 = x.getPixelColor(blurWidth,blurHeight+1)
                picBlur.setPixelColor(blurWidth,blurHeight,(r2+r3+r5+r6)/4,(g2+g3+g5+g6)/4,(b2+b3+b5+b6)/4)
            elif blurHeight==(height-1) and blurWidth==(width-1):
                r1,g1,b1 = x.getPixelColor(blurWidth-1,blurHeight-1)
                r2,g2,b2 = x.getPixelColor(blurWidth-1,blurHeight)
                r4,g4,b4 = x.getPixelColor(blurWidth,blurHeight-1)
                r5,g5,b5 = x.getPixelColor(blurWidth,blurHeight)
                picBlur.setPixelColor(blurWidth,blurHeight,(r1+r2+r4+r5)/4,(g1+g2+g4+g5)/4,(b1+b2+b4+b5)/4)
    return picBlur

def contrast(x):
    height = x.getHeight()
    width = x.getWidth()
    picContrast = picture2.Picture(width, height)
    for contrastHeight in range(0,height):
        for contrastWidth in range(0,width):
            r,g,b=x.getPixelColor(contrastWidth, contrastHeight)
            if 64<r<128:
                r = 128-(128-r)*2
            elif r<=64:
                r = 0
            elif 128<r<192:
                r = 128+(r-128)*2
            elif r>=192:
                r = 255
            if 64<g<128:
                g = 128-(128-g)*2
            elif g<=64:
                g = 0
            elif 128<g<192:
                g = 128+(g-128)*2
            elif g>=192:
                g = 255
            if 64<b<128:
                b = 128-(128-b)*2
            elif b<=64:
                b = 0
            elif 128<b<192:
                b = 128+(b-128)*2
            elif b>=192:
                b = 255
            picContrast.setPixelColor(contrastWidth, contrastHeight, r, g, b)
    return picContrast

def noblue(x):
    height = x.getHeight()
    width = x.getWidth()
    picNoblue = picture2.Picture(width, height)
    for noblueHeight in range(0,height):
        for noblueWidth in range(0,width):
            r,g, b = x.getPixelColor(noblueWidth, noblueHeight)
            b = 0
            picNoblue.setPixelColor(noblueWidth, noblueHeight, r, g, b)
    return picNoblue

def decontrast(x):
    height = x.getHeight()
    width = x.getWidth()
    picDecontrast = picture2.Picture(width, height)
    for decontrastHeight in range(0,height):
        for decontrastWidth in range(0,width):
            r,g,b=x.getPixelColor(decontrastWidth, decontrastHeight)
            if r<128:
                r = 128-(128-r)//2
            elif 128<r:
                r = 128+(r-128)//2
            if g<128:
                g = 128-(128-g)//2
            elif 128<g:
                g = 128+(g-128)//2
            if b<128:
                b = 128-(128-b)//2
            elif 128<b:
                b = 128+(b-128)//2
            picDecontrast.setPixelColor(decontrastWidth, decontrastHeight, r, g, b)
    return picDecontrast
    
def main():
    fileName = raw_input("Please enter the image file you'd like loaded: ")
    pic = picture2.Picture(fileName)
    print"\n1. Flip Horizontally\n2. Mirror Horizontally\n3. Scroll Horizontally\n4. Make Negative\n5. Make Grayscale\n6. Cycle Color Channels\n7. Zoom\n8. Posterize\n9. Change Brightness\n10. Increase Contrast\n11 Blur\n12 Rotate 180 Degrees\n13. No Blue\n14 Decrease Contrast"
    n = eval(raw_input("List the effect number you'd like to see (Press Enter afterwards):"))
    finished = False
    while not finished:
        if n==1:
            picFlip = flip(pic)
            picFlip.display()
            pic = picFlip
            raw_input()
        elif n==2:
            picMirror = mirror(pic)
            picMirror.display()
            pic = picMirror
            raw_input()
        elif n==3:
            picScroll = scroll(pic)
            picScroll.display()
            pic = picScroll
            raw_input()
        elif n==4:
            picNeg = neg(pic)
            picNeg.display()
            pic = picNeg
            raw_input()
        elif n==5:
            picGray = gray(pic)
            picGray.display()
            pic = picGray
            raw_input()
        elif n==6:
            picCycle = cycle(pic)
            picCycle.display()
            pic = picCycle
            raw_input()
        elif n==7:
            picZoom = zoom(pic)
            picZoom.display()
            pic = picZoom
            raw_input()
        elif n==8:
            picPoster = poster(pic)
            picPoster.display()
            pic = picPoster
            raw_input()
        elif n==9:
            picBright = bright(pic)
            picBright.display()
            pic = picBright
            raw_input()
        elif n==10:
            picContrast = contrast(pic)
            picContrast.display()
            pic = picContrast
            raw_input()
        elif n==11:
            picBlur = blur(pic)
            picBlur.display()
            pic = picBlur
            raw_input()
        elif n==12:
            picRotate = rotate(pic)
            picRotate.display()
            pic = picRotate
            raw_input()
        elif n==13:
            picNoblue = noblue(pic)
            picNoblue.display()
            pic = picNoblue
            raw_input()
        elif n==14:
            picDecontrast = decontrast(pic)
            picDecontrast.display()
            pic = picDecontrast
            raw_input()
        done = raw_input("Would you like another effect? Y/N")
        if done=="N":
            finished = True
        elif done=="Y":
            n = eval(raw_input("What other effect would you like? Pick a number and press Enter afterwards:"))
    raw_input()
    
main()