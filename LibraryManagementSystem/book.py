# book.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def to_dict(self):
        return {"title": self.title, "author": self.author}

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'])
