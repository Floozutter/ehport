from common import Favorite, CSV_DIALECT, URL_GALLERYPOPUPS, login
from requests_html import HTMLSession, HTMLResponse
from csv import DictReader
from time import sleep
from getpass import getpass
from typing import Optional

SECONDS_PER_FAV = 1

class FavNotFoundError(Exception):
    pass

def favorite_favorite(session: HTMLSession, favorite: Favorite) -> HTMLResponse:
    params = {
        "gid": favorite.gid,
        "t": favorite.t,
        "act": "addfav",
    }
    r = session.get(URL_GALLERYPOPUPS, params = params)
    rows = r.html.find("div.nosel > div")
    def find_value(rows, favname: str) -> Optional[str]:
        for row in rows:
            if row.find("div[onclick]")[-1].text == favname:
                return row.find("input", first = True).attrs["value"]
        return None
    value = find_value(rows, favorite.color_title)
    if value is None:
        raise FavNotFoundError
    else:
        data = {
            "favcat": value,
            "update": "1",
        }
        return session.post(URL_GALLERYPOPUPS, params = params, data = data)

if __name__ == "__main__":
    session = HTMLSession()
    login(session, input("username: "), getpass("password: "))
    with open(input("input file: "), mode = "r") as ifile:
        reader = DictReader(ifile, fieldnames = None, dialect = CSV_DIALECT)
        for i, row in enumerate(reader):
            favorite = Favorite(**row)
            favorite_favorite(session, favorite)
            print(f"[{i}] favorited {favorite}.")
            sleep(SECONDS_PER_FAV)
    print("all imported. >:3c")
