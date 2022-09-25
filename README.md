# Hacknu 3D App Django Backend

### Generic Info:
* The app is dedicated to visualize historical data, which is parsed from input Excel file.
* Useful for people to track their paths and services to locate a target.

### Technical Info:
* Backend - Django
* Frontend - ThreeJS, HTML, CSS, JavaScript
* Algorithms - Path Interpolation Algorithm

### Quick Start

1. [Install `poetry`](https://python-poetry.org/docs/#installation)
2. Install requirements:

```bash
$ poetry install
$ poetry shell
```

3. Migrations - go to www folder and: 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

4. Run server:

```bash
$ python manage.py runserver
```
