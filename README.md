# Tech Challenge

## Dependencies

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Tools

* [Direnv](https://direnv.net/)
* [Portainer](https://www.portainer.io/)
* [Pyenv](https://github.com/pyenv/pyenv)
* [pyenv-installer](https://github.com/pyenv/pyenv-installer)

## Running Services

Create and start containers. Option `-d` Detached mode: Run containers in the background.

```bash
docker-compose up -d
```

## Services

* Postgres running on port `5432`
* Pgadmin4 web-client for postgres. Running on port `8080`. [http://localhost:8080](http://localhost:8080)

### Postgres

| host      | port | user          | password      | database      |
|-----------|------|---------------|---------------|---------------|
| localhost | 5432 | tech-challenge | tech-challenge | tech_challenge |

### Pgadmin4

| host      | port | email                   | password      |
|-----------|------|-------------------------|---------------|
| localhost | 8080 | tech-challenge@email.com | tech-challenge |

### Portainer

Install portainer local

```bash
docker run --name portainer --restart=unless-stopped -d \
    -p 8000:8000 -p 9000:9000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/portainer_data:/data portainer/portainer
```

## Running scripts local

### Create a virtualenv

```bash
python -m venv .venv ; source .venv/bin/activate.fish
```

### Install and Update packages

```bash
pip install -U pip setuptools ; pip install -r requirements.txt ; pip install -r requirements-dev.txt
```

### Execute script

```bash
python tech_challenge/app.py
```
