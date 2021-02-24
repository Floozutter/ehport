from common import URL_FAV, Favorite, login
from requests_html import HTMLSession, HTMLResponse
from urllib.parse import urlparse
from getpass import getpass

def inline_set(session: HTMLSession, var: str, val: str) -> HTMLResponse:
    return session.get(URL_FAV, params = {"inline_set": f"{var}_{val}"})

def scrape_pagecount(session: HTMLSession) -> int:
    r = session.get(URL_FAV)
    pages = r.html.find("table.ptt td")
    return int(pages[-2].text)

def scrape_favorites(session: HTMLSession, page: int) -> tuple[Favorite, ...]:
    r = session.get(URL_FAV, params = {"page": page})
    rows = r.html.find("table.itg.gltm tr")[1:]
    def parse(row) -> Favorite:
        url = row.find("td.gl3m.glname a", first = True).attrs["href"]
        _, gid, t = filter(None, urlparse(url).path.split("/"))
        ct = row.find("td.gl2m > div:last-child", first = True).attrs["title"]
        return Favorite(gid, t, ct)
    return tuple(map(parse, rows))

if __name__ == "__main__":
    s = HTMLSession()
    login(s, input("username: "), getpass("password: "))
    inline_set(s, "fs", "f")  # sort by favorites
    inline_set(s, "dm", "m")  # minimal display mode
    pagecount = scrape_pagecount(s)
    #favorites = tuple(f for p in range(pages)[::-1] for f in get_favorites(d, p))
