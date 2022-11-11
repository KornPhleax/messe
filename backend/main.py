#!/usr/bin/env python
# encoding: utf-8
import json as JSON
from flask import Flask, redirect, request
from ldap import LDAP


ldap = LDAP("ldap://127.0.0.1:389", "dc=ffh,dc=de")
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


app.run()
