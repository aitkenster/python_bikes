import pytest
from ludibrio import *
from van import *

class TestVan:

		def setup_method(self, method):
				self.transit = Van()
				with Stub() as self.dockingstation:
						self.dockingstation.punctured_bikes >> ["Bike1", "Bike2"]
						self.dockingstation.working_bikes >> ["Bike3", "Bike4"]

		def test_inherits_from_dockingstation(self):
				assert self.transit.capacity == 10

		def test_can_collect_punctured_bikes(self):
				self.transit.collect_bikes(self.dockingstation, "punctured")
				assert self.transit.punctured_bikes == ["Bike2", "Bike1"]

		def test_can_collect_working_bikes(self):
				self.transit.collect_bikes(self.dockingstation, "working")
				assert self.transit.working_bikes == ["Bike4", "Bike3"]

		def test_can_deposit_broken_bikes(self):
				self.transit.punctured_bikes.append("bike1")
				self.transit.deposit_bikes(self.dockingstation, "punctured")
				assert len(self.transit.punctured_bikes) == 0

		def test_can_deposit_working_bikes(self):
				self.transit.working_bikes.append("bike1")
				self.transit.deposit_bikes(self.dockingstation, "working")
				assert len(self.transit.working_bikes) == 0