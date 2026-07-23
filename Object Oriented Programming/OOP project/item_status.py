class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    @classmethod
    def get_next(cls, current):
    # logic to return the next valid ItemStatus, based on current 
        if current == "Open":
            return cls.TODO
        elif current == "Todo":
            return cls.IN_PROGRESS
        elif current == "In progress":
            return cls.DONE
        elif current == "Done":
            return cls.VERIFIED
        else:
            return cls.VERIFIED
            
    @classmethod
    def get_previous(cls, current):
        if current == 'Verified':
            return cls.DONE
        elif current == "Done":
            return cls.IN_PROGRESS
        elif current == "In progress":
            return cls.TODO
        elif current == "Todo":
            return cls.OPEN
        else:
            return cls.OPEN

    
