from lager.tests import *

class TestChadController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='chad', action='index'))
        # Test response...
