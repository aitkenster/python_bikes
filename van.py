from bikecontainer import *

class Van(BikeContainer):
		def __init__(self):
				BikeContainer.__init__(self)

		def collect_bikes(self, location, status):
				if status == "punctured":
						self.get_punctured_bikes(location)
				elif status == "working":
						self.get_working_bikes(location)
				else:
						return "status not recognised"

		def get_punctured_bikes(self, location):
				while len(location.punctured_bikes) > 0:
						self.punctured_bikes.append(location.punctured_bikes.pop())

		def get_working_bikes(self, location):
				while len(location.working_bikes) > 0:
						self.working_bikes.append(location.working_bikes.pop())

		def deposit_bikes(self, location, status):
				if status == "punctured":
						self.deposit_punctured_bikes(location)
				elif status == "working":
						self.deposit_working_bikes(location)
				else:
						return "status not recognised"

		def deposit_punctured_bikes(self, location):
				while len(self.punctured_bikes) > 0:
						location.punctured_bikes.append(self.punctured_bikes.pop())

		def deposit_working_bikes(self, location):
				while len(self.working_bikes) > 0:
							location.working_bikes.append(self.working_bikes.pop())

