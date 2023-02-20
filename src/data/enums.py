from enum import Enum


class Link(Enum):
    domain: str = 'https://auto.drom.ru/'
    page_prefix: str = '/all/page'


class Brand(Enum):
    question: str = 'Enter car brand: '
    error: str = 'Invalid brand'
