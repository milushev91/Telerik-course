from item_status import ItemStatus
from board_item import BoardItem
from datetime import date, timedelta
from board import Board
 
def add_days_to_now(d):
    """This function help us parse the number of days(d) which is an integer into a datetime object.
    """
    return date.today() + timedelta(days = d)

# item = BoardItem('2323232323', add_days_to_now(2))
# print(item.title)
# print(item.due_date)
# print(item.status)

# item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
# print(item.status) # Open
# item.advance_status()
# print(item.status) # Todo
# item.advance_status()
# print(item.status) # In progress
# item.revert_status()
# print(item.status) # Todo

# item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
# print(item.info())

item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
anotherItem = BoardItem('Encrypt user data', add_days_to_now(10))
 
item.advance_status()
 
board = Board()
 
board.items.append(item)
board.items.append(anotherItem)
 
for board_item in board.items:
    board_item.advance_status()
 
for board_item in board.items:
    print(board_item.info())
