import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class CustomerManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = driver.WebDriverWait(self.driver, 10)


    # Locators
    MENU = (By.XPATH, "//i[@class='bx bx-grid-alt bx-sm pt-1']")
    CUSTOMER_MANAGEMENT = (By.XPATH, "//ul[@class='list-unstyled list-group notification navs module-wise']//a[@routerlinkactive='active'][normalize-space()='Customer Management']")
    ADD_NEW_BUTTON = (By.XPATH, "//button[contains(text(),'Add New')]")
    CUSTOMER_NAME = (By.XPATH, "//input[@formcontrolname='customerName']")
    PARENT_COMPANY = (By.XPATH, "//input[@formcontrolname='parentCompany']")
    ADDRESS = (By.XPATH, "//input[@formcontrolname='address']")
    DEPARTMENT = (By.XPATH, "//input[@formcontrolname='department']")
    SUBSIDIARY = (By.XPATH, "//input[@formcontrolname='subsidiary']")
    LOCATION = (By.XPATH, "//input[@formcontrolname='location']")
    PHONE_NUMBER = (By.XPATH, "//input[@formcontrolname='phoneNumber']")
    EMAIL_ADDRESS = (By.XPATH, "//input[@formcontrolname='emailAddress']")
    COMMENTS = (By.XPATH, "//input[@formcontrolname='comments']")
    CONTACT_NAME = (By.XPATH, "//input[@formcontrolname='contactName']")
    CONTACT_PHONE = (By.XPATH, "//input[@formcontrolname='contactPhone']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    def navigate_to_customer_management(self):
        time.sleep(5)
        self.driver.find_element(*self.MENU).click()
        self.driver.find_element(*self.CUSTOMER_MANAGEMENT).click()
        # print("Menu clicked")
        time.sleep(2)
        print("Navigating to Customer Management")

