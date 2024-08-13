from selenium.webdriver.common.by import By
class HomePage():

    def __init__(self,driver):
        self.driver = driver
    
        self.welcome_link_Class = "oxd-userdropdown-name"
        self.logout_link_class = "oxd-userdropdown-link"


    def click_welcome(self):
        self.driver.find_element(By.CLASS_NAME, self.welcome_link_Class).click()

    def click_logout(self):
        self.driver.find_element(By.CLASS_NAME, self.logout_link_class).click()