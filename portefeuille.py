from bourse import Bourse
from exceptions import ErreurDate, LiquiditéInsuffisante, ErreurQuantité
from datetime import date, timedelta, datetime

class Portefeuille():
    def __init__(self, montant, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()
        self.bourse = Bourse()
        self.I = {'date' : {f'{d}' : {f'montant_{d}' : montant, f'actions_{d}' : {'A' : 0, 'AAPL' : 0, 'C' : 0,
            'GOOG' : 0, 'HOG' : 0, 'HPQ' : 0, 'INTC' : 0, 'IBM' : 0, 'LUV' : 0, 'MMM' : 0, 'MSFT' : 0,
                'T' : 0, 'TGT' : 0, 'TXN' : 0, 'XOM' : 0, 'WMT' : 0}}}}

    def __interval(self, d2):
        d1 = datetime.strptime(list(self.I['date'])[-1], '%Y-%m-%d').date()
        x = self.I['date'][f'{d1}']

        for i in range((d2 - d1).days + 1):
            self.I['date'][f'{d1 + timedelta(days=i)}'] = {
                f'montant_{d1 + timedelta(days=i)}' : x[list(x)[0]], 
                    f'actions_{d1 + timedelta(days=i)}' : x[list(x)[1]]}

    def déposer(self, montant, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)

        x = self.I['date'][list(self.I['date'])[-1]]
        self.I['date'][f'{d}'] = {f'montant_{d}' : x[list(x)[0]] + montant, f'actions_{d}' : x[list(x)[1]]}

        x = self.I['date'][list(self.I['date'])[-1]][f'montant_{d}']

    def solde(self, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)
        return self.I['date'][f'{d}'][f'montant_{d}']

    def acheter(self, symbole, quantité = 0, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)
        x = self.I['date'][list(self.I['date'])[-1]]
        prix_actuel = self.bourse.prix(symbole, d)
        montant_total = prix_actuel * int(quantité)
        montant_portefeuille = self.I['date'][f'{d}'][f'montant_{d}']
        if montant_total > montant_portefeuille:
            raise LiquiditéInsuffisante()
        else:
            self.I['date'][f'{d}'] = {f'montant_{d}' : x[list(x)[0]] - montant_total, f'actions_{d}' : {'A' : x[list(x)[1]]['A'],
                'AAPL' : x[list(x)[1]]['AAPL'], 'C' : x[list(x)[1]]['C'], 'GOOG' : x[list(x)[1]]['GOOG'], 'HOG' : x[list(x)[1]]['HOG'],
                    'HPQ' : x[list(x)[1]]['HPQ'], 'INTC' : x[list(x)[1]]['INTC'], 'IBM' : x[list(x)[1]]['IBM'],
                        'LUV' : x[list(x)[1]]['LUV'], 'MMM' : x[list(x)[1]]['MMM'], 'MSFT' : x[list(x)[1]]['MSFT'],
                            'T' : x[list(x)[1]]['T'], 'TGT' : x[list(x)[1]]['TGT'], 'TXN' : x[list(x)[1]]['TXN'],
                                'XOM' : x[list(x)[1]]['XOM'], 'WMT' : x[list(x)[1]]['WMT']}}

            self.I['date'][f'{d}'][f'actions_{d}'][symbole] += quantité

    def vendre(self, symbole, quantité = 0, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)
        x = self.I['date'][list(self.I['date'])[-1]]
        prix_actuel = self.bourse.prix(symbole, d)
        montant_total = prix_actuel * int(quantité)

        if self.I['date'][f'{d}'][f'actions_{d}'][symbole] < quantité:
            raise ErreurQuantité()
        else:
            self.I['date'][f'{d}'] = {f'montant_{d}' : x[list(x)[0]] + montant_total, f'actions_{d}' : {'A' : x[list(x)[1]]['A'],
            'AAPL' : x[list(x)[1]]['AAPL'], 'C' : x[list(x)[1]]['C'], 'GOOG' : x[list(x)[1]]['GOOG'], 'HOG' : x[list(x)[1]]['HOG'],
                'HPQ' : x[list(x)[1]]['HPQ'], 'INTC' : x[list(x)[1]]['INTC'], 'IBM' : x[list(x)[1]]['IBM'],
                    'LUV' : x[list(x)[1]]['LUV'], 'MMM' : x[list(x)[1]]['MMM'], 'MSFT' : x[list(x)[1]]['MSFT'],
                        'T' : x[list(x)[1]]['T'], 'TGT' : x[list(x)[1]]['TGT'], 'TXN' : x[list(x)[1]]['TXN'],
                            'XOM' : x[list(x)[1]]['XOM'], 'WMT' : x[list(x)[1]]['WMT']}}
            
            self.I['date'][f'{d}'][f'actions_{d}'][symbole] -= quantité

    def valeur_totale(self, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)
        titres = self.titres(d)
        valeur_totale = self.I['date'][f'{d}'][f'montant_{d}']
        valeur_titres = {}
        for i in titres:
            valeur_titres[i] = self.bourse.prix(i, d)
            valeur_totale += titres[i] * valeur_titres[i]
        return valeur_totale

    def valeur_des_titres(self, symboles, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)
        valeur_totale = 0
        nombre = self.titres(d)
        symbole = {}
        for i in nombre:
            if i in symboles:
                symbole[i] = nombre[i]

        valeur_titres = {}
        for i in symbole:
            valeur_titres[i] = self.bourse.prix(i, d)
            valeur_totale += symbole[i] * valeur_titres[i]
        return valeur_totale

    def titres(self, d = None):
        if d == None:
            d = date.today()
        elif d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()

        self.__interval(d)
        x = {}
        for i in self.I['date'][f'{d}'][f'actions_{d}']:
            if self.I['date'][f'{d}'][f'actions_{d}'][i] != 0:
                x[i] = self.I['date'][f'{d}'][f'actions_{d}'][i]
        return x

    def valeur_projetée(self, rendement, d = None):
        if d == None or d == date.today():
            return "Aucun rendement à prévoir!"
        elif d - date.today() < timedelta(days=0):
            raise ErreurDate()

        de = list(self.I['date'])[-1]
        da = datetime.strptime(de, '%Y-%m-%d').date()
        titres = self.titres(da)
        valeur_totale = self.I['date'][f'{da}'][f'montant_{da}']
        différence = d - da
        y = int(différence.days/365)
        day = int(différence.days - y*365)

        if type(rendement) == type(1.0):
            valeur_totale_titres = 0
            for i in titres:
                valeur_totale_titres += self.bourse.prix(i, da) * titres[i]

            valeur_totale += valeur_totale_titres * (1 + rendement/100)**y
            valeur_totale += (day / 365) * valeur_totale_titres * (rendement/100)
            return valeur_totale

        elif type(rendement) == type({}):
            valeur_totale_titres = {}
            for i in titres:
                valeur_totale_titres[i] = self.bourse.prix(i, da) * titres[i]
                valeur_totale += valeur_totale_titres[i] * (1 + rendement[i]/100)**y
                valeur_totale += (day / 365) * valeur_totale_titres[i] * (rendement[i]/100)
            return valeur_totale
