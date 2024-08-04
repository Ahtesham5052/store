set -e 
gunicorn store.wsgi:application --logfile -