release: python ./manage.py migrate
release: python ./manage.py dump_user_activity 100
web: gunicorn app.wsgi:application --preload --workers 1