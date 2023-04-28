class BookNotFound(Exception):
    def __init__(self, name: str):
        super().__init__(f"Book[{name}] not found.")

class AuthorNotFound(Exception):
    def __init__(self, name: str):
        super().__init__(f"Author[{name}] not found.")
