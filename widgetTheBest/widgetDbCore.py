import sqlite3

class widgetDbCore:
    def __init__(self):
        # Create a database in RAM and connect:
        self._mDb = sqlite3.connect(':memory:')
        # get cursor object
        cursor = self._mDb.cursor()
        # create widgets table. This will be the body, or "Core" of our class
        # Properties have been defined as:
        # 1. Name(utf8 string, limited to 64 chars), data type: CHAR of size 64
        # 2. Number of parts(integer), data type: INT (no size)
        # 3. Created date(date, automatically set), data type: DATE
        # 4. Updated date(date, automatically set), data type: DATE
        # 0. of course we need an id, noted first below
        cursor.execute('''
            CREATE TABLE widgets(id INTEGER PRIMARY KEY, Name CHAR(64),
                               Number INT, Created DATE unique, Updated DATE)
        ''')
        widgetDb.commit()
    def __del__(self):
        # when this class is deleted, close our DB. Because, hey, it's the right thing to do.
        self._mDb.close()
