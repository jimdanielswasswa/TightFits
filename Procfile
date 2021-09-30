release: pip install -r requirements.txt
release: python3 urbanshop/manage.py migrate
web: gunicorn urbanshop/urbanshop.wsgi --log-file -