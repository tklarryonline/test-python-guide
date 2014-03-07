from lettuce import after, world, step, before
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import sure

def browser():
    if not hasattr(world, 'browser'):
        world.browser = webdriver.Firefox()
    return world.browser

@after.all
def close_browser(test):
    if hasattr(world, 'browser'):
        world.browser.quit()

def find_all(selector):
    return browser().find_elements_by_css_selector(selector)

def find(selector):
    return browser().find_element_by_css_selector(selector)

def xpath(selector):
    return browser().find_element_by_xpath(selector)

WebElement.find = WebElement.find_element_by_css_selector
WebElement.find_all = WebElement.find_elements_by_css_selector
WebElement.xpath = WebElement.find_element_by_xpath