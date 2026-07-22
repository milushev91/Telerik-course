class ForumPost():

    def __init__(self, author: str, text: str, upvotes:int) -> None:
        self.author = author
        self.text = text 
        self.upvotes = upvotes
        self.replies:list[str] = []
    
    def view(self) -> str:
        result = f'{self.text} / by {self.author}, {self.upvotes} votes.'
        for reply in self.replies:
            result += f"\n- {reply}"

        return result
               
    def add_reply(self, reply: str) -> None:
        self.replies.append(reply)
