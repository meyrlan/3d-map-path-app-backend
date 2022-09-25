# Hacknu 3D App Django Backend

### Generic Info:
* The app is dedicated to visualize historical data, which is parsed from input Excel file.
* Useful for people to track their paths and services to locate a target.
* Demonstration of the app: [Video link](https://drive.google.com/file/d/1wlTeC7tHH44Bf_GIy4AroO4qx5PucNUU/view?usp=sharing)

### Technical Info:
* Backend - Django (Python)
* [Frontend](https://github.com/meyrlan/hacknu-2022-frontend) - ThreeJS (JavaScript), HTML, CSS, Bootstrap
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

![image](https://user-images.githubusercontent.com/45965276/192124610-ed15ceb0-893b-4630-a885-5b05d6fa4cc0.png)
