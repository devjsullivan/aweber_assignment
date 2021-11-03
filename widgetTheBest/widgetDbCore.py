import sqlite3
from datetime import datetime


class widgetDbCore:
    def __init__(self):
        # Create a database in RAM and connect:
        self._mDb = sqlite3.connect(':memory:')
        # get cursor object, create one for self so we don't have to keep getting it for other functions
        self._mcursor = self._mDb.cursor()
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
    # add a row to the DB (dates will be updated automatically via datetime module
    def create(self, nameIn: str, numIn: int):
        current_date_and_time = datetime.now()
        pretty_date_and_time = now.strftime('%Y-%m-%d %H:%M:%S')
        # (created and updated times are the same, so use pretty_date_and_time for both:)
        self._mcursor.execute('''INSERT INTO widgets(Name, Number, Created, Updated)
                          VALUES(?,?,?,?)''', (nameIn, numIn, pretty_date_and_time, pretty_date_and_time))
    # output all widgets
    def list_all(self):
        widgets = self._mcursor.fetchall()
        print("Here is a list of all widgets in your database (colums are Name, Number, Date/time created, Date/time updated:")
        for w in widgets:
            # w[0] returns the first column in the query (Name), row[1] returns Number column, etc:
            print('{0} : {1}, {2}, {3}, {4}'.format(w[0], w[1], w[2], w[3], w[4]))
    def __del__(self):
        # when this class is deleted, close our DB. Because, hey, it's the right thing to do.
        self._mDb.close()
