class ElementNotFondException(Exception):
    pass
class CustomBaseException(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)

class ElementNotFoundException(CustomBaseException):
    """Exception raised when element not found."""


class InvalidScrollOptionException(CustomBaseException):
    def __init__(self, message, cause=None):
        super().__init__(message)
        self.__cause__ = cause
