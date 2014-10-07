from bike import *

class TestBike:
		def setup_method(self, method):
				self.bike = Bike()

		def test_not_punctured_when_created(self):
		    assert self.bike.punctured == False

		def test_can_get_flat_tyre(self):
			  self.bike.puncture()
			  assert self.bike.punctured == True

		def test_can_patch_up_puncture(self):
			  self.bike.patch()
			  assert self.bike.punctured == False