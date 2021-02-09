from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://e-hentai.org/bounce_login.php?b=d&bt=1-6")
    driver.find_element_by_name("UserName").send_keys(input("username: "))
    driver.find_element_by_name("PassWord").send_keys(getpass("password: "))
