class Question:
    def __init__(self, question, a1, a2, a3, a4, nca):
        self.question = question
        self. a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.nca = nca
    def __str__(self):
        emptystring = ""
        emptystring += str(self.question)
        emptystring += ("\n 1. " + self.a1)
        emptystring += ("\n 2. " + self.a2)
        emptystring += ("\n 3. " + self.a3)
        emptystring += ("\n 4. " + self.a4)
        return emptystring
    def getCorrectAnswer(self):
        return self.nca

