import allure_commons
import pytest
from appium import webdriver
from selene import support
from selene.support.shared import browser

import config
from utils import attachments


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = config.settings.timeout * 2

    yield

    attachments.video(browser)

    browser.quit()
