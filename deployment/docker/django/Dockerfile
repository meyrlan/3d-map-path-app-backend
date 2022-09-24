FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install some useful ubuntu utilitites
RUN apt-get update && apt-get install -y --no-install-recommends \
  netcat gettext wait-for-it

# Copy only project dependency files to speed up the process of creating a dockerfile
# by using docker layers caching.
COPY pyproject.toml poetry.lock /code/
WORKDIR /code

# Install website dependencies
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry self update 1.0.10
RUN poetry install --no-dev -E prod

# Copy the whole code
COPY . /code

# In case we forgot to initialize or update the submodules
RUN git submodule update --init --recursive

WORKDIR /code/www
# Set up entrypoint for the container
ENTRYPOINT ["/code/deployment/docker/django/entrypoint.sh"]
