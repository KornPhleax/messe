#!/usr/bin/env python
# encoding: utf-8
import json as JSON

class User:
	def __init__(self, givenname, surname, address, mail, preferences, telefon = None):
		self.givenname = givenname
		self.surname = surname
		self.address = address
		self.mail = mail
		self.preferences = preferences
		self.telefon = telefon

	def __init__(self, json):
		obj = JSON.loads(json)
		self.givenname = obj.givenname
		self.surname = obj.surname
		self.address = obj.address
		self.mail = obj.mail
		self.preferences = obj.preferences
		self.telefon = obj.telefon

# Example JSON:
'''
{
  "givenname": "Max",
  "surname": "Mustermann",
  "address": {
    "street": "Musterstr.",
    "number": "1",
    "postalcode": "77777",
    "city": "Musterstadt"
  },
  "mail": "max@mustermann.de",
  "preferences": {
    "camera": false,
    "tv": false,
    "smartphone": false,
    "printer": false,
    "monitor": false,
    "notebook": false
  },
  "telefon": null
}
'''