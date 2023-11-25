from bourse import Bourse
from exceptions import ErreurDate
from datetime import date

class Portefeuille():
    
    def __init__(self, montant, d, Actions):
        self.montant = montant
        self.bourse = Bourse()
        self.I = {'date' : {f'{d}' : {'montant_du_portefeuille' : self.montant, 'actions' : {}}}}
        for i in Actions:
            self.I['date'][f'{d}']['actions'][i] = Actions[i]
        

    def déposer(montant, d):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()
        self.montant += montant

    def afficher(self):
        print(self.I)


p = Portefeuille(2000, date(2010, 2, 20), {'AAPL' : 1, 'GOOG' : 2})
p.afficher()