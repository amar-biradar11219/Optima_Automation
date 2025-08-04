from pages.customer_management_page import CustomerManagementPage


class TestCustomerManagement:
    def test_navigate_to_customer_management(self, setup):
        customer_management_page = CustomerManagementPage(setup)
        driver=setup
        customer_management_page.navigate_to_customer_management()

