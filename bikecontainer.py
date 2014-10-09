from bike import *

class BikeContainer:
		def __init__(self):
			  self.capacity = 10
			  self.working_bikes = []
			  self.punctured_bikes = []

		def dock(self, item):
				if self.bike_is_dockable(item):
						self.add_to_working_or_punctured_list(item)
				else:
						return 'Bike station cannot dock right now'

		def undock(self, item):
				self.working_bikes.remove(item)

		def check_is_bike(self, item):
				if item.isinstance(Bike):
						return True
				else:
						return False

		def total_bikes_docked(self):
				return len(self.working_bikes) + len(self.punctured_bikes)

		def bike_is_dockable(self, item):
				return self.total_bikes_docked() < self.capacity and self.check_is_bike(item)

		def add_to_working_or_punctured_list(self, item):
				if item.punctured == False:
						self.working_bikes.append(item)
				else:
						self.punctured_bikes.append(item)
