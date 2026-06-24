"""PER-8195 — pytest fixtures: BrowserStack App Automate appium driver."""

import os
import pytest
from appium import webdriver


@pytest.fixture(scope="session")
def driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": os.environ.get("DEVICE", "Samsung Galaxy S22 Ultra"),
        "platformVersion": os.environ.get("OS_VERSION", "12.0"),
        "app": os.environ["APP"],
        "bstack:options": {
            "userName": os.environ["BROWSERSTACK_USERNAME"],
            "accessKey": os.environ["BROWSERSTACK_ACCESS_KEY"],
            "projectName": os.environ.get("PERCY_PROJECT", "Percy Automate Appium-Python Advanced"),
            "buildName": os.environ.get("PERCY_BUILD", "Advanced Automate Appium Python"),
            "sessionName": "advanced_visual_test",
        },
    }
    drv = webdriver.Remote("https://hub-cloud.browserstack.com/wd/hub", capabilities)
    yield drv
    drv.quit()
