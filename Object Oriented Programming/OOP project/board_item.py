class BoardItem:
    def __init__(self, title, due_date):
        self._title = None
        self.due_date = due_date 
        self.status = "Open"

    @property 
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, value):
        if len(value) < 5 or len(value) > 30:
            raise ValueError("Title must be a non-empty string with character length between 5 and 30 inclusive.")

        self._title = value
