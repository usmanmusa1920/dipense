
# DiPense

An OSINT tool lab for IT ninjas

# How me DiPense
To use this tool you have to make sure you have `docker` install as well as `docker-compose`, also make sure you have nothing running on port `8000` and `80` because these ports are going to be use for the services

After that then you are to pull the image from docker with

```
docker pull usmanmusa/dipense
```

Next you are to clone the github repo of the project in other to get the `docker-compose.yml` by:

`git clone https://github.com/usmanmusa1920/dipense.git`

After that cd into the project folder you just clone to spin up the services using `docker-compose up`, you can use `docker-compose up --build` in other to see how it build the image

Once that finish, you will notice in your terminal that it says you can reach it at `http://0.0.0.0:8000`, that one is a gunicorn server which doesn't serve static files, we recommend visiting it at port `80` which is an `Nginx` server that can serve static files, and it is a proxy to that gunicorn container.

See more documentations <a href="https://dipense.readthedocs.io">here!</a>

## Useful links

- Documentation: https://dipense.readthedocs.io
- PYPI Release: https://pypi.org/project/sakyum
- Docker-hub Release: https://hub.docker.com/r/usmanmusa/dipense

Pull requests are welcome


## Build Status
- version 0.1

## DiPense at a glance

![DiPense at a glance](docs/screen-shot.png)
