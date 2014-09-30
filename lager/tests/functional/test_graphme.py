from lager.tests import *

class TestGraphmeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='graphme', action='index'))
        # Test response...
