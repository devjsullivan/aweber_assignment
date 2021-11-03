import sqlite3
import time
from classes.widgetDbCore import widgetDbCore

if __name__ == '__main__':
    # This will be a test driver until we can get to creating unit test:
    myWidgetDbCore = widgetDbCore()
    print("widgetDbCore should initialize to be empty, so let's verify by calling list_all(), (after asterisks):")
    print("***************************")
    myWidgetDbCore.list_all()
    print("***************************")
    print("list_all() just called. Was anything output between the asterisks?:")
    print("Okay, now let's add some rows to the database (starting with Name Marnie and Number 2), then list_all() again, (after asterisks):")
    myWidgetDbCore.create("Marnie", 2)
    print("***************************")
    myWidgetDbCore.list_all()
    print("Okay, now let's try to add a row with name size greater than 64 to prove Name length is monitored:")
    myWidgetDbCore.create("Marnie12345678901234567890012345678900123456789001234567890012345678900123456789001234567890", 2)
    print("***************************")
    myWidgetDbCore.list_all()
    print("***************************")
    print("list_all() just called. There should be one row listed between the asterisks?:")
    print("Now let's update this row. id should be 1 by default. So let's change the name from Marnie to Charlie. Before we do this, let's sleep a few seconds as well so we can see Update time modified, too.")
    time.sleep(5)
    myWidgetDbCore.update_name_by_id(1, "Charlie")
    print("***************************")
    myWidgetDbCore.list_all()
    print("***************************")
    print("update_name_by_id() then list_all()  just called. Name should be changed & update time a little later, no?")
    print("Now let's update the number via name. Using Charlie, let's verify the update_number_by_name function and change Number to 5, also sleeping 10 seconds to verify update time works.")
    time.sleep(10)
    myWidgetDbCore.update_number_by_name("Charlie", 5)
    print("***************************")
    myWidgetDbCore.list_all()
    print("***************************")
    print("update_number_by_name() then list_all()  just called. Number should be changed & update time a little later, no?")
    print("Now let's try out the delete function, and delete record with id = 1 (as that's all we have).")
    print("***************************")
    myWidgetDbCore.list_all()
    print("***************************")
    print("list_all() before delete() just called between asterisks. Number of records should still be one.")
    print("***************************")
    print("Calling delete now:")
    myWidgetDbCore.delete(1)
    print("***************************")
    print("***************************")
    myWidgetDbCore.list_all()
    print("***************************")
    print("list_all() called after delete() between asterisks. Number of records should be zero.")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
