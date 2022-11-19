#!/usr/bin/env python
# encoding: utf-8
import json as JSON
from flask import Flask, redirect, request
from api.ldap import LDAP
from api.redis_session import Redis 
import os

LDAP_URL = os.environ['LDAP_URL']
LDAP_BASE_DN = os.environ['LDAP_BASE_DN']
LDAP_BIND_USER = os.environ['LDAP_BIND_USER']
LDAP_BIND_PW = os.environ['LDAP_BIND_PW']

REDIS_URL = os.environ['REDIS_URL']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_PW = os.environ['REDIS_PW']


ldap = LDAP(f"ldap://{LDAP_URL}:389", LDAP_BASE_DN, LDAP_BIND_USER, LDAP_BIND_PW)
redis = Redis(REDIS_URL, REDIS_PORT, REDIS_PW, ttl = 30, length = 20)
app = Flask(__name__)


@app.route("/")
def index():
    return JSON.dumps({"api": "working :)"})


@app.route("/health")
def health():
    return JSON.dumps({"result": str(ldap.health())})


@app.route("/authenticate_user", methods=["POST"])
def authenticate_user():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        json = request.json
        status, result = ldap.authenticate_user(json["user"], json["password"])
        token = redis.create_session(json['user']) if status else None
        return JSON.dumps(
            {
            	"result": status,
                "ldap_result": str(result),
                "token": token,
                "ttl": redis.ttl
            }
        )
    else:
        return "Content-Type not supported!"

if __name__ == "__main__":
    app.run()
