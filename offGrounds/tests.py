from django.test import TestCase

# run this command: py manage.py test


# Create your tests here.
class DummyTests(TestCase):

    def test_first_dummy(self):
        """
        This is a dummy test case
        """
        self.assertIs(True, True)
