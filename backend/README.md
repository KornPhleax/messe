# Backend module
Docker Containers:
1. openldap (osixia/openldap:1.3.0)
2. phpldapadmin (osixia/phpldapadmin:0.9.0)
3. Python Flask Backend (built via Dockerfile in this repo)

## Docker Container
The Docker Containers are responsible for hosting openldap and phpldapadmin which gets use by the python Flask Backend REST API. 
The python application is hosted in its own python container built with `docker-compose up -d` 

## Python Flask Backend local setup for development
This ist the REST API implemented in Flask.
It allows for checking the health via the /health route, using the /authenticate_user endpoint a user can be authenticated via sending username and password in this json format:

`{"user":"givenname surname","password":"<password>" }`


## Development Setup
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

Now we need a virtual environment for python to install its dependencies, execute `python -m venv ./venv` now switch into it with `source ./venv/bin/activate`.

To start the flask API install all requirements in the provided file like this:
`pip install -r requirements.txt`
and start the server with `python main.py`

Good Luck!
