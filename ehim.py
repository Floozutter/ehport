from common import Favorite, CSV_DIALECT, login
from requests_html import HTMLSession, HTMLResponse
from csv import DictReader
from getpass import getpass
from typing import Tuple

SECONDS_PER_FAV = 1

if __name__ == "__main__":
    session = HTMLSession()
    login(session, input("username: "), getpass("password: "))
    with open(input("input file: "), mode = "r") as ifile:
        reader = DictReader(ifile, fieldnames = None, dialect = CSV_DIALECT)
        for row in reader:
            fav = Favorite(**row)
            print(fav)
    print("all imported. >:3c")
