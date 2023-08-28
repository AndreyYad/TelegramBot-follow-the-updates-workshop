'''
Модуль с функциями использующие регулярные выражения
'''

from re import search

async def search_id(text):
    pattern = '\?id=\d+'
    search_ = search(pattern, text)
    if search_ != None:
        search_ = int(search_[0].replace('?id=', ''))
    return search_

if __name__ == '__main__':
    pass