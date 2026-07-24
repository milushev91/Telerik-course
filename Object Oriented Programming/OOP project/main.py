from item_status import ItemStatus
from board_item import BoardItem
from calculate_date import add_days_to_now


item = BoardItem('2323232323', add_days_to_now(2))
print(item.title)
print(item.due_date)
print(item.status)


