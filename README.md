# Little Lemon Restaurant Web Application

## Welcome to the Little Lemon Full Stack Web App

### Before running the server check the following:

1. Run the following commands in the terminal:
    - Change directory to the project folder using cd. (This folder will contain 'Pipfile' and 'Pipfile.lock')
    - pipenv shell or python3 pipenv shell
    - pipenv install or if error? pip install


2. Database configuration (Found: Project Level 'settings.py'):

    - CREATE A DATABASE in MySQL with the DB name you will insert below.

        - **DON't FORGET TO CHANGE THE DATABASE PASSWORD IN 'settings.py' ACCORDING TO YOUR USER AND PASSWORD in MySQL.**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : 'yourpassword',
    }
}
```
3. Then run the following (in the folder containing 'manage.py'):
    // python3 manage.py makemigrations
    // python3 manage.py showmigrations
    // python3 manage.py migrate

4. Run the server (in the folder containing 'manage.py'):
    // python3 manage.py runserver
