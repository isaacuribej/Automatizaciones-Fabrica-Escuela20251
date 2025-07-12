# conftest.py

import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        "ignore_https_errors": True
    }

@pytest.fixture(scope="session")
def base_url():
    return "https://courier-sync.vercel.app"
