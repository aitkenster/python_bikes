import pytest
from van import *
from ludibrio import *

class TestVan:

		def setup_method(self, method):
				self.transit = Van()
				with Stub() as self.dockingstation:
						self.dockingstation.punctured_bikes >> ["Bike1", "Bike2"]

		def test_inherits_from_dockingstation(self):
				assert self.transit.capacity == 10

		# def test_can_collect_bikes(self):
		# 		self.transit.collect_bikes(self.dockingstation, "punctured")
		# 		assert self.transit.punctured_bikes == ["Bike1", "Bike2"]