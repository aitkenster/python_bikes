from bikecontainer import *

class Van(BikeContainer):
		def __init__(self):
				BikeContainer.__init__(self)

		def collect_bikes(self, location, status):
				if status == "punctured":
						self.get_type_bikes(self.punctured_bikes, location.punctured_bikes)
				elif status == "working":
						self.get_type_bikes(self.working_bikes, location.working_bikes)
				else:
						return "status not recognised"

		def get_type_bikes(self, type, location):
				while len(location) > 0:
						type.append(location.pop())

		def deposit_bikes(self, location, status):
				if status == "punctured":
						self.deposit_type_bikes(location.punctured_bikes, self.punctured_bikes)
				elif status == "working":
						self.deposit_type_bikes(location.working_bikes, self.working_bikes)
				else:
						return "status not recognised"

		def deposit_type_bikes(self, location, type):
				while len(type) > 0:
						location.append(type.pop())

