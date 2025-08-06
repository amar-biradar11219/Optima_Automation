from pages.customer_management_page import CustomerManagementPage
from utilities.read_excel import Utils
import pytest

class Test_CustomerManagement:


    test_data = Utils.read_data_from_excel("testdata/customer_management_data.xlsx", "customer_data")
    @pytest.mark.parametrize("test_data", test_data)
    @pytest.mark.usefixtures("setup")
    def test_create_customer(self,setup, test_data):
        self.driver = setup
        print(test_data)
        self.customer_management_pages = CustomerManagementPage(self.driver)
        self.customer_management_pages.navigate_to_customer_management()
        self.customer_management_pages.create_customer(test_data)

        # Add assertions to verify customer creation
        # Add assertions or further actions as needed



