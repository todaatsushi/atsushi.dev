# atsushi.dev

Personal portfolio website for me - Atsushi Toda. Can be altered to become anybody's portfolio site! Built with Django, frontend CSS in UiKit.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

Using a virtual env (recommended), install dependancies from requirements.txt.

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


## Extra installation notes
The default database is sqlite3 and production is configured to MySQL.
The home page references a non existant project (at installation) named [Champ](https://champ.atsushi.dev/). Remove it to work initially.

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

* **Me, Atsushi Toda** - [GitHub](https://github.com/broadsinatlanta) - [Actual atsushi.dev site](https://www.atsushi.dev)

## License

This project is licensed under the MIT License.
