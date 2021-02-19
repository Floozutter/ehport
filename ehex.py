from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from getpass import getpass
from typing import NamedTuple

class Favorite(NamedTuple):
    gid: str
    t: str
    color_title: str

def login(driver, username: str, password: str) -> None:
    driver.get("https://e-hentai.org/bounce_login.php")
    driver.find_element_by_name("UserName").send_keys(username)
    driver.find_element_by_name("PassWord").send_keys(password)
    driver.find_element_by_name("ipb_login_submit").click()

def set_modes(driver) -> None:
    driver.get("https://e-hentai.org/favorites.php?inline_set=fs_f")  # favorited order
    driver.get("https://e-hentai.org/favorites.php?inline_set=dm_m")  # minimal display mode

def get_pages(driver) -> int:
    driver.get("https://e-hentai.org/favorites.php")
    return int(driver.find_elements_by_css_selector("table.ptt td")[-2].text)

def get_favorites(driver, page: int) -> tuple[Favorite, ...]:
    driver.get(f"https://e-hentai.org/favorites.php?page={page}")
    rows = driver.find_elements_by_css_selector("table.itg.gltm tr:not(:first-of-type)")
    def parse(row) -> Favorite:
        url = row.find_element_by_css_selector("td.gl3m.glname a").get_attribute("href")
        _, gid, t = filter(None, urlparse(url).path.split("/"))
        ct = row.find_element_by_css_selector("td.gl2m > div:last-child").get_attribute("title")
        return Favorite(gid, t, ct)
    return tuple(map(parse, rows))

if __name__ == "__main__":
    d = webdriver.Firefox()
    login(d, input("username: "), getpass("password: "))
    set_modes(d)
    pages = get_pages(d)
    favorites = tuple(f for p in range(pages)[::-1] for f in get_favorites(d, p))
