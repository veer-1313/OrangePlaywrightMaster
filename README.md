# OrangeHRMApplicationPlaywright

Python Playwright + pytest automation framework for:

`https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`

## Project structure

```text
config/       Environment-backed settings
pages/        Page Object Model classes
 api/         API client and endpoint modules
 testdata/    JSON test data
 tests/       pytest UI and API test cases
utils/        Shared data helpers
conftest.py   Browser lifecycle and pytest options
.github/      CI workflow and repository guidance
```

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m playwright install chromium firefox
Copy-Item .env.example .env
```

The default UI target is public and does not require credentials. Keep secrets in environment variables and never commit them.

## Run tests

Run the complete suite in headless Chrome:

```powershell
pytest --headless
```

Run only the smoke tests in Firefox:

```powershell
pytest -m smoke --browser-name firefox --headless
```

Run with a visible Chrome browser:

```powershell
pytest --browser-name chrome
```

Run API checks only:

```powershell
pytest tests\api
```

Create an HTML report:

```powershell
pytest --headless --html=reports\login-report.html --self-contained-html
```

Create an Allure report:

```powershell
pytest --headless --alluredir=reports\allure-results
allure serve reports\allure-results
```

Each test outcome is written to `Log\automation.log`. Failed UI tests automatically
create a full-page image in `Screenshot\` and attach it to the Allure result.

Playwright manages its browser binaries. The target site must be reachable from the test machine.
