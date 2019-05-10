



def main():
   fileName = input("Choose a file: ")
   inputFile = open(fileName, 'r')
   CODE = inputFile.readline()
   Match = 0
   Mismatch = 0
   newline = 0
   for line in inputFile:
      errors = len(line)
      position = 0
      newline = newline + 1
      line = line[:-1]
      for j in range(len(CODE) - len(line)):
         for i in range(len(line)):
            if CODE[i + j] == line[i]:
               Match = Match + 1
            else:
               Mismatch = Mismatch + 1
         if Mismatch <  errors:
            errors = Mismatch
            position = j
         Match = 0
         Mismatch = 0
      print("Sequence", newline, "has", errors, "errors at position", position)

main()