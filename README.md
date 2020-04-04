# UserActivity

- This powers https://morning-scrubland-98506.herokuapp.com/

## Local installation steps:

- Clone the Repo.
- Execute all below commands in the root folder(manage.py location).
- Install pipenv from pip `pip install pipenv`.
- Install dependencies `pipenv install`.
- Activate virtualenv by doing `pipenv shell`.
- Do initial migrations `./manage.py migrate`.
- Dump dummy data `./manage.py dump_user_activity 100` where 100 is the number dummy users. we can chage accordingly.
- Run the server `./manage.py runserver`.
- Go the home route where api is being served.
