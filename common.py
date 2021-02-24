from requests_html import HTMLSession, HTMLResponse
from enum import Enum
from typing import NamedTuple

URL_LOGIN = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"
URL_FAV = "https://e-hentai.org/favorites.php"

class Favorite(NamedTuple):
    gid: str
    t: str
    color_title: str

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
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(text)
