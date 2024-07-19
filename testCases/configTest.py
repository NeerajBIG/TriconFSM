import os
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

def pytest_configure(config):
    config._metadata['Project Name'] = 'Test Project'
    config._metadata['Module Name'] = 'Test Module'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
