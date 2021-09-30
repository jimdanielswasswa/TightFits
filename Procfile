release: pip install -r requirements.txt
release: python3 manage.py migrate
web: gunicorn urbanshop.wsgi --log-file -