echo "BUILD START"
python3.11.0rc1 -m pip install -r requirements.txt
python3.11.0rc1 manage.py collectstatic --noinput --clear
echo "BUILD END"