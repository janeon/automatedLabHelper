





import picture2

def main():
    pic = picture2.Picture("crayons.bmp")
    pic = scroll(pic)
    pic.display()
    input()

def flip(pic):
    height = pic.getHeight()
    width = pic.getWidth()
    for y in range(0, height - 1):
        for x in range(0, (width - 1) / 2):
            r1, g1, b1 = pic.getPixelColor(x, y)
            r2, g2, b2 = pic.getPixelColor((width - 1) - x, y)
            pic.setPixelColor(x, y, r2, g2, b2)
            pic.setPixelColor((width - 1) - x, y, r1, g1, b1)
    return 

def scroll(pic):
    height = pic.getHeight()
    width = pic.getWidth()
    for y in range(0, height - 1):
        for x in range(0, (width - 1) / 2):
            r1, g1, b1 = pic.getPixelColor(x, y)
            r2, g2, b2 = pic.getPixelColor((width - 1) - x, y)
            pic.setPixelColor(x, y, r2, g2, b2)
            pic.setPixelColor((width - 1) - x, y, r1, g1, b1)
main()