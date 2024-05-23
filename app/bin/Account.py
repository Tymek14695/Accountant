#necessary libraries
from random import randint
from Report import Report as r
 



class Account:
    #account data
    serie, number, tail = '', '', ''
    id = ''



    #constructor
    def __init__(self):
        r(self)

        #generating serie
        self.serie += ord(randint(65, 91))
        self.serie += ord(randint(65, 91))

        #generating number
        self.number = randint(10000, 100000)

        #generating tail
        self.tail += ord(randint(65, 91))
        self.tail += ord(randint(65, 91))
        self.tail += ord(randint(65, 91))

        #id = [serie][number][tail]
        self.id = self.serie + self.number + self.tail
    

    