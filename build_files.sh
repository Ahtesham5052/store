#!/bin/bash

# Install Python 3.11 if it's not available
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 not found, installing..."
    sudo apt-get update
    sudo apt-get install python3.11 python3.11-venv python3.11-dev -y
fi

# Create a virtual environment
python3.11 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput
