from subprocess import *
import os

def main():
    matchFiles = os.listdir("testFiles/match")
    #print(matchFiles)
    for file in matchFiles:
        fileName = "testFiles/match/"+file
        call = "python3 cleanOutput.py "+fileName+" CWERF"
        result = check_output(call.split(" ")).decode("utf-8")
        print(result)



    # for index in range(1,93):
    #     try:
    #         fileName = "testFiles/match/match"+str(index)+".py"
    #         call = "python3 cleanOutput.py "+fileName+" CWERF"
    #         result = check_output(call.split(" ")).decode("utf-8")
    #         print(result)
    #     except IOError as e:
    #         pass

if __name__ == "__main__":
    main()
