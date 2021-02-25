from common import Favorite, CSV_FIELDNAMES, CSV_DIALECT, URL_FAVS, login
from requests_html import HTMLSession, HTMLResponse
from urllib.parse import urlparse
from csv import DictWriter
from time import sleep
from getpass import getpass

SECONDS_PER_PAGE = 1

def inline_set(session: HTMLSession, var: str, val: str) -> HTMLResponse:
    return session.get(URL_FAVS, params = {"inline_set": f"{var}_{val}"})

def scrape_pagecount(session: HTMLSession) -> int:
    r = session.get(URL_FAVS)
    pages = r.html.find("table.ptt td")
    return int(pages[-2].text)

def scrape_favorites(session: HTMLSession, page: int) -> tuple[Favorite, ...]:
    r = session.get(URL_FAVS, params = {"page": page})
    rows = r.html.find("table.itg.gltm tr")[1:]
    def parse(row) -> Favorite:
        url = row.find("td.gl3m.glname a", first = True).attrs["href"]
        _, gid, t = filter(None, urlparse(url).path.split("/"))
        ct = row.find("td.gl2m > div:last-child", first = True).attrs["title"]
        return Favorite(gid, t, ct)
    return tuple(map(parse, rows))

if __name__ == "__main__":
    session = HTMLSession()
    login(session, input("username: "), getpass("password: "))
    session.get(URL_FAVS)  # get some more cookies to munch on
    inline_set(session, "fs", "f")  # sort by favorites
    inline_set(session, "dm", "m")  # minimal display mode
    pagecount = scrape_pagecount(session)
    with open(input("output file: "), mode = "w") as ofile:
        writer = DictWriter(ofile, fieldnames = CSV_FIELDNAMES, dialect = CSV_DIALECT)
        writer.writeheader()
        for page in range(pagecount)[::-1]:
            favorites = scrape_favorites(session, page)[::-1]
            writer.writerows(map(lambda fav: fav._asdict(), favorites))
            print(f"scraped {len(favorites)} favorites from page {page}.")
            sleep(SECONDS_PER_PAGE)
    print("all done. >:3c")
