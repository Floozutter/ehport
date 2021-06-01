from requests_html import HTMLSession, HTMLResponse
from csv import unix_dialect
from typing import NamedTuple

class Favorite(NamedTuple):
    gid: str  # gallery id
    t: str  # gallery token
    favname: str  # name of favorite category

CSV_FIELDNAMES = Favorite._fields
class CSV_DIALECT(unix_dialect):
    pass

URL_LOGIN = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"
URL_FAVORITES = "https://e-hentai.org/favorites.php"
URL_GALLERYPOPUPS = "https://e-hentai.org/gallerypopups.php"

def login(session: HTMLSession, username: str, password: str) -> HTMLResponse:
    data = {
        "UserName": username,
        "PassWord": password,
        "CookieDate": "1",
        "b": "d",
        "bt": "1-6",
    }
    return session.post(URL_LOGIN, data)

def pry(filename: str, text: str) -> None:
    with open(filename, mode = "w", encoding = "utf-8") as f:
        f.write(text)
