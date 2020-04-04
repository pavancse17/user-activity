release: python ./manage.py migrate
web: gunicorn app.wsgi:application --preload --workers 1