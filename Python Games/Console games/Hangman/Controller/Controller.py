from Domain.Sentence import Sentence
from Repository.Repo import Repo


class Controller:
    def __init__(self, validator, repo: Repo):
        self._validator = validator
        self._repo = repo
        #self._game = game

    def add_sen(self, sen):
        #self.validator.validate(sen)
        if self._repo.search_for_duplicate(sen)==0:
            raise ValueError("Duplicated sentence!")
        self._repo.add_sen(sen)

    def select_sen(self):
        return self._repo.select_sen()

    def random_sentences(self):
        sen = ["m", "e","r","g","e"," ","f","o","a","r","t","e"," ","b","i","n","e"]
        self.add_sen(sen)
        alta = ["e","s","t","e"," ","f","o","a","r","t","e"," ","f","u","n"]
        self.add_sen(alta)

    def hangman_style(self, the_sen):
        sen = []
        for i in range(len(the_sen)):
            if the_sen[i] == " ":
                sen.append(" ")
            else:
                sen.append("_")
        sen[0] =the_sen[0]
        sen[len(the_sen)-1]=the_sen[len(the_sen)-1]
        for i in range(len(the_sen)):
            if the_sen[i] == the_sen[0] or the_sen[i]==the_sen[len(the_sen)-1]:
                sen[i]=the_sen[i]
        reveal = []
        for i in range(1,len(the_sen)-1):
            if the_sen[i+1]==" " or the_sen[i-1]==" ":
                reveal.append(the_sen[i])

        for j in range(len(reveal)):
            for i in range(len(the_sen)):
                if the_sen[i]==reveal[j]:
                    sen[i]=the_sen[i]
        return sen

    def update_sen(self, the_sen, sen,l):
        ok = 0
        for i in range(len(sen)):
            if the_sen[i] == l:
                sen[i] = the_sen[i]
                ok = 1
        return sen , ok    #returns an 1 ok if there were matches in the sentence with the letter

    def update_hang(self,the_hang, hang):
        i = 0
        while hang[i]!="_" and i<len(hang)-1:
            i += 1
        if i <= len(hang)-1:
            hang[i]=the_hang[i]     #adds a new letter to the word hangman
        return hang

    def winner(self, sen, hang):
        let = 0                #how many letters are revealed
        all = 0                #how many letters are in total without spaces
        for i in range(len(sen)):
            if sen[i]!=" ":
                all += 1
                if sen[i]!="_":
                    let += 1
        if all==let:
            return "human"

        let = 0
        for i in range(len(hang)):
            if hang[i]!="_":
                let += 1
        if let == len(hang):
            return "computer"
        return None




