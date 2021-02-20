from typing import NamedTuple

class Favorite(NamedTuple):
    gid: str
    t: str
    color_title: str

def login(session, username: str, password: str) -> None:
    raise NotImplementedError
