"""
Create Retrieve Update Delete
Создать Получить(считать) Обновить Удалить

TypeVar - пользовательский тип данных для аннотаций типа. Проходили в курсе.
T = TypeVar("T") это может быть все что угодно
S = TypeVar("S") это подкласс какого-то класса
L = TypeVar("L") это точное совпадение один в один
"""
from typing import Dict, List, TypeVar

from peewee import ModelSelect

from ..common.models import db, ModelBase

T = TypeVar("T")

def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    """
    Операция записи
    скрываем параметр установкой _ перед названием!
    :param call:
    :return
    :argument db - база данных из database\common\models
    :argument model: модель с которой будем работать. В нашем случае это class History
    :argument *data: передаваемые данные в виде списка со словарем
    """
    with db.atomic():
        model.insert.many(*data).execute()

def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)

    return response

class CRUDInterface():
    """
    Делаем интерфейс наружу.
    """
    @staticmethod
    def create():
        return _store_date

    def retrieve(self):
        return _retrieve_all_data

if __name__ == '__main__':
    _store_date()
    _retrieve_data_all_data()
    CRUDInterface()