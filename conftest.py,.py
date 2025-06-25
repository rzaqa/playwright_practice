import pytest

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
