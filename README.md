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





