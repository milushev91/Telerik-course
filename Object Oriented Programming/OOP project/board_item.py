from datetime import date
from item_status import ItemStatus
from event_log import EventLog

class BoardItem:
    def __init__(self, title:str, due_date:date) -> None:
        self._title = title
        self._due_date = due_date 
        self._status = ItemStatus.OPEN
        event = EventLog(f"Item created: {self.title}, [{self._status} | {self.due_date}]")
        self._events:list[str] = [event.info()]

    @property 
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, value):
        if len(value) < 5 or len(value) > 30:
            raise ValueError("Title must be a non-empty string with character length between 5 and 30 inclusive.")

        self._title = value

    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value):
        if date.today() > value:
            raise ValueError("Due date cannot be into the past.")
        
        current_due_date = self._due_date
        self._due_date = value
        event = EventLog(f"DueDate changed from {current_due_date} to {self._due_date}")
        self._events.append(event.info())

    @property 
    def status(self):
        return self._status 
    
    @property
    def events(self):
        return self._events
    
    def revert_status(self) -> None:
        self._status = ItemStatus.get_previous(self._status)
    
    def advance_status(self) -> None:
        self._status = ItemStatus.get_next(self._status)
    
    def info(self) -> str:
        return f"{self.title}, [{self._status} | {self.due_date}]"
    
    def history(self) -> str:

        for event in self.events:
            print(event)
    
