# we will open the already exist file of the database.db and then we wiil operate on  him

import sys

from database.Repository import *


def main(id):
    price = repo.getprice(2)
    print(price)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        raise ValueError("usage")
    main(2)
