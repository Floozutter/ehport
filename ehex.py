from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://e-hentai.org/bounce_login.php")
    driver.find_element_by_name("UserName").send_keys(input("username: "))
    driver.find_element_by_name("PassWord").send_keys(getpass("password: "))
    driver.find_element_by_name("ipb_login_submit").click()
    driver.get("https://e-hentai.org/favorites.php")
