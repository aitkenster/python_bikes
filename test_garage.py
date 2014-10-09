import pytest
from ludibrio import *
from garage import *

class TestGarage:

		def setup_method(self, method):
				self.halfords = Garage()
				with Stub() as self.punctured_bike:
						self.punctured_bike.patch()
		def test_inherits_from_bike_container(self):
				assert self.halfords.capacity == 10

		def test_can_fix_all_punctured_bikes(self):
				self.halfords.punctured_bikes.append(self.punctured_bike)
				self.halfords.patch_punctured_bikes()
				assert len(self.halfords.punctured_bikes) == 0
				assert len(self.halfords.working_bikes) == 1