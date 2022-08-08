## Flask blog application

### Setup:

#### Clone

Navigate to your project directory and clone the repo:

~~~
git clone https://github.com/Yoinezero/flask-project.git
~~~

#### If you are working on your local machine:

1. Configure virtual environment

~~~
python -m venv venv
source venv/bin/activate
~~~

2. Install dependencies

~~~
pip install -r requirements.txt
~~~

3. Create .env file with following parameters:

~~~
SECRET_KEY="secret_key"
DATABASE_URL="sql_uri"
TEST_DATABASE_URL="sql_test_uri"
~~~

### Database workflow:

If you already have migrations (database tables upgrade) you should
apply them first. You have to run following command in terminal:

~~~
flask db upgrade
~~~

To generate new migration, run this command:

~~~
flask db migrate -m "<here you can write name of migration>"
~~~

Then to apply it, run `upgrade` command once again.

If you aren't satisfied with new functionality, you can downgrade your
database to previous state with following command:

~~~
flask db downgrade
~~~

### Run application

~~~
gunicorn --bind 0.0.0.0:5000 "app:create_app()"
~~~