"""PER-8195 — pytest fixtures: BrowserStack Automate appium driver (mobile web).

Percy on Automate with Appium captures a mobile *browser* session, the same flow as
../tests/test.py. Native-app sessions belong to App Percy (example-percy-appium-python):
the CLI's Automate capture path cannot read window metadata from an App Automate
native session, so screenshots there are never taken.
"""

import os
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

URL = os.environ.get("URL", "https://en.wikipedia.org/wiki/BrowserStack")


@pytest.fixture(scope="session")
def driver():
    capabilities = {
        "platformName": "Android",
        "browserName": "chrome",
        "bstack:options": {
            "userName": os.environ["BROWSERSTACK_USERNAME"],
            "accessKey": os.environ["BROWSERSTACK_ACCESS_KEY"],
            "deviceName": os.environ.get("DEVICE", "Samsung Galaxy S22 Ultra"),
            "osVersion": os.environ.get("OS_VERSION", "12.0"),
            "appiumVersion": os.environ.get("APPIUM_VERSION", "2.19.0"),
            "projectName": os.environ.get("PERCY_PROJECT", "Percy Automate Appium-Python Advanced"),
            "buildName": os.environ.get("PERCY_BUILD", "Advanced Automate Appium Python"),
            "sessionName": "advanced_visual_test",
        },
    }
    drv = webdriver.Remote(
        "https://hub-cloud.browserstack.com/wd/hub",
        options=AppiumOptions().load_capabilities(capabilities),
    )
    drv.get(URL)
    yield drv
    drv.quit()
