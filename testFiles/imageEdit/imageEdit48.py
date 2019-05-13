






import picture2
import random
copy=0
def main():
    print "Hello, this is an image editor. You are SO fortunate to have stumbled upon it."
    user_input=False
    while user_input==False:
        try:
            user_picture = raw_input("Please enter the file of the picture you wish to be manipulated: ")
            pic=picture2.Picture(user_picture)
            user_input=True
        except IOError:
            print "typo?"
            
    
    h=pic.getHeight()
    w=pic.getWidth()
    pic.display()
    user_input=False

    while user_input==False:
        print
        print "Please enter one of the following options:"
        print 'scroll,copy,colorCycle,posterize,fuzz,superimpose'
        print 'zoom,startOver,rotate,contrast'
        print 'negate,greyscale,flip,mirrorRight'
        n = raw_input("mirrorLeft,brightness,blur,exit: ")
        if n == "negate":
            negate(w,h,pic)
            pic.display()
        elif n == "greyscale":
            greyscale(w,h,pic)
            pic.display()
        elif n == "flip":
            flip(w,h,pic)
            pic.display()
        elif n=="exit":
            user_input=True
        elif n=="mirrorRight":
            mirrorRight(w,h,pic)
            pic.display()
        elif n=="mirrorLeft":
            mirrorLeft(w,h,pic)
            pic.display()
        elif n=="copy":
            copy=make_copy(w,h,pic)
            copy.display()
        elif n=="scroll":
            scroll(w,h,pic)
            pic.display()
        elif n=="colorCycle":
            color_cycle(w,h,pic)
            pic.display()
        elif n=="posterize":
            posterize(w,h,pic)
            pic.display()
        elif n=="fuzz":
            print "(wait for it...)"
            for i in range(5):
                fuzz(w,h,pic)
            pic.display()
        elif n=="zoom":
            zoom(w,h,pic)
            pic.display()
        elif n=="superimpose":
            superimpose(w,h,pic)
            pic.display()
        elif n=="startOver":
            start_over(w,h,pic,user_picture)
            pic.display()
        elif n=="contrast":
            contrast(w,h,pic)
            pic.display()
        elif n=="rotate":
            rotate(w,h,pic)
            pic.display()
        elif n=="blur":
            blur(w,h,pic)
            pic.display()
        elif n=="brightness":
            brightness(w,h,pic)
            pic.display()
        else:
            print
            print "You seemed to have entered a typo."
            print "Please try again, if that's ok with you."


def negate(w,h,pic):
    for i in range(w):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,255-n,255-m,255-p)
    return pic

def greyscale(w,h,pic):
    for i in range(w):
        for j in range(h):
            n,m,p = pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,(n+m+p)//3,(n+m+p)//3,(n+m+p)//3)
    return pic
def flip(w,h,pic):
    for i in range((w)//2):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            N,M,P=pic.getPixelColor(w-1-i,j)
            pic.setPixelColor(i,j,N,M,P)
            pic.setPixelColor(w-i-1,j,n,m,p)
def scroll(w,h,pic):
    d=eval(raw_input("Please input the amount of pixels you wish to scroll by: "))
    copy=make_copy(w,h,pic)
    for i in range((w)):
        for j in range(h):
            n,m,p=copy.getPixelColor(i,j)
            pic.setPixelColor((i+d)%(w),j,n,m,p)
def mirrorLeft(w,h,pic):
    for i in range((w//2)):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            N,M,P=pic.getPixelColor(w-1-i,j)
            pic.setPixelColor(i,j,N,M,P)
def mirrorRight(w,h,pic):
    for i in range((w//2)):
        for j in range(h-1):
            n,m,p=pic.getPixelColor(i,j)
            N,M,P=pic.getPixelColor(w-1-i,j)
            pic.setPixelColor(w-1-i,j,n,m,p)
def make_copy(w,h,pic):
    copy=picture2.Picture(w,h)
    for i in range(w):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            copy.setPixelColor(i,j,n,m,p)
    return copy
def color_cycle(w,h,pic):
    for i in range(w):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,p,n,m)
def posterize(w,h,pic):
    for i in range(w):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,n-(n%32),m-(m%32),p-(p%32))
def fuzz(w,h,pic):
    for i in range(w):
        for j in range(h):
            t=random.randint(-50,50)
            n,m,p=pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,(n+t),(m+t),(p+t))
def start_over(w,h,pic,user_picture):
    copy=picture2.Picture(user_picture)
    for i in range(w):
        for j in range(h):
            n,m,p=copy.getPixelColor(i,j)
            pic.setPixelColor(i,j,n,m,p)
def superimpose(w,h,pic):
    copy=make_copy(w,h,pic)
    print
    print "SUPERIMPOSE: Please enter one of the following options"
    print "to superimpose on the original:"
    print 'scroll,colorCycle,posterize,fuzz,'
    print 'zoom,rotate,contrast,brightness,blur'
    n = raw_input("negate,greyscale,flip,mirrorRight,mirrorLeft: ")
    if n == "negate":
        negate(w,h,copy)
    elif n == "greyscale":
        greyscale(w,h,copy)
    elif n == "flip":
        flip(w,h,copy)
    elif n=="mirrorRight":
        mirrorRight(w,h,copy)
    elif n=="mirrorLeft":
        mirrorLeft(w,h,copy)
    elif n=="scroll":
        scroll(w,h,copy)
    elif n=="colorCycle":
        color_cycle(w,h,copy)
    elif n=="posterize":
        posterize(w,h,copy)
    elif n=="fuzz":
        print "(wait for it...)"
        for i in range(5):
            fuzz(w,h,copy)
    elif n=="zoom":
        zoom(w,h,copy)
    elif n=="rotate":
        rotate(w,h,copy)
    elif n=="contrast":
        contrast(w,h,copy)
    elif n =="brightness":
        brightness(w,h,copy)
    elif n =="blur":
        blur(w,h,copy)
    else:
        print
        print "typo"
    for i in range(w):
            for j in range(h):
                n,m,p=pic.getPixelColor(i,j)
                N,M,P=copy.getPixelColor(i,j)
                pic.setPixelColor(i,j,(N+n)//2,(M+m)//2,(P+p)//2)
def zoom(w,h,pic):
    copy=make_copy(w,h,pic)
    for i in range(0,w,2):
        for j in range(0,h,2):
            n,m,p=copy.getPixelColor(w/4+(i/2)%(w/2),h/4+(j/2)%(h/2))
            pic.setPixelColor(i,j,n,m,p)
            pic.setPixelColor(i+1,j,n,m,p)
            pic.setPixelColor(i,j+1,n,m,p)
            pic.setPixelColor(i+1,j+1,n,m,p)
def contrast(w,h,pic):
    for i in range(w):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,((n-128)*2)+128,((m-128)*2)+128,((p-128)*2)+128)
def rotate(w,h,pic):
    copy=make_copy(w,h,pic)
    for i in range(w):
        for j in range(h):
            n,m,p=copy.getPixelColor(w-1-i,h-1-j)
            pic.setPixelColor(i,j,n,m,p)
def blur(w,h,pic):
    copy=make_copy(w,h,pic)
    for i in range(1,w-1):
        for j in range(1,h-1):
            n,m,p=copy.getPixelColor(i,j)
            n1,m1,p1=copy.getPixelColor(i+1,j)
            n2,m2,p2=copy.getPixelColor(i+1,j+1)
            n3,m3,p3=copy.getPixelColor(i+1,j-1)
            n4,m4,p4=copy.getPixelColor(i,j+1)
            n5,m5,p5=copy.getPixelColor(i,j-1)
            n6,m6,p6=copy.getPixelColor(i-1,j)
            n7,m7,p7=copy.getPixelColor(i-1,j+1)
            n8,m8,p8=copy.getPixelColor(i-1,j-1)
            N = (n+n1+n2+n3+n4+n5+n6+n7+n8)//9
            M = (m+m1+m2+m3+m4+m5+m6+m7+m8)//9
            P = (p+p1+p2+p3+p4+p5+p6+p7+p8)//9
            pic.setPixelColor(i,j,N,M,P)
def brightness(w,h,pic):
    x = eval(raw_input("Please enter the amount by which you wish to change the brightness: "))
    for i in range(w):
        for j in range(h):
            n,m,p=pic.getPixelColor(i,j)
            pic.setPixelColor(i,j,(n+x)-(n+x)//255,(m+x)-(m+x)//255,(p+x)-(p+x)//255)
main()

    