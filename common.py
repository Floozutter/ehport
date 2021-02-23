from requests_html import HTMLSession, HTMLResponse
from typing import NamedTuple

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
    return session.post("https://forums.e-hentai.org/index.php?act=Login&CODE=01", data)
