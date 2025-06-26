import pytest
import sys
import os
# This will add the directory 04_pom to PYTHONPATH, will work withoutmarking as  SOURSE ROOT folder or  without .ini file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '04_pom')))

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "root-secret",
                    "value": "sd4fFfv!x_cfcroot",
                    "url": "https://example.com"
                },
            ]
        },
    }

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)