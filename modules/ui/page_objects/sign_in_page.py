from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https:\\github.com\login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")

        #enter wrong data
        login_elem.send_keys(username)
                            
        #finding password field
        pass_elem = self.driver.find_element(By.ID, "password")

        #enter wrong password
        pass_elem.send_keys(password)
 
        #finding button sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        #leftClick
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title