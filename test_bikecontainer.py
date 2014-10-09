import pytest
from ludibrio import *
from bikecontainer import *

class TestDockingStation:

		def setup_method(self, method):
				self.box = BikeContainer()
				with Stub() as self.bike:
						self.bike.isinstance(Bike) >> True
						self.bike.punctured >> False
				with Stub() as self.punctured_bike:
						self.punctured_bike.isinstance(Bike) >> True
						self.punctured_bike.punctured >> True
				with Stub() as self.chicken:
						self.chicken.isinstance(Bike) >> False

		def fill_station(self, station):
				for i in range(0,station.capacity):
						station.dock(self.bike)

		def test_initialized_with_default_capacity(self):
				assert self.box.capacity == 10

		def test_no_bikes_when_created(self):
				assert len(self.box.working_bikes) == 0
				assert len(self.box.punctured_bikes) == 0

		def test_can_dock_a_working_bike(self):
				self.box.dock(self.bike)
				assert len(self.box.working_bikes) == 1

		def test_can_dock_a_punctured_bike(self):
		 		self.box.dock(self.punctured_bike)

		def test_can_undock_a_bike(self):
			  self.box.working_bikes.append(self.bike)
			  self.box.undock(self.bike)
			  assert len(self.box.working_bikes) == 0

		def test_knows_how_many_bikes_are_docked(self):
				self.box.working_bikes.append(self.bike)
				self.box.punctured_bikes.append(self.punctured_bike)
				assert self.box.total_bikes_docked() == 2

		def test_knows_item_is_not_a_bike(self):
				assert self.box.check_is_bike(self.chicken) == False

		def test_knows_item_is_a_bike(self):
				assert self.box.check_is_bike(self.bike) == True

		def test_cannot_dock_bike_if_station_full(self):
			  self.fill_station(self.box)
			  assert self.box.dock(self.bike) == 'Bike station cannot dock right now'
			  assert len(self.box.working_bikes) == 10