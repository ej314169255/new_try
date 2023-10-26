from selenium import webdriver
from unittest import TestCase, main

#class ExampleSeleniumTest(TestCase):
def testSearch(self):
  dirver = webdriver.Firefox()
  dirver.get("https://www.cs/umd.edu/~mount/ANN/")
  driver.implicitly_wait(30)
  body = driver.find_element_by_link_text("ann_1.1.2.zip").click()
  return 0

if __name__ == '__main__':
  main()
