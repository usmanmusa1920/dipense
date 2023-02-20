
DiPense
=======

An OSINT tool lab for IT ninjas

How to
======

To use this tool you have to make sure you have `docker` install as well as `docker-compose`, also make sure you have nothing running on port `8000` and `80` because these ports are going to be use for the services

After that then you are to pull the image from docker with
**docker pull usmanmusa/dipense**

Next you are to clone the github repo of the project
**git clone https://github.com/usmanmusa1920/dipense.git**
in other to get the
**docker-compose.yml**

After that cd into the project folder you just clone to spin up the services using
**docker-compose up**, you can use **docker-compose up --build** in other to see how it build the image

Once that finish, you will notice in your terminal that it says you can reach it at
**http://0.0.0.0:8000**,
that one is a gunicorn server which doesn't serve static files,
we recommend visiting it at port
**80**
which is an
**Nginx**
server that can serve static files, and it is a proxy to that gunicorn container

Officially site at:
===================

- https://dipense.readthedocs.io/en/latest/

Docker hub repo at:
===================

- https://hub.docker.com/r/usmanmusa/dipense

Build Status
============

- version 0.1

DiPense at a glance
===================

.. image:: screen-shot.png
  :width: 400
  :alt: Alternative text