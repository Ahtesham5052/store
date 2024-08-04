#!/bin/bash

# Install Python 3.11 without sudo if not already installed
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 not found. Installing..."
    # Installing pyenv to manage Python versions
    curl https://pyenv.run | bash
    export PATH="$HOME/.pyenv/bin:$HOME/.pyenv/shims:$HOME/.pyenv/versions"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    pyenv install 3.11.0
    pyenv global 3.11.0
fi

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python3.11 manage.py migrate

# Collect static files
python3.11 manage.py collectstatic --no-input
