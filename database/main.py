# we will open the already exist file of the database.db and then we wiil operate on  him

import sys

from database.Repository import *


def main(id):
    price = repo.getprice(id)
    print(price, repo.lastindex())  # {price of product, number of items in tables}
    return price, repo.lastindex()


if __name__ == "__main__":
    if len(sys.argv) != 1:
        raise ValueError("usage")
    main(3)
