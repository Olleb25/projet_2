import json
import argparse
from datetime import timedelta, date
import requests
from exceptions import ErreurDate


class Bourse : 
    def prix(self, symbole, d):
        auj = date.today()
        if d.year - auj.year > 0 or d.month - auj.month > 0 or d.day - auj.day > 0:
            raise ErreurDate()
        
        if d.year - auj.year == 0 and d.month - auj.month == 0 and d.day - auj.day == 0:
            hier = timedelta(days = 3)
            d -= hier

        if d.weekday() == 5:
            vendredi = timedelta(days = 1)
            d -= vendredi

        if d.weekday() == 6:
            vendredi = timedelta(days= 2)
            d -= vendredi 
        

        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
        params = {'début' : d, 'fin' : d}
        reponse = requests.get(url=url, params=params)
        reponse = json.loads(reponse.text)
        return reponse['historique'][d.strftime('%Y-%m-%d')]['fermeture']


bourse = Bourse()
d = date(2023, 11, 25)
print(bourse.prix('AAPL', d))