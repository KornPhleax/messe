#!/usr/bin/env python
# encoding: utf-8
import json as JSON
from flask import Flask, redirect, request
from app.ldap import LDAP
import os

LDAP_URL = os.environ['LDAP_URL']
LDAP_BASE_DN = os.environ['LDAP_BASE_DN']
LDAP_BIND_USER = os.environ['LDAP_BIND_USER']
LDAP_BIND_PW = os.environ['LDAP_BIND_PW']


ldap = LDAP(f"ldap://{LDAP_URL}:389", LDAP_BASE_DN, LDAP_BIND_USER, LDAP_BIND_PW)
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
        return JSON.dumps(
            {
            	"result": status,
                "ldap_result": str(result)
            }
        )
    else:
        return "Content-Type not supported!"

if __name__ == "__main__":
    app.run()
