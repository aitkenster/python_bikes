from bike import *

class DockingStation:
		def __init__(self):
			  self.capacity = 10
			  self.bikes = []

		def dock(self, item):
				if len(self.bikes) < self.capacity:
						self.bikes.append(item)
				else:
						return 'Bike station full'

		def undock(self, item):
				self.bikes.remove(item)

		def check_item(self, item):
				if item.isinstance(Bike):
						return True
				else:
						return False

