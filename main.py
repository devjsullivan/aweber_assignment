from widgetDbCore import widgetDbCore

if __name__ == '__main__':
    # This will be a test driver until we can get to creating unit test:
    myWidgetDbCore = widgetDbCore()
    print("widgetDbCore should init empty, so let's verify by calling list_all(), (after asterisks):")
    print("***************************")
    myWidgetDbCorelist_all()
    print("***************************")
    print("list_all() just called. Was anything output between the asterisks?:")
    exit()


    print_hi('PyCharm')
    ret: int = usingTypeAnnots(6,8)

    print("Here: ", ret)

# Create a database in RAM and connect:
widgetDb = sqlite3.connect(':memory:')
# get cursor object
cursor = widgetDb.cursor()
# create widget table
cursor.execute('''
    CREATE TABLE widgets(id INTEGER PRIMARY KEY, Name CHAR(64),
                       Number INT, Created DATE unique, Updated DATE)
''')
widgetDb.commit()

#cursor = widgetDb.cursor()
#cursor.execute('''DROP TABLE widgets''')
#widgetDb.commit()


cursor = widgetDb.cursor()
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'

name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# Insert user 1
cursor.execute('''INSERT INTO widgets(Name, Number, Created, Updated)
                  VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
print('First user inserted')

# Insert user 2
cursor.execute('''INSERT INTO widgets(Name, Number, Created, Updated)
                  VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
print('Second user inserted')

widgetDb.commit()

cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone() #retrieve the first row
print("First row:\n")
print(user1[0]) #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

# are we done with the database? if so, close:
widgetDb.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
