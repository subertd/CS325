class InvalidInputException(Exception):
    def __init__(self, message):
        super(InvalidInputException, self).__init__(message)
