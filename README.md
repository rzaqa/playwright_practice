# Create virtual environment with venv
```bash
python3 -m venv venv
```

# Activate venv
```bash
source venv/bin/activate
```

# Install playwright
```bash
pip install playwright
```

# Install PyTest
```bash
pip install pytest
```

# Install plugin
```bash
pip install pytest-playwright
```

# Install browsers (Chromium, Firefox, WebKit.)
```bash
playwright install
```

# Install only Firefox
```bash
playwright install firefox
```

# Work with codegen

Run codegen tool
```bash
playwright codegen demo.playwright.dev/todomvc/#/
```

 Run codegen tool
```bash
playwright codegen demo.playwright.dev/todomvc/#/
```

 Run codegen and define browser windows size
```bash
playwright codegen --viewport-size=800,600 https://demo.playwright.dev/todomvc/#/
```

 Run codegen and save test script in file
```bash
playwright codegen -o lesson.py https://demo.playwright.dev/todomvc/#/
```

Codegen -help
```bash
playwright codegen --help
```




# Official documentation Playwright for Python
https://playwright.dev


# Run test with PyTest
```bash
pytest
```

run tests with some options:
1. In headed mode:
```bash
pytest --headed
```
2. With specific browsers
```bash
pytest --headed --browser webkit --browser firefox
```

3. Run tests via browsers installed on LapTop
```bash
pytest --browser-channel=msedge --headed
```

4. Slowing down test execution
```bash
pytest --slowmo 1000
```
5. Running in emulation of device
```bash
pytest --device="iPhone 13 Mini"
```
6. Enable tracing for each test execution
```bash
pytest --tracing=on
```

7. Record video for each test (on, off or retain-on-failure)
```bash
pytest --video=retain-on-failure
```

8. Make screenshots after each test
```bash
pytest --screenshot=on
```

# Run test in DEBUG mode:
```bash
PWDEBUG=1 pytest -k 'test_todo'
```
or we can read a API logs from Playwright, need to use DEBUG=pw:api
```bash
DEBUG=pw:api
```


# Get UI element using built-in Playwright locators
1. in DevTools -> Console, you can past 
```bash
playwright.getByPlaceholder("What needs to be done?")
```
2. Or using using "playwright.inspect(selector)"
3. Generate locator "playwright.generateLocator($0)"


# Install allure 
```bash
pip install allure-pytest
```

# Run tests and generating allure report:
```bash
pytest --alluredir=reports
```
or add to pytest.ini
```
[pytest]
addopts = --alluredir=reports
```

Generate allure report from a raw data (need to delete existing allure-report directory)
```bash
allure generate reports
```

Open allure report from a generated report
```bash
allure open
```