from datetime import datetime

class EventLog:
    def __init__(self, description: str) -> None:
        if not description or not description.strip():
            raise ValueError("Description cannot be empty") 
            
        self._description = description.strip()
        self._timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    @property 
    def description(self):
        return self._description
    
    @property
    def timestamp(self):
        return self._timestamp
    
    def info(self) -> str:
        return f"[{self._timestamp}] {self._description}"
