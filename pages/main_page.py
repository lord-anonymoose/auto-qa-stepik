from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()