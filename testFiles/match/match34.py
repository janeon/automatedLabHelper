





def main():
	file = open("text.txt","r")
	lines = file.readlines()
	for j in range(1,len(lines)): 
		q = len(lines[0]) 
		r = len(lines[j]) 
		s = q-r 
		e=[]
		for i in range(s):
			e.append(0)
			
		for x in range(s): 
			for y in range(r): 
				if lines[0][x+y] != lines[j][y]:
					e[x] = e[x]+1
		for n in range(len(e)):
			e[n] = e[n]-1
		print("Sequence ",j," has ",min(e)," errors at position ",e.index(min(e)),".",sep='')
main()