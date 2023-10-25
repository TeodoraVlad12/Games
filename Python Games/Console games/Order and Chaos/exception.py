class MyException(Exception):
    def __init__(self, message):
        self._message = message

    def get(self):
        return self._message

    def __str__(self):
        return self._message
