from Report import Report as r




class Transaction:
    debit, credit = '', ''
    value, units = 0, ''
    name = ''
    def __init__(self, debit:str, credit:str, value:float, units:str, name:str):
        self.debit, self.credit, self.value, self.units = debit, credit, value, units
        self.name = name
    def send(self, debit:str, credit:str, value:float, units:str, name:str):
        pass
    
