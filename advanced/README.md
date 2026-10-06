# Advanced Percy on Automate + Appium-Python

Exercises the Percy on Automate feature surface via `percy-appium-app` (Python) on a
mobile-browser session (Chrome on a real Android device). Native apps use App Percy
instead — see `example-percy-appium-python`.

## Run locally

```bash
cd advanced
make install
export BROWSERSTACK_USERNAME="<your username>"
export BROWSERSTACK_ACCESS_KEY="<your access key>"
export APPIUM_VERSION="2.19.0"   # optional; BrowserStack appiumVersion
export PERCY_TOKEN="<your project token>"
make test
```

## CI note

`workflow_dispatch`-only — Percy on Automate CI requires a real BrowserStack Automate session.

## Coverage matrix

Source of truth: [`matrix.yml`](./matrix.yml).
