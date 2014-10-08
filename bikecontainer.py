from bike import *

class BikeContainer:
		def __init__(self):
			  self.capacity = 10
			  self.bikes = []
			  self.punctured_bikes = []

		def dock(self, item):
				if len(self.bikes) < self.capacity and self.check_is_bike(item) == True:
						self.bikes.append(item)
				else:
						return 'Bike station cannot dock right now'

		def undock(self, item):
				self.bikes.remove(item)

		def check_is_bike(self, item):
				if item.isinstance(Bike):
						return True
				else:
						return False