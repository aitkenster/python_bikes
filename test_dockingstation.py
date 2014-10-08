import pytest
from ludibrio import *
from dockingstation import *

class Chicken:
		 def squawk():
		 		return "squawk"

class TestDockingStation:

		def setup_method(self, method):
				self.bank = DockingStation()
				with Mock() as self.chicken:
						self.chicken = Chicken()
				with Mock() as self.bike:
						self.bike = Bike()

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
				with Stub() as self.chicken:
						self.chicken.isinstance(Bike) >> False
				assert self.bank.check_item(self.chicken) == False

		def test_knows_item_is_a_bike(self):
				with Stub() as self.bike:
						self.bike.isinstance(Bike) >> True
				assert self.bank.check_item(self.bike) == True

		def test_cannot_dock_bike_if_station_full(self):
			  self.fill_station(self.bank)
			  assert self.bank.dock(self.bike) == 'Bike station full'
			  assert len(self.bank.bikes) == 10
