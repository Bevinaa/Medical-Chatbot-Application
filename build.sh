#!/usr/bin/env bash
# Downgrade to Python 3.10 (or 3.11) manually
sudo apt-get update
sudo apt-get install python3.10 python3.10-venv python3.10-dev -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
python3 --version

# Now install dependencies using pip3
pip3 install -r requirements.txt

# Start app
python3 app.py
