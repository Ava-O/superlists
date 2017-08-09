from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #user checks browser
        self.browser.get('http://localhost:8000')

        #user sees To-Do in browser title
        self.assertIn('To-Do', self.browser.title)

        #user sees mention of To-Do lists on page
        header_text = self.browser.get_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #text prompting the user to enter a to do item is displayed along with the input space to insert it
        inputbox = self.browser.get_element_by_id('id_new_item')
        self.assertIn(inputbox.get_attribute('placeholder'),
                      'Enter a to do item')

        #register input 'Buy vodka' in inputbox
        inputbox.send_keys('Buy vodka, make party')

        #user hits enter
        inputbox.send_keys(Keys.ENTER)

        #input will be saved in a to do list table that we retrieve
        #and display in browser for the user to see
        #but not before waiting a second for the browser to load after the refresh started when hitting ENTER
        time.sleep(1)
        table = self.browser.gfind_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(rows.text == '1: Buy vodka, make party' for row in rows)
        )

        #test not finished yet
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


