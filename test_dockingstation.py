from dockingstation import *

class TestDockingStation:

		def setup_method(self, method):
				self.bank = DockingStation()


		def test_initialized_with_default_capacity(self):
				assert self.bank.capacity == 10

		def test_no_bikes_when_created(self):
				assert len(self.bank.bikes) == 0
