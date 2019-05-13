



import picture2
def main():
    goodInput = False
    while not goodInput:
        try:
            selection=raw_input("Please enter the name of the image you'd like to manipulate (including the .bmp): ")
            pic=picture2.Picture(selection)
            w=pic.getWidth()
            h=pic.getHeight()
            pic1=picCopy(w,h,pic)
            goodInput = True
            
        except:
            print("Please be sure to input the correct name of the various picture files or valid file types, etc.")
            print
    Boredom = False
    while not Boredom:
        bloopity=raw_input("If you're done messing around type in Bored. If not, type in the name of the function you'd like to run and please choose from: Horizontalflip, Horizontalscroll, Negative, Grayscale, Cyclecolors, Mirror, Posterize, Changebrightness, Increasecontrast, Blur, Zoom, Rotate180, Verticalscroll, or Turnuptheheat. When choosing a function please type the function exactly as shown in the previous sentence. If not, we'll print the original image for your viewing pleasure. Thanks!: ")
        if bloopity == "Horizontalflip":
            pic1=hflip(w,h,pic1)
        if bloopity == "Horizontalscroll":
            pic1=hscroll(w,h,pic1)
        if bloopity == "Negative":
            pic1=negatize(w,h,pic1)
        if bloopity == "Grayscale":
            pic1=grayscale(w,h,pic1)
        if bloopity == "Cyclecolors":
            pic1=cycle(w,h,pic1)
        if bloopity == "Posterize":
            pic1=poster(w,h,pic1)
        if bloopity == "Changebrightness":
            pic1=brightness(w,h,pic1)
        if bloopity == "Increasecontrast":
            pic1=inccontrast(w,h,pic1)
        if bloopity == "Blur":
            pic1=blur(w,h,pic1)
        if bloopity == "Zoom":
            pic1=zoom(w,h,pic1)
        if bloopity == "Rotate180":
            pic1=rotate180(w,h,pic1)
        if bloopity == "Turnuptheheat":
            pic1=turnuptheheat(w,h,pic1)
        if bloopity == "Verticalscroll":
            pic1=vscroll(w,h,pic1)
        if bloopity == "Mirror":
            pic1=hmirror(w,h,pic1)
        if bloopity == "Bored":
            Boredom = True
        pic1.display()
        raw_input("Please press any key and then <enter> to continue.")

    
def picCopy(w,h,pic):
    pic1 = picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            colors = pic.getPixelColor(i,j)
            pic1.setPixelColor(i,j,colors[0],colors[1],colors[2])
    return pic1
    
    
    
    
def hmirror(w,h,pic1):
    for i in range(w):
        for j in range(h):
            mirror=pic1.getPixelColor(i,j)
            pic1.setPixelColor((w-1-i),j,mirror[0],mirror[1],mirror[2])
    return pic1

def hflip(w,h,pic1):
    picflip = picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            flip=pic1.getPixelColor(i,j)
            picflip.setPixelColor((w-1-i),j,flip[0],flip[1],flip[2])
    return picflip

def hscroll(w,h,pic1):
    goodInput = False
    while not goodInput:
        try:
            d=input("Please enter the amount by which you'd like to scroll the image: ")
            picScroll = picture2.Picture(w,h)
            for i in range(w):
                for j in range(h):
                    scroll=pic1.getPixelColor(i,j)
                    picScroll.setPixelColor((i+d)%w,j,scroll[0],scroll[1],scroll[2])
            return picScroll
        except NameError:
            print("Please enter numbers.")

def negatize(w,h,pic1):
    picnegative = picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            negatives=pic1.getPixelColor(i,j)
            picnegative.setPixelColor(i,j,255-negatives[0],255-negatives[1],255-negatives[2])
    return picnegative
    
def grayscale(w,h,pic1):
    picgray = picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            gray=pic1.getPixelColor(i,j)
            grayavg=(gray[0]+gray[1]+gray[2])//3
            picgray.setPixelColor(i,j,grayavg,grayavg,grayavg)
    return picgray

def cycle(w,h,pic1):
    piccycle = picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            cycl=pic1.getPixelColor(i,j)
            piccycle.setPixelColor(i,j,cycl[2],cycl[0],cycl[1])
    return piccycle


    
def poster(w,h,pic1):
    picposter = picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            color=pic1.getPixelColor(i,j)
            blah0=color[0]%32
            blah1=color[1]%32
            blah2=color[2]%32
            if blah0 <= 15:
                sth0 = color[0]-blah0
            else:
                sth0 = color[0]+32-blah0
            if blah1 <= 15:
                sth1 = color[1]-blah1
            else:
                sth1 = color[1]+32-blah1
            if blah2 <= 15:
                sth2 = color[2]-blah2
            else:
                sth2 = color[2]+32-blah2
            picposter.setPixelColor(i,j,sth0,sth1,sth2)
    return picposter

def brightness(w,h,pic1):
    goodInput = False
    while not goodInput:
        try:
            change = input("Please enter an integer value by which you'd like to change the brightness: ")
            bright = picture2.Picture(w,h)
            for i in range(w):
                for j in range(h):
                    brighten=pic1.getPixelColor(i,j)
                    blah0=brighten[0]+change
                    if (brighten[0]+change)>255:
                        blah0=255
                    if (brighten[0]+change)<0:
                        blah0=0
                    blah1=brighten[1]+change
                    if (brighten[1]+change)>255:
                        blah1=255
                    if (brighten[1]+change)<0:
                        blah1=0
                    blah2=brighten[2]+change
                    if (brighten[2]+change)>255:
                        blah2=255
                    if (brighten[2]+change)<0:
                        blah2=0    
                    bright.setPixelColor(i,j,blah0,blah1,blah2)
            return bright
        except NameError:
            print("Please enter numbers.")

def inccontrast(w,h,pic1):
    inccon=picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            thing=pic1.getPixelColor(i,j)
            if thing[0]>=128:
                blah0=((thing[0]-128)*2)+128
            if thing[0]<128:
                blah0=128-((128-thing[0])*2)
            if blah0>255:
                blah0=255
            if blah0<0:
                blah0=0
            if thing[1]>=128:
                blah1=((thing[1]-128)*2)+128
            if thing[1]<128:
                blah1=128-((128-thing[1])*2)
            if blah1>255:
                blah1=255
            if blah1<0:
                blah1=0
            if thing[2]>=128:
                blah2=((thing[2]-128)*2)+128
            if thing[2]<128:
                blah2=128-((128-thing[2])*2)
            if blah2>255:
                blah2=255
            if blah2<0:
                blah2=0
            inccon.setPixelColor(i,j,blah0,blah1,blah2)
    return inccon

def blur(w,h,pic1):
    blurry=picture2.Picture(w,h)
    for i in range(0,(w//3)-2):
        for j in range(0,(h//3)-2):
            blur0=pic1.getPixelColor(2+3*i,1+3*j)
            blur1=pic1.getPixelColor(1+3*i,3*j)
            blur2=pic1.getPixelColor(1+3*i,1+3*j)
            blur3=pic1.getPixelColor(1+3*i,2+3*j)
            blur4=pic1.getPixelColor(2+3*i,2+3*j)
            blur5=pic1.getPixelColor(3+3*i,2+3*j)
            blur6=pic1.getPixelColor(3+3*i,1+3*j)
            blur7=pic1.getPixelColor(2+3*i,3*j)
            blur8=pic1.getPixelColor(3+3*i,3*j)
            spot0=(blur0[0]+blur1[0]+blur2[0]+blur3[0]+blur4[0]+blur5[0]+blur6[0]+blur7[0]+blur8[0])/9
            spot1=(blur0[1]+blur1[1]+blur2[1]+blur3[1]+blur4[1]+blur5[1]+blur6[1]+blur7[1]+blur8[1])/9
            spot2=(blur0[2]+blur1[2]+blur2[2]+blur3[2]+blur4[2]+blur5[2]+blur6[2]+blur7[2]+blur8[2])/9
            blurry.setPixelColor(2+3*i,1+3*j,spot0,spot1,spot2)
            blurry.setPixelColor(1+3*i,3*j,spot0,spot1,spot2)
            blurry.setPixelColor(1+3*i,1+3*j,spot0,spot1,spot2)
            blurry.setPixelColor(1+3*i,2+3*j,spot0,spot1,spot2)
            blurry.setPixelColor(2+3*i,2+3*j,spot0,spot1,spot2)
            blurry.setPixelColor(3+3*i,2+3*j,spot0,spot1,spot2)
            blurry.setPixelColor(3+3*i,1+3*j,spot0,spot1,spot2)
            blurry.setPixelColor(2+3*i,3*j,spot0,spot1,spot2)
            blurry.setPixelColor(3+3*i,3*j,spot0,spot1,spot2)
    return blurry

def zoom(w,h,pic1):
    zoomy=picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            bloop=pic1.getPixelColor((w//4)+(i//2),(h//4)+(j//2))
            zoomy.setPixelColor(i,j,bloop[0],bloop[1],bloop[2])
    return zoomy

def rotate180(w,h,pic1):
    rotate=picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            flop=pic1.getPixelColor(i,j)
            rotate.setPixelColor(w-i-1,h-j-1,flop[0],flop[1],flop[2])
    return rotate

def turnuptheheat(w,h,pic1):
    goodInput = False
    while not goodInput:
        try:
            hotness=picture2.Picture(w,h)
            heatindex = input("Please enter an integer value by which you'd like to turn up the heat: ")
            for i in range(w):
                for j in range(h):
                    floggerbop=pic1.getPixelColor(i,j)
                    bloopster0=floggerbop[0]+heatindex
                    if floggerbop[0]+heatindex > 255:
                        bloopster0=255
                    if floggerbop[0]+heatindex < 0:
                        bloopster0=0
                    hotness.setPixelColor(i,j,bloopster0,floggerbop[1],floggerbop[2])
            return hotness
        except NameError:
            print("Please enter numbers.")

def vscroll(w,h,pic1):
    goodInput = False
    while not goodInput:
        try:
            d=input("Please enter the amount by which you'd like to scroll the image: ")
            picScroll2 = picture2.Picture(w,h)
            for i in range(w):
                for j in range(h):
                    scroll2=pic1.getPixelColor(i,j)
                    picScroll2.setPixelColor(i,(j+d)%h,scroll2[0],scroll2[1],scroll2[2])
            return picScroll2
        except NameError:
            print("Please enter numbers.")

main()



