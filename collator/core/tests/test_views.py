
from test_plus.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'node_name': 'New node name'})
        self.assertIn('New node name', response.content.decode())
        self.assertTemplateUsed(response, 'core/home.html')
