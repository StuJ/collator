from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_node_and_retrieve_it_later(self):

        # Homepage is loaded
        self.browser.get('http://localhost:8000')

        self.assertIn('Collator', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Collator', header_text)
        body_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Organise', body_text)

        # Add node interface is present
        inputbox = self.browser.find_element_by_id('id_new_node')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Add a new node...')

        # Can add a new node and it appears on the list on the homepage
        inputbox.send_keys('Museums')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        nodes = self.browser.find_elements_by_class_name('homepage_node')
        self.assertTrue(
            any(node.text == 'Museums' for node in nodes)
        )
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

