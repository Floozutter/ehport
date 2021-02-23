from common import Favorite, login
from requests_html import HTMLSession
from urllib.parse import urlparse
from getpass import getpass

def set_modes(driver) -> None:
    raise NotImplementedError
    driver.get("https://e-hentai.org/favorites.php?inline_set=fs_f")  # favorited order
    driver.get("https://e-hentai.org/favorites.php?inline_set=dm_m")  # minimal display mode

def get_pages(driver) -> int:
    raise NotImplementedError
    driver.get("https://e-hentai.org/favorites.php")
    return int(driver.find_elements_by_css_selector("table.ptt td")[-2].text)

def get_favorites(driver, page: int) -> tuple[Favorite, ...]:
    raise NotImplementedError
    driver.get(f"https://e-hentai.org/favorites.php?page={page}")
    rows = driver.find_elements_by_css_selector("table.itg.gltm tr:not(:first-of-type)")
    def parse(row) -> Favorite:
        url = row.find_element_by_css_selector("td.gl3m.glname a").get_attribute("href")
        _, gid, t = filter(None, urlparse(url).path.split("/"))
        ct = row.find_element_by_css_selector("td.gl2m > div:last-child").get_attribute("title")
        return Favorite(gid, t, ct)
    return tuple(map(parse, rows))

if __name__ == "__main__":
    s = HTMLSession()
    login(s, input("username: "), getpass("password: "))
    #set_modes(d)
    #pages = get_pages(d)
    #favorites = tuple(f for p in range(pages)[::-1] for f in get_favorites(d, p))
