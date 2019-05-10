
def protein_seq(protein, marker, sequence):
	position = 0
	z = len(protein) - len(marker)
	e = len(protein)
	for x in range(z) :
		m = x
		n = 0
		for v in range(len(marker)): 
			if protein[x] != marker[v] :
				n = n + 1
			m= m + 1
	
		if n<e :
			e = n
			position = x
		
		
	print (sequence ,"has ",e," errors at position ",position,".")
		
def main():
		thefile = input("file name?")	
		file = open(thefile, "r")
		protein = ""
		sequence = 1
		for line in file:
			if sequence == 1:
				protein = line
				sequence = sequence + 1
			else:	
				protein_seq(protein, line, sequence)
				sequence = sequence +1
main()
		
		
	
