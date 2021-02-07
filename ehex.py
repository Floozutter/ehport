from selenium import webdriver
from getpass import getpass

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://e-hentai.org/favorites.php")
    username = input("username: ")
    password = getpass("password: ")    
