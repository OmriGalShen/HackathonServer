class _Electronics:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, electronic):
        self._cursor.execute("""
                    INSERT INTO Objects (id, date, supplier, quantity) VALUES (?, ?, ?)
                """, [electronic.id, electronic.price, electronic.model])

    """If an order request has been set, 
    we update the quantity and then check with get quantity if quantity==0. if we do we remove him from the table"""

    def delete(self, id):
        self._cursor.execute("""
                    DELETE FROM Objects WHERE id = ?""", [id])

    def search(self, id):
        self._cursor.execute("""
                    SELECT price FROM Objects WHERE id = ?""", [id])