from django.test import TestCase, RequestFactory
from ..viewsets.viewsets import MaosPossiveisViewSet

# Create your tests here.

class MaosPossiveisTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
    
    def test_list(self):
        print('ddd')
        #request = self.factory.get('/')
        self.assertEqual('','')

