import secrets
import redis
import json as json 
import time

class Redis:
	def __init__(self, host, port, password, ttl = 30, length = 20):
		self.redis_db = redis.Redis(
    		host=host,
    		port=port,
    		password=password)
		self.ttl = ttl
		self.length = length

	def create_session(self, username):
		token_url, token = Token.create_token(username, self.ttl, self.length)
		self.redis_db.set(token_url, token)
		return token_url, self.ttl

	def verify_session(self, token_url):
		token = self.redis_db.get(token_url)
		return token if token is not None and token['ts_expired'] > time.time() else False

class Token:
	def create_token(username, ttl = 30, length = 20):
		token_url =  secrets.token_urlsafe(length)
		return token_url, json.dumps({"user": username, "ts_created": time.time(), "ts_expired": time.time() + (ttl * 60)})