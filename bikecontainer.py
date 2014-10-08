from bike import *

class BikeContainer:
		def __init__(self):
			  self.capacity = 10
			  self.working_bikes = []
			  self.punctured_bikes = []

		def dock(self, item):
				if len(self.working_bikes) < self.capacity and self.check_is_bike(item) == True:
						self.working_bikes.append(item)
				else:
						return 'Bike station cannot dock right now'

		def undock(self, item):
				self.working_bikes.remove(item)

		def check_is_bike(self, item):
				if item.isinstance(Bike):
						return True
				else:
						return False