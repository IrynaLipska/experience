from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CheckTrack(BasePage):
    URL = 'https://novaposhta.ua'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(CheckTrack.URL)

    def enter_track_number(self, number):
        track_number = self.driver.find_element(By.ID, "cargo_number")

        track_number.send_keys(number)
        
        track_number.send_keys(Keys.ENTER)

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
