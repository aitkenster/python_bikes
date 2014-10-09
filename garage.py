from bikecontainer import *

class Garage(BikeContainer):

		def __init__(self):
				BikeContainer.__init__(self)

		def patch_punctured_bikes(self):
				while len(self.punctured_bikes) > 0:
					bike = self.punctured_bikes.pop()
					self.working_bikes.append(bike.patch())