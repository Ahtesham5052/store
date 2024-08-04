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

# Check if mysql_config is available
if ! command -v mysql_config &> /dev/null
then
    echo "mysql_config not found. Setting MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS manually..."
    export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
    export MYSQLCLIENT_LDFLAGS="-L/usr/lib/mysql -lmysqlclient"
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
