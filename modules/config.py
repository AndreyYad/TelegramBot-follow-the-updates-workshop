'''Возвращение значений конфига'''

from json import load

with open('config.json') as file:
    config = load(file)

TOKEN = config.get('token')