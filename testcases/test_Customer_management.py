import pytest
import logging
from pages.customer_management_page import CustomerManagementPage
from utilities.read_excel import ExcelUtils


class TestCustomerManagement:
    logger = logging.getLogger(__name__)

    @pytest.fixture(scope="class")
    def customer_data(self):
        return ExcelUtils.read_data_from_excel("testdata/usercradentials.xlsx", "Customer data")

    @pytest.mark.parametrize("testdata", customer_data)
    def test_create_customer(self, setup, testdata):
        """Test creating a new customer with data from Excel"""
        self.logger.info(f"Testing customer creation for: {testdata['customer_name']}")

        customer_management_page = CustomerManagementPage(setup)
        customer_management_page.navigate_to_customer_management()
        customer_management_page.create_Customer(testdata)

        # TODO: Add verification steps here to confirm customer was created
        self.logger.info("Customer creation test completed")
