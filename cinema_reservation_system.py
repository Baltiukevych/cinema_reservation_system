from pprint import pprint as pp
from movie import Movie
from cinemas import *
from helpers import *


def make_movie():
    f = Movie("2007", City())
    f.allocate_client("Magda M", "1A")
    f.allocate_client("Gosia D", "3B")
    f.allocate_client("Jola G", "1C")
    f.relocate_client("1A", "1D")
    pp(f.seats)

    print(f.count_empty_seats())
    f.print_card(card_printer)

make_movie()
