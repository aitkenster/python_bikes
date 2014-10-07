class Bike:
	def __init__(self):
		self.punctured = False

	def puncture(self):
		self.punctured = True

	def patch(self):
		self.punctured = False

