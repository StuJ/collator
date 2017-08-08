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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Collator', header_text)
        body_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Organise', body_text)

if __name__ == '__main__':
    unittest.main(warnings='ignore')

