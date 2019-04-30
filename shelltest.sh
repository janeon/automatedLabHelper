#!/bin/bash
python3 -m pip install virtualenv
python3 -m virtualenv virtual
source virtual/bin/activate
pip3 install pylint
python cleanOutput.py script.py WEc
