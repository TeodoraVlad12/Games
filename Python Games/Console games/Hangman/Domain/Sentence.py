class Sentence:
    def __init__(self, the_sen: list, sen: list, the_hang: list, hang: list ):
        self._the_sen = the_sen
        self._sen = sen
        self._the_hang = the_hang
        self._hang = hang
        self._all = all
        self._the_hang = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        self._hang = ["_", "_" , "_", "_", "_", "_", "_"]

    @property
    def the_sen(self):
        return self._the_sen

    @property
    def sen(self):
        return self._sen

    @property
    def the_hang(self):
        return self._the_hang

    @property
    def hang(self):
        return self._hang

    @property
    def all(self):
        return self._all

    @the_sen.setter
    def the_sen(self, new):
        self._the_sen = new

    @sen.setter
    def sen(self, new):
        self._sen = new

    @the_hang.setter
    def the_hang(self, new):
        self._the_hang = new

    @hang.setter
    def hang(self, new):
        self._hang = new

    @all.setter
    def all(self, new):
        self._all = all

    def update(self):
        pass

    def __str__(self):
        result=""
        for i in range(len(self._sen)):
            if self._sen[i] == " ":
                result += " "
            elif self._sen[i] == "_":
                result += "_"
            else:
                result += self._sen[i]
        result += " "
        result += "-"
        result += " "

        for i in range(len(self._hang)):
            if self._hang[i] == None:
                result += "_"
            else:
                result += self._hang[i]
        return result

class Validator:
    pass

