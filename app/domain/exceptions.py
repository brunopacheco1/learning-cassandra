class CommonException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class BookNotFoundException(CommonException):
    def __init__(self, name: str):
        super().__init__("Book[%s] not found." % name)

class AuthorNotFoundException(CommonException):
    def __init__(self, name: str):
        super().__init__("Author[%s] not found." % name)
