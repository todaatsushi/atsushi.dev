# atsushi.dev

Personal portfolio website for me - Atsushi Toda. Can be altered to become anybody's portfolio site! Built with Django, frontend CSS in UiKit.

## Project links
* [atsushi.dev](https://www.atsushi.dev) - link to the site
* [Project page](https://www.atsushi.dev/work/atsushidev/) on atsushi.dev - link to more information on the project page on my site

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

Using a virtual env (recommended), install dependencies from requirements.txt.

```
pip install -r requirements.txt
```
Then, just migrate the databases and you're good to go.
```
python manage.py migrate
```
Optional:
```
python manage.py createsuperuser
```

to use admin functionalities e.g. create projects.

## .env variables
atsushi.dev expects the following variables:

### Django
* SECRET_KEY - Django secret key
* DEBUG - Debug settings ('True' for debug mode)

### Personal
* EMAIL_ADDRESS
* EMAIL_PASSWORD
* LOCAL_HOST - localhost name

### Database - Production only
* DB_NAME - MySQL database name
* DB_USER
* DB_PASSWORD
* DB_HOST
* DB_TEST_DB - Name of the test database used


## Extra installation notes
* The default database is sqlite3 and production is configured to MySQL.
* *MySQL is hosted and configured on PythonAnywhere - settings may need refactoring depending on where it is hosted*
* The home page references a non existant project (at installation) named [Champ](https://champ.atsushi.dev/). Remove it to work initially.
* ***atsushi.dev expects a Gmail address***

## Running the tests

Unit tests are written for every app's models and forms.

To run everything:
```
python manage.py test
```

## Deployment

To serve static files make sure [Whitenoise](http://whitenoise.evans.io/en/stable/django.html) is configured properly and run
```
python manage.py collectstatic
```

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [UiKit](https://getuikit.com/docs/introduction) - CSS / JavaScript Framework

## Authors

* **Me, Atsushi Toda** - [GitHub](https://github.com/todaatsushi) - [Personal site](https://www.atsushi.dev)

## License

This project is licensed under the MIT License.
