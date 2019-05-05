#!/bin/bash

# install & activate python3 virtual environment called "virtual"
virtualenv -p python3 virtual 1> /dev/null
source virtual/bin/activate 1> /dev/null
# https://askubuntu.com/questions/1131539/make-virtualenv-and-activate-it-with-shell-script
# https://stackoverflow.com/questions/14967032/error-when-installing-python-settuptools-no-such-file-or-directory-usr-loca

# # install pylint
pip3 install pylint 1> /dev/null

# adding and running our custom checkers
cp -R checkers/* virtual/lib/python3.5/site-packages/pylint/checkers/

# running pylint and postprocessing errors
python3 cleanOutput.py testreturnnotcaught.py WEc
