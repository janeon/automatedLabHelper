





import picture2
import os
import random

def copy(pic):
	h = pic.getHeight()
	w = pic.getWidth()
	picCopy = picture2.Picture(w,h)
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			g = pic.getPixelGreen(i,j)
			b = pic.getPixelBlue(i,j)
			picCopy.setPixelColor(i,j,r,g,b)
	return picCopy

def bigCopy(pic):
	h = pic.getHeight()
	w = pic.getWidth()
	picCopy = picture2.Picture(2*w,2*h)
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			g = pic.getPixelGreen(i,j)
			b = pic.getPixelBlue(i,j)
			J = 2*j
			I = 2*i
			picCopy.setPixelColor(I,J,r,g,b)
			picCopy.setPixelColor((I+1),J,r,g,b)
			picCopy.setPixelColor(I,(J+1),r,g,b)
			picCopy.setPixelColor((I+1),(J+1),r,g,b)
	return picCopy

def flipHorizotal(h,w,pic):
	picCopy = copy(pic)
	for i in range(1,w):
		for j in range(1,h):
			r = picCopy.getPixelRed(w-i,j)
			g = picCopy.getPixelGreen(w-i,j)
			b = picCopy.getPixelBlue(w-i,j)
			pic.setPixelColor(i,j,r,g,b)
	return pic

def mirrorHorizontal(h,w,pic):
	for i in range(1,w):
		for j in range(1,h):
			r = pic.getPixelRed(w-i,j)
			g = pic.getPixelGreen(w-i,j)
			b = pic.getPixelBlue(w-i,j)
			pic.setPixelColor(i,j,r,g,b)
	return pic

def scrollHorizontal(h,w,pic):
	try:
		d = int(raw_input("By how many pixels shall me sroll right? "))
	except ValueError:
		print "I don\'t know why I expected any better... *SIGH*"
		return pic
	except TypeError:
		print "I don\'t know why I expected any better... *SIGH*"
		return pic
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed((i+d)%w,j)
			g = pic.getPixelGreen((i+d)%w,j)
			b = pic.getPixelBlue((i+d)%w,j)
			pic.setPixelColor(i,j,r,g,b)
	return pic

def makeNegative(h,w,pic):
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			g = pic.getPixelGreen(i,j)
			b = pic.getPixelBlue(i,j)
			pic.setPixelColor(i,j,255-r,255-g,255-b)

def makeGrayscale(h,w,pic):
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			g = pic.getPixelGreen(i,j)
			b = pic.getPixelBlue(i,j)
			pic.setPixelColor(i,j,(r+g+b)/3,(r+g+b)/3,(r+g+b)/3)

def cycleColorChannels(h,w,pic):
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			g = pic.getPixelGreen(i,j)
			b = pic.getPixelBlue(i,j)
			pic.setPixelColor(i,j,b,r,g)
	return pic

def zoom(h,w,pic):
	picCopy = bigCopy(pic)
	for i in range(w):
		for j in range(h):
			r = picCopy.getPixelRed(i,j)
			g = picCopy.getPixelGreen(i,j)
			b = picCopy.getPixelBlue(i,j)
			pic.setPixelColor(i,j,r,g,b)
	return pic

def posterize(h,w,pic):
	picCopy = copy(pic)
	d=0
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			if r < 13:
				r = 0
			if r >= 13 and r < 26:
				r = 13
			if r >= 26 and r < 39:
				r = 26
			if r >= 52 and r < 65:
				r = 52
			if r >= 65 and r < 78:
				r = 65
			if r >= 78 and r < 91:
				r = 78
			if r >= 91 and r < 104:
				r = 91
			if r >= 104 and r < 117:
				r = 104
			if r >= 130 and r < 143:
				r = 130
			if r >= 143 and r < 156:
				r = 143
			if r >= 156 and r < 169:
				r = 156
			if r >= 182 and r < 195:
				r = 182
			if r >= 195 and r < 208:
				r = 195
			if r >= 208 and r < 221:
				r = 208
			if r >= 221:
				r = 221
			g = pic.getPixelGreen(i,j)
			if g < 13:
				g = 0
			if g >= 13 and g < 26:
				g = 13
			if g >= 26 and g < 39:
				g = 26
			if g >= 52 and g < 65:
				g = 52
			if g >= 65 and g < 78:
				g = 65
			if g >= 78 and g < 91:
				g = 78
			if g>= 91 and g < 104:
				g = 91
			if g >= 104 and g < 117:
				g = 104
			if g >= 130 and g < 143:
				g = 130
			if g >= 143 and g < 156:
				g = 143
			if g >= 156 and g < 169:
				g = 156
			if g >= 182 and g < 195:
				g = 182
			if g >= 195 and g < 208:
				g = 195
			if g >= 208 and g < 221:
				g = 208
			if g >= 221:
				g = 221
			b = pic.getPixelBlue(i,j)
			if b < 13:
				b = 0
			if b >= 13 and b < 26:
				b = 13
			if b >= 26 and b < 39:
				b = 26
			if b >= 52 and b < 65:
				b = 52
			if b >= 65 and b < 78:
				b = 65
			if b >= 78 and b < 91:
				b = 78
			if b >= 91 and b < 104:
				b = 91
			if b >= 104 and b < 117:
				b = 104
			if b >= 130 and b < 143:
				b = 130
			if b >= 143 and b < 156:
				b = 143
			if b >= 156 and b < 169:
				b = 156
			if b >= 182 and b < 195:
				b = 182
			if b >= 195 and b < 208:
				b = 195
			if b >= 208 and b < 221:
				b = 208
			if b >= 221:
				b = 221
			pic.setPixelColor(i,j,r,g,b)

def changeBrightness(h,w,pic):
	try:
		d = int(raw_input("How bright? "))
	except ValueError:
		print "I don\'t know why I expected any better... *SIGH*"
		return pic
	for i in range(w):
		for j in range(h):
			r = pic.getPixelRed(i,j)
			g = pic.getPixelGreen(i,j)
			b = pic.getPixelBlue(i,j)
			pic.setPixelColor(i,j,r+d,g+d,b+d)
	return pic

def increaseContrast(h,w,pic):
	picCopy = copy(pic)
	for i in range(w):
		for j in range(h):
			r = picCopy.getPixelRed(i,j)
			g = picCopy.getPixelGreen(i,j)
			b = picCopy.getPixelBlue(i,j)
			av = (r+b+g)/3
			move = av -127
			pic.setPixelColor(i,j,r+move,g+move,b+move)

def blur(h,w,pic):
	picCopy = copy(pic)
	for i in range(1,w-1):
		for j in range(1,h-1):
			r = (picCopy.getPixelRed(i-1,j-1)+picCopy.getPixelRed(i-1,j)+picCopy.getPixelRed(i-1,j+1)+picCopy.getPixelRed(i,j-1)+picCopy.getPixelRed(i,j)+picCopy.getPixelRed(i,j+1)+picCopy.getPixelRed(i+1,j-1)+picCopy.getPixelRed(i+1,j)+picCopy.getPixelRed(i+1,j+1))/9
			g = (picCopy.getPixelGreen(i-1,j-1)+picCopy.getPixelGreen(i-1,j)+picCopy.getPixelGreen(i-1,j+1)+picCopy.getPixelGreen(i,j-1)+picCopy.getPixelGreen(i,j)+picCopy.getPixelGreen(i,j+1)+picCopy.getPixelGreen(i+1,j-1)+picCopy.getPixelGreen(i+1,j)+picCopy.getPixelGreen(i+1,j+1))/9
			b = (picCopy.getPixelBlue(i-1,j-1)+picCopy.getPixelBlue(i-1,j)+picCopy.getPixelBlue(i-1,j+1)+picCopy.getPixelBlue(i,j-1)+picCopy.getPixelBlue(i,j)+picCopy.getPixelBlue(i,j+1)+picCopy.getPixelBlue(i+1,j-1)+picCopy.getPixelBlue(i+1,j)+picCopy.getPixelBlue(i+1,j+1))/9
			pic.setPixelColor(i,j,r,g,b)
	return pic

def rotate180degrees(h,w,pic):
	picCopy = copy(pic)
	for i in range(1,w-1):
		for j in range(1,h-1):
			r = picCopy.getPixelRed(w-i,h-j)
			g = picCopy.getPixelGreen(w-i,h-j)
			b = picCopy.getPixelBlue(w-i,h-j)
			pic.setPixelColor(i,j,r,g,b)
	return pic
	
def noise(h,w,pic):
	picCopy = copy(pic)
	for i in range(w):
		for j in range(h):
			q = random.randrange(-20,20)
			s = random.randrange(-20,20)
			t = random.randrange(-20,20)
			r = picCopy.getPixelRed(i,j)
			g = picCopy.getPixelGreen(i,j)
			b = picCopy.getPixelBlue(i,j)
			pic.setPixelColor(i,j,r+q,g+s,b+t)
	return pic
	
def restart(h,w,file):
	pic = picture2.Picture(file)
	r = random.randrange(256)
	b = random.randrange(256)
	g = random.randrange(256)
	pic.setPenColor(r,g,b)
	pic.drawCircleFill(95,90,90)
	print "Haha, JK, there is no perfect restart."
	return pic

def weird(h,w,pic):
	picCopy = copy(pic)
	for i in range(w):
		for j in range(h):
			r = picCopy.getPixelRed(i,j)
			g = picCopy.getPixelGreen(i,j)
			b = picCopy.getPixelBlue(i,j)
			move = 127-(r+g+b)/3
			pic.setPixelColor(i,j,r+move,g+move,b+move)
def main():
	n = 0
	os.system('clear')
	
	
	
	
	
	
	
	
	
	
	file = "estes.jpg"
	pic = picture2.Picture(file)
	h = pic.getHeight()
	w = pic.getWidth()
	os.system('clear')
	while n != 16:
		pic.display()
		print "What would you like to do to",file,"?"
		print "1-Flip Horizontally"
		print "2-Mirror Horizontally"
		print "3-Scroll Horizontally"
		print "4-Make Negative"
		print "5-Make Greyscale"
		print "6-Cycle Color Channels"
		print "7-Zoom"
		print "8-Posterize"
		print "9-Change Brightness"
		print "10-Increase Contrast"
		print "11-Blur"
		print "12-Rotate 180 Degrees"
		print "13-Make Noisy"
		print "14-Restart"
		print "15-Make it weird"
		print "16-Quit"
		print
		n=int(raw_input("Enter a command(1-16): "))
		if n > 16 or n < 1:
			os.system('clear')
			print "You have failed to perfectly follow simple instructions.\nTry again."
			n = 0
		if n == 1:
			os.system('clear')
			pic = flipHorizotal(h,w,pic)
		if n == 2:
			os.system('clear')
			pic = mirrorHorizontal(h,w,pic)
		if n == 3:
			os.system('clear')
			scrollHorizontal(h,w,pic,)
		if n == 4:
			os.system('clear')
			makeNegative(h,w,pic)
		if n == 5:
			os.system('clear')
			makeGrayscale(h,w,pic)
		if n == 6:
			os.system('clear')
			cycleColorChannels(h,w,pic)
		if n == 7:
			os.system('clear')
			zoom(h,w,pic)
		if n == 8:
			os.system('clear')
			posterize(h,w,pic)
		if n == 9:
			os.system('clear')
			changeBrightness(h,w,pic)
		if n == 10:
			os.system('clear')
			increaseContrast(h,w,pic)
		if n == 11:
			os.system('clear')
			blur(h,w,pic)
		if n == 12:
			os.system('clear')
			rotate180degrees(h,w,pic)
		if n == 13:
			os.system('clear')
			noise(h,w,pic)
		if n == 14:
			os.system('clear')
			pic = restart(h,w,file)
		if n == 15:
			os.system('clear')
			weird(h,w,pic)
	os.system('clear')
	print "Goodbye."
main()