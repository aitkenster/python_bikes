import pytest
from ludibrio import *
from dockingstation import *

class TestDockingStation:

		def setup_method(self, method):
				self.bank = DockingStation()
				with Stub() as self.bike:
						self.bike.isinstance(Bike) >> True
				with Stub() as self.chicken:
						self.chicken.isinstance(Bike) >> False
				with Stub() as self.punctured_bike:
						self.punctured_bike.punctured >> True

		def fill_station(self, station):
				for i in range(0,station.capacity):
						station.dock(self.bike)

		def test_initialized_with_default_capacity(self):
				assert self.bank.capacity == 10

		def test_no_bikes_when_created(self):
				assert len(self.bank.bikes) == 0

		def test_can_dock_a_bike(self):
				self.bank.dock(self.bike)
				assert len(self.bank.bikes) == 1

		def test_can_undock_a_bike(self):
			  self.bank.dock(self.bike)
			  self.bank.undock(self.bike)
			  assert len(self.bank.bikes) == 0

		def test_knows_item_is_not_a_bike(self):
				assert self.bank.check_is_bike(self.chicken) == False

		def test_knows_item_is_a_bike(self):
				assert self.bank.check_is_bike(self.bike) == True

		def test_cannot_dock_bike_if_station_full(self):
			  self.fill_station(self.bank)
			  assert self.bank.dock(self.bike) == 'Bike station cannot dock right now'
			  assert len(self.bank.bikes) == 10

		def test_can_return_punctured_bikes(self):
				self.bank.bikes.append(self.punctured_bike)
				self.bank.get_punctured_bikes()
				assert len(self.bank.punctured_bikes) == 1
