'''
Модуль для получения данных о работе Steam Workshop'а
'''

from requests import get
from bs4 import BeautifulSoup

from asyncio import run

URL_TEMPLATES = {
    'main' : 'https://steamcommunity.com/workshop/filedetails/?id={}',
    'updates' : 'https://steamcommunity.com/sharedfiles/filedetails/changelog/{}'
}

async def get_name_work(work_id):
    url = URL_TEMPLATES['main'].format(work_id)
    page = get(url)
    if page.status_code != 200:
        print(f'{page.status_code}: Что то не так - {url}')
    else:
        soup = BeautifulSoup(page.text, "html.parser")
        search = soup.find('div', class_='workshopItemTitle')
        if search != None:
            return search.text

if __name__ == '__main__':
    work_id = 2076426030
    print(run(get_name_work(work_id)))