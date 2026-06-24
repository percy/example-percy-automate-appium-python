"""PER-8195 Phase 3 — automate-appium-python advanced example."""

import time
from percy import percy_screenshot


def test_exercises_baseline(driver):
    time.sleep(5)
    percy_screenshot(driver, name="Wikipedia Home")


def test_exercises_device_name_and_orientation(driver):
    percy_screenshot(
        driver,
        name="Wikipedia Home — landscape",
        device_name="Samsung Galaxy S22 Ultra",
        orientation="landscape",
    )


def test_exercises_fullscreen_and_bars(driver):
    percy_screenshot(
        driver,
        name="Wikipedia Home — fullscreen",
        fullscreen=True,
        status_bar_height=24,
        nav_bar_height=0,
    )


def test_exercises_ignore_regions_xpaths(driver):
    percy_screenshot(
        driver,
        name="Wikipedia Home — ignore via xpath",
        ignore_regions_xpaths=['//android.widget.TextView[@text="Search Wikipedia"]'],
    )


def test_exercises_custom_ignore_regions(driver):
    percy_screenshot(
        driver,
        name="Wikipedia Home — custom ignore region",
        custom_ignore_regions=[{"top": 0, "bottom": 100, "left": 0, "right": 300}],
    )


def test_exercises_consider_regions_xpaths(driver):
    percy_screenshot(
        driver,
        name="Wikipedia Home — consider via xpath",
        consider_regions_xpaths=['//android.widget.TextView[@text="Search Wikipedia"]'],
    )


def test_exercises_sync_mode(driver):
    percy_screenshot(driver, name="Wikipedia Home — sync", sync=True)


def test_exercises_test_case_and_labels(driver):
    percy_screenshot(
        driver,
        name="Wikipedia Home — test_case + labels",
        test_case="home-smoke",
        labels="smoke,automate-appium-python",
    )
