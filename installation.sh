#!/bin/bash
# This bash script was made possible by:
# https://askubuntu.com/questions/1131539/make-virtualenv-and-activate-it-with-shell-script

# installing pip
# commented out because it turns out that lab machines require admin access to install pip3
# curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py 1> /dev/null

# installing and activating a python virtual env
# python3 -m pip install virtualenv 1> /dev/null
deactivate 1> /dev/null
python3 -m virtualenv virtual 1> /dev/null
source virtual/bin/activate 1> /dev/null

# installing pylint
pip install pylint 1> /dev/null

# adding and running our custom checkers

# custom checkers temporarily commented out due to crashing return not caught checker
# cp -R customCheckers/* virtual/lib/python3.6/site-packages/pylint/checkers/
python3 cleanOutput.py testreturnnotcaught.py WEc
