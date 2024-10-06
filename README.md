# Little Lemon Restaurant Web Application

## Welcome to the Little Lemon Full Stack Web App

This is a Web Application and REST API built for the Little Lemon Restaurant.

---

**Note:** This project contains two separate applications, one for the GUI(restaurant) and one for the API(restaurantAPI).

---

### Technologies:
1. Python
2. Django
3. DRF (Django Rest Framework)
4. HTML
5. CSS
6. JavaScript
7. MySQL

---

### Before running the server, check the following:

1. Run the following commands in the terminal:
    - Change directory to the project folder using cd.
      (**Note:** folder will contain 'Pipfile' and 'Pipfile.lock') 
        - for example `cd Little_Lemon/LittleLemon`
    - `pipenv shell` or `python3 pipenv shell`
    - `pipenv install` or if error? `pip install`
---

2. Database configuration (**Found:** Inside Project Level 'settings.py'):

    - CREATE A DATABASE in MySQL with the DataBase name you will insert below.

    - **CHANGE THE DATABASE USER AND PASSWORD IN '*settings.py*' ACCORDING TO YOUR USER AND PASSWORD in MySQL.**

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
---
**Note:** If you add menu data properly (after running server properly), you  will dynamically load static files in the menu page.
---

3. Then run the following (in the folder containing 'manage.py'):
    - ` python3 manage.py makemigrations `
    - ` python3 manage.py showmigrations `
    - ` python3 manage.py migrate `
---

4. Run the server (in the folder containing 'manage.py'):
    - ` python3 manage.py runserver `
---

### Links (WHILE SERVER IS RUNNING):
#### GUI
- Home `http://127.0.0.1:8000/`
- About `http://127.0.0.1:8000/about/`
- Menu`http://127.0.0.1:8000/menu/<pk>`
- Book `http://127.0.0.1:8000/book/`
- Reservations `http://127.0.0.1:8000/reservations/`

#### API
- All Menu `http://127.0.0.1:8000/api/menu` or `http://127.0.0.1:8000/api/menu-items`
- Single Menu `http://127.0.0.1:8000/api/menu/1` or `http://127.0.0.1:8000/api/menu-items/1`
- Booking `http://127.0.0.1:8000/api/booking/tables/` or `http://127.0.0.1:8000/restaurant/booking/tables/`
- Auth Token Gen (only POST) `http://127.0.0.1:8000/api/api-token-auth/`
- Users `http://127.0.0.1:8000/auth/users/`
- Token Login `http://127.0.0.1:8000/auth/token/login`
- Token Logout `http://127.0.0.1:8000/auth/token/logout`
---
