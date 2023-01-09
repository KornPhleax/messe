import json as JSON

class Database:
	def __init__(self, path = "./data.json"):
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