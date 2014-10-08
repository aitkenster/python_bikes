import pytest
from ludibrio import *
from dockingstation import *

class TestDockingStation:

		def setup_method(self, method):
				self.bank = DockingStation()
				with Stub() as self.bike:
						self.bike.isinstance(Bike) >> True
						self.bike.punctured >> False
				with Stub() as self.punctured_bike:
						self.punctured_bike.punctured >> True
		
	
		def test_inherits_from_dockingstation(self):
				assert self.bank.capacity == 10

		def test_can_return_punctured_bikes(self):
				self.bank.working_bikes.append(self.punctured_bike)
				self.bank.working_bikes.append(self.bike)
				self.bank.get_punctured_bikes()
				assert len(self.bank.punctured_bikes) == 1
