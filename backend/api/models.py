#!/usr/bin/env python
# encoding: utf-8
import json as JSON

class User:
	def __init__(self, givenname, surname, address, mail, preferences, telefon = None):
		self.givenname = givenname
		self.surname = surname
		self.address = Address(address)
		self.mail = mail
		self.preferences = Preferences(preferences)
		self.telefon = telefon

	def __init__(self, json):
		obj = JSON.loads(json)
		self.givenname = obj.givenname
		self.surname = obj.surname
		self.address = obj.address
		self.mail = obj.mail
		self.preferences = obj.preferences
		self.telefon = obj.telefon

class Address:
	def __init__(self, street, number, postalcode, city):
		self.street = street
		self.number = number
		self.postalcode = postalcode
		self.city = city

	def __init__(self, json):
		obj = JSON.loads(json)
		self.street = obj.street
		self.number = obj.number
		self.postalcode = obj.postalcode
		self.city = obj.city

class Preferences:
	def __init__(self, camera, tv, smartphone, printer, monitor, notebook):
		self.camera = camera
		self.tv = tv
		self.smartphone = smartphone
		self.printer = printer
		self.monitor = monitor
		self.notebook = notebook

	def __init__(self, json):
		obj = JSON.loads(json)
		self.camera = obj.camera
		self.tv = obj.tv
		self.smartphone = obj.smartphone
		self.printer = obj.printer
		self.monitor = obj.monitor
		self.notebook = obj.notebook

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