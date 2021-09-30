release: pip install -r requirements.txt
release: python3 urbanshop/manage.py migrate
web: gunicorn python3 urbanshop/manage.py runserver --log-file -