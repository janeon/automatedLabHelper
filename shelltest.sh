#!/bin/bash
# This bash script was made possible by:
# https://askubuntu.com/questions/1131539/make-virtualenv-and-activate-it-with-shell-script

# installing pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# installing and activating a python virtual env
python3 -m pip install virtualenv
python3 -m virtualenv virtual
source virtual/bin/activate

# installing pylint
pip3 install pylint

# adding and running our custom checkers
cp -R customCheckers/* virtual/lib/python3.6/site-packages/pylint/checkers/
python3 cleanOutput.py script.py WEc
