#!/usr/bin/env python
# encoding: utf-8
import json as JSON

'''
this file contains the "database" implementation.
it saves a list of contacts as json on disk.
for fast caching and lesser reads it only reads 
once on startup and caches the users. 
on every new user all data gets written to the disk.
'''
class Database:
	def __init__(self, path = "./data/data.json"):
		self.path = path
		try:
			with open(self.path, 'r') as file:
				self.cache = JSON.load(file)
		except:
			self.cache = []

	def add_item(self, user):
		self.cache.append(user)
		with open(self.path, "w") as file:
			file.write(JSON.dumps(self.cache))

	def get_all_items(self):
		return self.cache