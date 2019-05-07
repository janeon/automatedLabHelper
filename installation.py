#import os


#os.system("virtualenv -p python3 virtual 1> /dev/null")
#os.system("source activate;python -V")
#os.system("/bin/bash  --rcfile virtual/bin/activate 1> /dev/null")
 



#!/bin/bash

# install & activate python3 virtual environment called "virtual"
#python3 -m virtualenv virtual 1> /dev/null
#virtualenv -p python3 virtual
#. virtual/bin/activate
# https://askubuntu.com/questions/1131539/make-virtualenv-and-activate-it-with-shell-script
# https://stackoverflow.com/questions/14967032/error-when-installing-python-settuptools-no-such-file-or-directory-usr-loca

# # install pylint
#pip3 install pylint

# adding and running our custom checkers
# rsync -r checkers/ virtual/lib/python3.5/site-packages/pylint/checkers/
# cp -r ./checkers/. ./virtual/lib/python3.5/site-packages/pylint/checkers/
# cp -R checkers/* virtual/lib/python3.5/site-packages/pylint/checkers/
# running pylint and postprocessing errors
# python3 cleanOutput.py testreturnnotcaught.py WEc
