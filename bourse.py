import json
import argparse
from datetime import timedelta, date
import requests
from exceptions import ErreurDate


class Bourse : 
    def prix(self, symbole, d):
        if d.year - date.today().year > 0 or d.month - date.today().month > 0 or d.day - date.today().day > 0:
            raise ErreurDate()
        
        if d.year - date.today().year == 0 and d.month - date.today().month == 0 and d.day - date.today().day == 0:
            hier = timedelta(days = 2)
            d -= hier

        if d.year - date.today().year == 0 and d.month - date.today().month == 0 and d.day - date.today().day == -1:
            hier = timedelta(days = 1)
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
d = date(2023, 11, 26)
print(bourse.prix('AAPL', d))