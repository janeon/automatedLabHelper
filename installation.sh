#!/bin/bash
# This bash script was made possible by:
# https://askubuntu.com/questions/1131539/make-virtualenv-and-activate-it-with-shell-script

# installing pip
# commented out because it turns out that lab machines require admin access to install pip3
# curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py 1> /dev/null



# installing and activating a python virtual env
# python3 -m pip install virtualenv 1> /dev/null


# https://stackoverflow.com/questions/14967032/error-when-installing-python-settuptools-no-such-file-or-directory-usr-loca

# deactivate 1> /dev/null
virtualenv -p python3 virtual 1> /dev/null
source virtual/bin/activate 1> /dev/null
#
# # installing pylint
pip3 install pylint 1> /dev/null

# adding and running our custom checkers
# custom checkers temporarily commented out due to crashing return not caught checker
# figure out what version of python is in the current environment and insert into following command
# var=$(echo python --version)
# echo var

cp -R checkers/* virtual/lib/python3.5/site-packages/pylint/checkers/
python3 cleanOutput.py testreturnnotcaught.py WEc
