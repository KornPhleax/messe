# Backend module
Docker Containers:
1. openldap (osixia/openldap:1.3.0)
2. phpldapadmin (osixia/phpldapadmin:0.9.0)
3. redis (redis:6.2-alpine)
4. Python Flask Backend (built via Dockerfile in this repo)

## Docker Containers
The Docker Containers are responsible for hosting redis, openldap and phpldapadmin which gets use by the python Flask Backend REST API. 
The python application is hosted in its own python container built with `docker-compose up -d --build` 

## Python Flask Backend
This is the REST API implemented in Flask.
It allows for checking the health via the /health route, using the /authenticate_user endpoint a user can be authenticated via sending username (first letter of givenname and complete surname) and password in this json format:

`{"user":"<username>","password":"<password>" }`


## Installation
You need:
- docker installed 
- python installed
- internet connection - lol

Execute the provided `docker-compose.yml` via `docker-compose up -d` to start openldap, phpldapadmin and the backend. 
It should be reachable at 

`http://localhost:8080`,

phpldapadmin is reachable at

`https://localhost:8081` **HTTPS!**

you should be able to login with the default credentials:

`cn=admin,dc=ffh,dc=de`

`admin`

There you could import your previously saved backup or create new groups and users.

### Development Setup

We need a virtual environment for python to install its dependencies, execute `python -m venv ./venv` now switch into it with `source ./venv/bin/activate`.

To start the flask API install all requirements in the provided file like this:

`pip install -r requirements.txt`

and export all needed environment vars:

`export LDAP_URL=localhost && export LDAP_BASE_DN=dc=ffh,dc=de && export LDAP_BIND_USER=admin && export LDAP_BIND_PW=admin && export REDIS_URL=localhost && export REDIS_PORT=6379 && export REDIS_PW=3ec7kJVE76jEVDVtjdyJVtyvJDty`

and start the server with `python -m api.wsgi`

Good Luck!
