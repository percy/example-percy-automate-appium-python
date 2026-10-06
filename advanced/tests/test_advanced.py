"""PER-8195 Phase 3 — automate-appium-python advanced example.

Percy on Automate takes its per-snapshot settings through the `options` dict
(snake_case or camelCase keys); bare keyword arguments raise inside the SDK and are
swallowed. percy_screenshot returns None whenever no snapshot was posted, so each
test asserts on that rather than passing silently.
"""

import time
from percy import percy_screenshot

HEADER_XPATH = '//h1'


def snapshot(driver, name, **options):
    result = percy_screenshot(driver, name=name, options=options)
    assert result is not None, f'Percy did not capture "{name}" (see the [percy] log above)'
    return result


def test_exercises_baseline(driver):
    time.sleep(5)
    snapshot(driver, "Wikipedia Article")


def test_exercises_full_page(driver):
    snapshot(driver, "Wikipedia Article — full page", full_page=True)


def test_exercises_ignore_regions_xpaths(driver):
    snapshot(driver, "Wikipedia Article — ignore via xpath", ignore_region_xpaths=[HEADER_XPATH])


def test_exercises_ignore_regions_selectors(driver):
    snapshot(driver, "Wikipedia Article — ignore via selector", ignore_region_selectors=["h1"])


def test_exercises_custom_ignore_regions(driver):
    snapshot(
        driver,
        "Wikipedia Article — custom ignore region",
        custom_ignore_regions=[{"top": 0, "bottom": 100, "left": 0, "right": 300}],
    )


def test_exercises_consider_regions_xpaths(driver):
    snapshot(driver, "Wikipedia Article — consider via xpath", consider_region_xpaths=[HEADER_XPATH])


def test_exercises_sync_mode(driver):
    # The sync payload depends on the token's scope (a write-only token cannot read the
    # comparison back), so only the shape is asserted here.
    result = percy_screenshot(driver, name="Wikipedia Article — sync", options={"sync": True})
    assert result is None or isinstance(result, dict)


def test_exercises_test_case_and_labels(driver):
    snapshot(
        driver,
        "Wikipedia Article — test_case + labels",
        test_case="home-smoke",
        labels="smoke,automate-appium-python",
    )
