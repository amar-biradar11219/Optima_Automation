import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from utilities.read_excel import Utils


class CustomerManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)


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
        self.logger.info("Navigating to Customer Management")
        self.wait_and_click(self.MENU)
        self.wait_and_click(self.CUSTOMER_MANAGEMENT)



    # createdCustomerTestData= Utils.read_data_from_excel("testdata/usercradentials.xlsx","Customer data")
    # @pytest.mark.parametrize("testdata", createdCustomerTestData)
    def create_Customer(self, customer_data):
        """
        Create a new customer using provided customer data dictionary
        """
        self.logger.info(f"Creating new customer: {customer_data['customer_name']}")

        self.wait_and_click(self.MENU)
        self.wait_and_click(self.ADD_NEW_BUTTON)

        # Fill in customer details
        self.wait_and_send_keys(self.CUSTOMER_NAME, customer_data['customer_name'])
        self.wait_and_send_keys(self.PARENT_COMPANY, customer_data['Parent_company'])
        self.wait_and_send_keys(self.ADDRESS, customer_data['address'])
        self.wait_and_send_keys(self.DEPARTMENT, customer_data['department'])
        self.wait_and_send_keys(self.SUBSIDIARY, customer_data['subsidiary'])
        self.wait_and_send_keys(self.LOCATION, customer_data['location'])
        self.wait_and_send_keys(self.PHONE_NUMBER, customer_data['phone_number'])
        self.wait_and_send_keys(self.EMAIL_ADDRESS, customer_data['email_addres'])
        self.wait_and_send_keys(self.COMMENTS, customer_data['comments'])
        self.wait_and_send_keys(self.CONTACT_NAME, customer_data['contact_name'])

        self.logger.info("Customer details entered successfully")
