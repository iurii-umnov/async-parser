# Asynchronous parser for [Drom.ru] 🏎

## Description

This parser allows you to parse all the available cars under provided brand from one of the most popular websites for
car sales in Russia.

## Features

- Asynchronous parsing
- Logic with error handling on reading html page elements
- Determining the maximum number of pages available
- Object-Oriented structure of the parsing logic

## Tech

Parser uses a number of open source projects to work properly:

- [Python] - the main language
- [aiohttp] - asynchronous connection and requests
- [asyncio] - parallel computing (parsing)
- [BeautifulSoup] - html pages/elements parsing


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

  [Drom.ru]: <https://www.drom.ru/>
  [Python]: <https://www.python.org/>
  [aiohttp]: <https://docs.aiohttp.org/en/stable/>
  [asyncio]: <https://docs.python.org/3/library/asyncio.html>
  [BeautifulSoup]: <https://beautiful-soup-4.readthedocs.io/en/latest/>