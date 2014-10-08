from bikecontainer import *

class DockingStation(BikeContainer):
		def __init__(self):
				BikeContainer.__init__(self)

		def get_punctured_bikes(self):
				for bike in self.bikes:
						if bike.punctured == True:
								self.punctured_bikes.append(bike)


