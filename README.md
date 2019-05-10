# automatedLabHelper
Jane Hsieh, Emily Hamlin, Adina Johnson

## Overview of our project
Novice programmers often encounter similar issues in programming. Students in an introductory computer science course such as CSCI 150 offered here at Oberlin are no exception. Even though the class has been carefully designed to provide students with a multitude of resources (such as instructors, student lab helpers, and office hours), a portion of the class may still be intimidated or embarrassed to ask for guidance. Two of our team members have experience in lab helping CSCI 150 and have noticed that students often run into similar errors on their programming assignments. This provides us with an opportunity to detect common errors from past student homework solutions and utilize knowledge from student responses in README reports as well as our own lab-helping experience to compile a list of suggested solutions for the more commonly occurring problems. The “intelligent” component of our program will be able to form answers to newer bugs and questions that have not been experienced in the past.

Our project is an automated lab helper designed to help CSCI 150 students find bugs in their code and develop a better understanding of common errors and how to fix them.

## Files

### interface.py
Our lab helper program can be run from the command line using `cleanOutput.py` (explained below), or using a Tkinter interface. The interface can be installed and run with

``` 
python3 install.py
```
which opens up a launcher window for the virtual environment, followed by
```
python3 interface.py
```

This will not only run pylint, it will also install the latest versions of pip, pylint, and virtualenv (in case your environment doesn't have them already) inside the virtual environment called virtual (which will appear in parentheses on the left of each CLI line).


### cleanOutput.py
`cleanOutput.py` post-processes pylint output into more readable, less redundant output. Users who desired to see their output straight from the command line rather than through the tkinter interface can run `cleanOutput.py` through the command line using the command

```bash
python3 cleanOutput.py [filename] [{c,r,w,e,f,C,R,W,E,F}`<sup>\*</sup>`]
```

where the final parameter is a string containing some subset of the characters `CRWEF`. ((**This isn't really true rn??:** Lowercase 'c','r', 'w','e',and 'f' lists line numbers where convention/warning messages are found for each type of message (organized by error code), while their capitalized counterparts give the full list of messages outputted from pylint in addition to the lists of line numbers by error type.)) The meanings of each letter is as follows:

* **C (Convention):**  denotes style-based warnings. They don't have anything to do with the correctness of the code, but simply check whether the code matches python code conventions/standards, and so they can for the most part be safely ignored by 150 students when debugging.
* **R (Refactor):** denotes warnings for bad "code smell", which means code that is generally written in a way that isn't optimal (i.e. includes duplicated code, large and confusing classes, etc.).
* **W (Warning):** refers to warnings related to python specifically. These will likely be useful for 150 stuents to look at.
* **E (Error):** refers to actual bugs in the code. Errors are also generally important to look at.
* **F (Fatal):** means that there is a problem with the output of pylint. ((check this))

These 5 error types are the same as those used by pylint (see https://docs.pylint.org/en/1.6.0/tutorial.html).

### regexChecks.py
`regexChecks.py` contains a function called `check(line)`, which takes in a string and compares it to each of the defined regexes. `regexChecks.py` is called by `cleanOutput.py` to help catch syntax errors caused by mistakes such as forgetting colons and parentheses.

### checkers/return-not-caught-checker.py

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

### installation.py??? Which of theses are still needed? Which can be removed?
likely that this one can be removed, could we test it on a lab machine sometime today? It'll take a second

### more stuff from earlier versions of the readme:

### TODO:
- Make it possible to run cleanoutput on interface
- Find sites that targets/is often visited or popular among beginning Python coders and scrape from each for example code or demos / articles / documentation.

### DONE:
- Basic interface for making installing and file browsing easier
- Written a custom checker
- Figure out how to package pylint in environments

Code types:

"I": "info",
"C": "convention",
"R": "refactor",
"W": "warning",
"E": "error",
"F": "fatal"

List of some codes: http://pylint-messages.wikidot.com/all-codes (has been copied to allCodes.txt for cleaning)

List of all codes: https://docs.pylint.org/en/1.6.0/features.html
