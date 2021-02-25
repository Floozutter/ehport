from common import Favorite, CSV_DIALECT, login
from requests_html import HTMLSession, HTMLResponse
from csv import DictReader
from time import sleep
from getpass import getpass

SECONDS_PER_FAV = 1

def favorite_favorite(session: HTMLSession, favorite: Favorite) -> HTMLResponse:
    raise NotImplementedError

if __name__ == "__main__":
    session = HTMLSession()
    login(session, input("username: "), getpass("password: "))
    with open(input("input file: "), mode = "r") as ifile:
        reader = DictReader(ifile, fieldnames = None, dialect = CSV_DIALECT)
        for row in reader:
            favorite = Favorite(**row)
            favorite_favorite(session, favorite)
            print(f"favorited {favorite}.")
            sleep(SECONDS_PER_FAV)
    print("all imported. >:3c")
