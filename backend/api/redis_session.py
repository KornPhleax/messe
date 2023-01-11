#!/usr/bin/env python
# encoding: utf-8
import secrets
import redis
import json as JSON
import time


'''
connects to redis database.
'''
class Redis:
	def __init__(self, host, port, password, ttl = 30, length = 20):
		self.redis_db = redis.Redis(
    		host=host,
    		port=port,
    		password=password)
		self.ttl = ttl
		self.length = length

	'''
	creates a token for verification as the given user
	'''
	def create_session(self, username):
		token_url, token = Token.create(username, self.ttl, self.length)
		self.redis_db.set(token_url, token)
		return token_url

	'''
	verifies a token
	'''
	def verify_session(self, token_url):
		redis_obj = self.redis_db.get(token_url)
		token = JSON.loads(redis_obj) if redis_obj is not None else None
		return token if token is not None and token['ts_expired'] > time.time() else False

	'''
	delete token 
	'''
	def delete_session(self, token_url):
		redis_obj = self.redis_db.get(token_url)
		if redis_obj is not None:
			self.redis_db.delete(token_url)
		else:
			return False
		return True

'''
Token helper class, creates json object with token information inside to store token expire timestamp
'''
class Token:
	def create(username, ttl = 30, length = 20):
		token_url =  secrets.token_urlsafe(length)
		return token_url, JSON.dumps({"user": username, "ts_created": time.time(), "ts_expired": time.time() + (ttl * 60)})