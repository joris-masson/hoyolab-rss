from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def initialize_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)
