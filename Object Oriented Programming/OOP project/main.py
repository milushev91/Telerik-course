from item_status import ItemStatus
from board_item import BoardItem
from datetime import date, timedelta
 
def add_days_to_now(d):
    """This function help us parse the number of days(d) which is an integer into a datetime object.
    """
    return date.today() + timedelta(days = d)

item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
print(item.title)
print(item.due_date)
print(item.status)
