from database.common.models import db, History
from database.core import crud
from site_API.core import site_api, url, headers, params

db_write = crud.create()
db_read = crud.retrieve()

fact_by_number = site_api.get_math_fact()
fact_by_date = site_api.get_date_fact()
"""
Вариант реализации функции поиск события по цифре
"""
response = fact_by_number("GET", url, headers, params, 1729, timeout=3)
response = response.json()

data = [{'number': response.get("number"), "message": response.get("text")}]
db_write(db, History, data)

# print(response)

"""
Вариант реализации функции поиск события по дате
"""
response = fact_by_date("GET", url, headers, params, 21, 6, timeout=3)
response = response.json()

data = [{'number': response.get("year"), "message": response.get("text")}]
db_write(db, History, data)

retrieved = db_read(db, History, History.number, History.message)

for element in retrieved:
    print(element.number, element.message)

# print(response)

