# automatedLabHelper
Jane Hsieh, Emily Hamlin, Adina Johnson

## Overview of our project
Novice programmers often encounter similar issues in programming. Students in an introductory computer science course such as CSCI 150 offered here at Oberlin are no exception. Even though the class has been carefully designed to provide students with a multitude of resources (such as instructors, student lab helpers, and office hours), a portion of the class may still be intimidated or embarrassed to ask for guidance. Two of our team members have experience in lab helping CSCI 150 and have noticed that students often run into similar errors on their programming assignments. This provides us with an opportunity to detect common errors from past student homework solutions and utilize knowledge from student responses in README reports as well as our own lab-helping experience to compile a list of suggested solutions for the more commonly occurring problems. The “intelligent” component of our program will be able to form answers to newer bugs and questions that have not been experienced in the past.

Our project is an automated lab helper designed to help CSCI 150 students find bugs in their code and develop a better understanding of common errors and how to fix them.

## Files

### helper.py
Our lab helper program can be run from the command line using `cleanOutput.py` (explained below), or using a Tkinter interface. The interface can be installed and run with

```
python3 launch.py
```
which opens up a launcher window for the virtual environment (installs the latest versions of pip and pylint). 

Once inside the virutal environment named "virtual", call
```
python3 helper.py
```


### cleanOutput.py
`cleanOutput.py` post-processes pylint output into more readable, less redundant output. Users who desire to see their output straight from the command line rather than through the tkinter interface can run `cleanOutput.py` on the CLI with

```
python3 cleanOutput.py [filename] [{c,r,w,e,f,C,R,W,E,F}<sup>\*</sup>]
```

where the final parameter is a string containing some subset of the characters `CRWEFcwerf`. Lowercase 'c','r', 'w','e',and 'f' lists line numbers where convention/warning messages are found for each type of message (organized by message code), while their capitalized counterparts give the full list of messages outputted from pylint in addition to the lists of line numbers by message type. The meanings of each letter is as follows:

* **C/c (Convention):**  denotes style-based warnings. They don't have anything to do with the correctness of the code, but simply check whether the code matches python code conventions/standards, and so they can for the most part be safely ignored by 150 students when debugging.
* **R/r (Refactor):** denotes warnings for bad "code smell", which means code that is generally written in a way that isn't optimal (i.e. includes duplicated code, large and confusing classes, etc.).
* **W/w (Warning):** refers to warnings related to python specifically. These will likely be useful for 150 stuents to look at.
* **E/e (Error):** refers to actual bugs in the code. Errors are also generally important to look at.
* **F/f (Fatal):** means that there is a problem with the output of pylint.

These 5 message types are the same as those used by pylint (see https://docs.pylint.org/en/1.6.0/tutorial.html).

### regexChecks.py
`regexChecks.py` contains a function called `check(line)`, which takes in a string and compares it to each of the defined regexes. `regexChecks.py` is called by `cleanOutput.py` to help catch syntax errors caused by mistakes such as forgetting colons and parentheses.

### ranking.py

`ranking.py` takes in a list of folders and reads each python file in each of the folders. It then outputs a list of pylint messages and the number of times each message was found throughout all the files. Call `ranking.py` as follows:
```
ranking.py [-h] [-a] [-p] folders [folders ...]
```
where `-h` displays the following information:
```
positional arguments:
  folders         list the paths to folders you want to read from (including /
                  after folder name)

optional arguments:
  -h, --help      show this help message and exit
  -a, --all       print all messages (including those with value 0)
  -p, --progress  print the name of each file as it is processed
```

By default, `ranking.py` will only output message codes with prevalences greater than 0.

### checkers/return-not-caught-checker.py (located under checkers folder)

`return-not-caught-checker.py` is a checker for pylint. It checks whether a function has a return value. If the function is called, it checks whether the return value from the function is saved. For example, it would produce a warning for the following code:

```python3
def test():
    return 2

def main():
    test()

if __name__ == '__main__':
    main()
```

but would not return an error if `test()` was replaced with `retVal = test()`. It doesn't work in all cases yet (for instance, it would return an error for something like `print(test())`).

## Progress

### TODO:
<<<<<<< HEAD
- Run our program on example files from 150 to determine utility of each error based on frequency of occurence in past student code
- Find sites that targets/is often visited or popular among beginning Python coders and scrape from each for example code or demos / articles / documentation.
=======
* Run our program on example files from 150 to determine utility of each error based on frequency of occurence in past student code
* Find sites that targets/is often visited or popular among beginning Python coders and scrape from each for example code or demos/articles/documentation.
>>>>>>> 6146636577e6eb420b1cd23e454bec274ce18e73

### DONE:
* Basic interface for making installing and file browsing easier
* Make it possible to run cleanoutput on interface
* Written a custom checker
* Figure out how to package pylint in environments

## Miscellaneous

List of some codes: http://pylint-messages.wikidot.com/all-codes (has been copied to allCodes.txt for cleaning)

List of all codes: https://docs.pylint.org/en/1.6.0/features.html
