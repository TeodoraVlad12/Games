class MyException(Exception):
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self._message

x =5
ok=0
if x==2:
    print("da")
if x==7:
    print("nu")