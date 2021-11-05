#!/bin/bash

sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

export DATABASE_URI secretkey

python3 create.py
python3 main.py
