import sqlite3
import atexit

from DAO import _Electronics
from DTO import *


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect("electronics.db")
        self.electric = _Electronics(self._conn)  # instance of electrics

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        cursor = self._conn.cursor()
        cursor.execute("""CREATE TABLE Objects(id INTEGER PRIMARY KEY,
                                                    price INTEGER,
                                                    model TEXT,  
                                                    )
        """)

    def getprice(self, id):  # return the price of an item
        cursor = self._conn.cursor()
        cursor.execute("""
                            SELECT price FROM Objects WHERE id = ?""", [id])
        price = cursor.fetchone()[0]
        return price

    def getmodel(self, id):  # return the model of an item
        cursor = self._conn.cursor()
        cursor.execute("""
                            SELECT model FROM Objects WHERE id = ?""", [id])
        price = cursor.fetchone()[0]
        return price


repo = _Repository()
atexit.register(repo.close)