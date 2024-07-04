import logging
from Utility.customLogger import LogGenerator
class Test_001_Login:
    logger=LogGenerator.custom_logger()

    def test_login_page_title(self):
        self.logger.info("Hiiiii")
        assert True