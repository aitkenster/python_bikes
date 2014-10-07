from bike import *

class TestBike:
		def setup_method(self, method):
				self.bike = Bike()

		def test_not_broken_when_created(self):
		    assert self.bike.broken == False