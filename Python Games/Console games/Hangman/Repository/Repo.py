from Domain.Sentence import Sentence
import random

class Repo:
    def __init__(self, file_name):
        self._file_name = file_name
        self._data = []
        self._load_file()

    def _load_file(self):
        lines = []
        try:
            fin = open(self._file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError as io:
            pass

        for line in lines:
            atributes = line.split(',')
            new_sen = []
            i=0
            while i < len(atributes):
                if atributes[i] == "_":
                    new_sen.append(" ")
                else:
                    new_sen.append(atributes[i])
                i += 1
            self._data.append(new_sen)

    def get_all_sen(self):
        return list(self._data)

    def save_file(self):
        fout = open(self._file_name, "wt")
        for sen in self.get_all_sen():
            new= ""
            i = 0
            while i < len(sen):
                if sen[i]==" ":
                    new += "_"
                    new += ","
                else:
                    new += sen[i]
                    new += ","
                i += 1
            new += '\n'
            fout.write(new)
        fout.close()

    def select_sen(self):
        n = len(self.get_all_sen())
        nr = random.randint(0,n-1)
        return self._data[nr]

    def add_sen(self, sen):
        self._data.append(sen)
        self.save_file()

    def search_for_duplicate(self, sen):
        ok = 1
        for sentence in self.get_all_sen():
            check = 1
            if len(sen) != len(sentence):
                check = 0
            else:
                ok2 = 1
                for i in range(len(sen)):
                    if sen[i] != sentence[i]:
                        ok2 = 0
                        break
                if ok2 == 1:
                    check = 1
            if check == 1:
                ok = 0
                break
        return ok          # returns 1 if there are no duplicates and 0 if there are








