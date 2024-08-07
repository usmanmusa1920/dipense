
# DiPense

```sh
@@@@@@@   @@@  @@@@@@@   @@@@@@@@  @@@  @@@   @@@@@@   @@@@@@@@  
@@@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@   @@@@@@@@  
@@!  @@@  @@!  @@!  @@@  @@!       @@!@!@@@  !@@       @@!       
!@!  @!@  !@!  !@!  @!@  !@!       !@!!@!@!  !@!       !@!       
@!@  !@!  !!@  @!@@!@!   @!!!:!    @!@ !!@!  !!@@!!    @!!!:!    
!@!  !!!  !!!  !!@!!!    !!!!!:    !@!  !!!   !!@!!!   !!!!!:    
!!:  !!!  !!:  !!:       !!:       !!:  !!!       !:!  !!:       
:!:  !:!  :!:  :!:       :!:       :!:  !:!      !:!   :!:       
 :::: ::   ::   ::        :: ::::   ::   ::  :::: ::    :: ::::  
:: :  :   :     :        : :: ::   ::    :   :: : :    : :: :: 
```

An OSINT tool for IT ninjas

[![Downloads Month Badge](https://static.pepy.tech/badge/dipense/month)](https://pypi.org/project/dipense)
[![License Badge](https://img.shields.io/pypi/l/dipense.svg)](https://pypi.org/project/dipense)
[![Supported Wheel Badge](https://img.shields.io/pypi/wheel/dipense.svg)](https://pypi.org/project/dipense)
[![Supported Versions Badge](https://img.shields.io/pypi/pyversions/dipense.svg)](https://pypi.org/project/dipense)

## Usage:: (local)

First clone the repository

```sh
	git clone https://github.com/usmanmusa1920/dipense
```

Enter into the directory, which live in `dipense/dipense`

```sh
	cd dipense/dipense
```

Create virtual environment

```sh
	python -m venv d_venv
```

Activate virtual environment

```sh
	source d_venv/bin/activate
```

Install requirements

```sh
	pip install -r requirements.txt
```

Now run the development server by:

```sh
	python manage.py runserver
```

Visit the url address `http://localhost:8000`, use the below user credential to login!

**Email:** mr_robot@mail.com **Password:** root1234

## Usage:: (Docker release)

> **Note**
> The docker version is too old, but soon new will be release!

To use this tool you have to make sure you have `docker` install as well as `docker-compose`, also make sure you have nothing running on port `8000` and `80` because these ports are going to be use for the services

After that then you are to pull the image from docker with

```sh
	docker pull usmanmusa/dipense
```

Next you are to clone the github repo of the project in other to get the `docker-compose.yml` by:

```sh
	git clone https://github.com/usmanmusa1920/dipense.git
```

Now cd into the project folder you just clone to spin up the services using the command::

```sh
	docker-compose up
```

you can use the command below instead of the above, in other to see how it build the image::

```sh
	docker-compose up --build
```

Once that finish, you will notice in your terminal that it says you can reach it at `http://0.0.0.0:8000`, that one is a gunicorn server which doesn't serve static files, we recommend visiting it at port `80` which is an `Nginx` server that can serve static files, and it is a proxy to that gunicorn container.

## Usage:: (Pypi release)

First we recommend creating a virtual environment `python -m venv venv` and then activate it `source venv/bin/activate`

Once that finish now install the library using

```sh
	pip install --upgrade dipense
```

Wait for the installation to finish, basically the library was uploaded using `sdist` (Source Distribution)

After that, create a new file let call it `route.py` in the file put the below code

```python
	from dipense import payloads
	from dipense.structure import helper


	if __name__ == '__main__':
		payloads(helper)
```

save the file and navigate to where the file is located in terminal and your are ready to go

To find information about a domain name run the file like:

```sh
	python route.py payloadwho -d google.com
	# or
	python route.py payloadwho --domain google.com
```


To find information about an ip address run the file like so below, and the command require root previlage (super user):

```sh
	python route.py payloadip -i 198.3.11.7
	# or
	python route.py payloadip --ip 198.3.11.7
```

You can also specify a flag of `-o` or `--open` to `True` this will automatically open a webbrowser showing you where that ip address is located, like:

```sh
	python route.py payloadip -i 198.3.11.7 -o True
	# or
	python route.py payloadip -i 198.3.11.7 --open True
```


To find information about a phone number run the file like you see below, be sure to start with the country code of that phone number:

```sh
	python route.py payloadnum -n +2349083513047
	# or
	python route.py payloadnum --number +2349083513047
```


To see positional argument and flags available run the file without any flag or positional argument like:

```sh
	python route.py
```

See more documentations <a href="https://dipense.readthedocs.io">here!</a>

## Useful links

- Documentation: https://dipense.readthedocs.io
- Repository: https://github.com/usmanmusa1920/dipense
- Docker-hub Release: https://hub.docker.com/r/usmanmusa/dipense
- PYPI Release: https://pypi.org/project/flask-unity

## Build Status
- version 0.1.5

## DiPense at a glance (docker)

![DiPense at a glance](docs/_static/screen-shot.png)

## DiPense at a glance (pypi)

![DiPense at a glance](docs/_static/dipense-terminal.png)

Pull requests are welcome
