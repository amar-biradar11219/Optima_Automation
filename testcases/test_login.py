import time

import pytest

from utilities.logger import LogGenerator
from utilities.read_excel import Utils


# testdata =Utils.read_data_from_excel("testdata/usercradentials.xlsx","Cradentials")
@pytest.mark.skip
class Test_Login:
    def test_login(self, setup):
        driver = setup
        time.sleep(5)
        print(driver.title)
