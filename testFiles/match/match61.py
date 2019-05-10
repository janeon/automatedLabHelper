





def main():
  goodInput = False
  while not goodInput:
    try:
      file = input("Please enter your file you want coded >>> ")
      inputFile = open(file,"r")
      goodInput = True
      protein = inputFile.readline() 
      for match in inputFile:
        errorList = []
        least = 100000
        position = 0
        for i in range(len(protein)):
          errors = 0
          for j in range((len(match)-1)): 
              if i + j < len(protein):
                  if protein[i+j] != match[j]:
                      errors = errors + 1
          if i + j < len(protein):
            errorList.append(errors)
          for z in range(len(errorList)):
            if errorList[z] < least:
              least = errorList[z]
              position = z
        print("Sequence", match, "has", least, "errors at position", position) 
      
    except IOError:
      print("Please enter a valid file")
   
main()