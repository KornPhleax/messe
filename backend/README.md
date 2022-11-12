# Backend module
1. Docker Container
2. Python Flask Backend

## Docker Container
The Docker Container is responsible for hosting openldap and phpldapadmin, this is used by the python Flask Backend REST API. 
The python application is hosted in its own python container built on `docker-compose up -d` 

## Python Flask Backend local setup for development
This ist the REST API implemented in Flask.
Currently it only allows for checking the health via the /health route, intended for docker healthchecks.
Using the /authenticate_user endpoint a user can be authenticated via sending username and password in this json format:
`{"user":"givenname surname","password":"<password>" }`


## Development Setup
You need:
- docker installed 
- python installed
- internet connection - lol

Execute the provided `docker-compose.yml` via `docker-compose up -d` to start openldap and phpldapadmin. 
It should be reachable at `https://localhost:8080` only via **HTTPS!**
you should be able to login with the default credentials:
`cn=admin,dc=ffh,dc=de`
`admin`
There you could import your previously saved backup or create new groups and users.

Now we need a virtual environment for python to install its dependencies, execute `python -m venv ./venv` now switch into it with `source ./venv/bin/activate`.

To start the flask API install all requirements in the provided file like this:
`pip install -r requirements.txt`
and start the server with `python main.py`

Good Luck!
