from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # Unfinished (also is this in the right place?)
    def test_can_create_node_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('Collator', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
