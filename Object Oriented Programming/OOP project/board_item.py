from datetime import date

class BoardItem:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date 
        self._status = "Open"

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
        
        self._due_date = value
    
    @property 
    def status(self):
        return self._status 
    
    @status.setter
    def status(self, value):
        if value not in ["Open", "Todo", "InProgress", "Done", "Verified"]:
            raise ValueError("Not valid status")
        
        self._status = value
