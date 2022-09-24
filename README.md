# Eventter Django Backend

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

## Quick Start

**NOTE**: The project uses Python 3.7, so need it installed first. It is recommended to use `pyenv` for installation.

Here is a short instruction on how to quickly set up the project for development:

1. [Install `poetry`](https://python-poetry.org/docs/#installation)
2. `git clone --recurse-submodules git@gitlab.com:go-kid/web-server.git`
3. Install requirements:

```bash
$ poetry install
$ poetry shell
```

---

4. Install pre-commit hooks: `$ pre-commit install`
5. Initiate the database: `$ cd www && python manage.py migrate`
6. Run `$ python manage.py fill_dev_db` This will create a superuser (username and password are "admin"), load fixtures and fill the database with testing data. **NOTE**: By default, all database tables will be truncated. See `$ python manage.py fill_dev_db --help` for details.
   OR
   Manually create a superuser:

```bash
$ python manage.py createsuperuser --username admin --email admin@admin.com
```

7. Generate translations by running `$ python manage.py compilemessages`. In order to do that you need to have GNU gettext utility installed. On OSX it is done via `brew install gettext`.
8. Run the server: `$ python manage.py runserver`

## How to run with PostgreSQL in Development

> In the root git directory

1. Create or update `.env` file.

```bash
$ cat << EOT >> .env
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=django
SQL_PASSWORD=postgres
SQL_HOST=localhost
SQL_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=django
POSTGRES_PASSWORD=postgres
EOT
```

2. Deactivate current `poetry shell` environment if it was already activated and activate it again with additional environment variables. We use `DJANGO_READ_DOT_ENV_FILE=True` before the command to add environment variables to `Django` settings from the `.env` file:

```bash
$ exit
$ DJANGO_READ_DOT_ENV_FILE=True poetry shell
```

3. Install `psycopg2` package. **NOTE:** Avoid installing by `poetry add` because it will update `pyproject.toml` and `poetry.lock`.

```bash
$ pip install 'psycopg2>=2.8.4,<3.0'
```

4. Run the `PostgreSQL` database in `Docker` container

```bash
docker run --rm --name pg --env-file .env -d -p 5432:5432 postgres:12.5-alpine
```

5. If you have a dump of the real DB you can use the following command to restore data.

```bash
docker cp <name-of-dump-file> pg:/tmp/dump.sql
docker exec pg pg_restore -U django -d postgres /tmp/dump.sql
```

6. Do what you need

```bash
cd www
python manage.py <command>
# Create a superuser, for example.
python manage.py createsuperuser --username admin
```

7. When finished

```bash
docker stop pg # To stop the Postgres database
cd .. # To return to the `server-py` directory
rm .env # Remove .env file
exit # Deactivate and activate the `virtualenv` environment again
poetry shell # To switch back to SQLite
```
