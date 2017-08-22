import requests
from bs4 import BeautifulSoup

from app import db
from app.models import Food


def get_products_from_tables():
    r = requests.get('http://www.freshfactory.ua/calories_table')
    soup = BeautifulSoup(r.content, 'lxml')

    data = []
    tables = soup.find_all('table', attrs={'class': 'nutritive_value'})
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                cols = [element.text.strip() for element in cols]
                data.append(Food(
                    name=cols[0],
                    protein=round(float(cols[1].replace(',', '.'))/100, 3),
                    fat=round(float(cols[2].replace(',', '.'))/100, 3),
                    carbohydrate=round(float(cols[3].replace(',', '.'))/100, 3),
                    calories=round(float(cols[4].replace(',', '.'))/100, 3),
                    type_of_food='I don\'t know yet...'
                ))
    return data
