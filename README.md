# APP_spreadseets
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&&logoColor=ffffff&color=5fe620)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=5fe620)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=5fe620)](https://alembic.sqlalchemy.org/en/latest/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat&logo=Uvicorn&logoColor=ffffff&color=5fe620)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=5fe620)](https://docs.pydantic.dev/latest/)



## Приложение "Добавление товара в заказ"
Метод приложения принимает ID заказа, ID номенклатуры и количество. Если товар уже есть в заказе, его количество увеличивается, а не создавается новая позиция. Если товара нет в наличии то возвращается соответствующая ошибка.

## Технологии проекта
* Python — высокоуровневый язык программирования.
* FastAPI — веб-фреймворк для создания API, написанный на Python. FastAPI активно использует декораторы, аннотации типов и интроспекцию кода, что позволяет уменьшить количество шаблонного кода в веб-приложении.
* SQLAlchemy — Программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM.
* Alembic — библиотека для миграции к базе данных. Поддерживает возможность создания автоматических миграций на основе SqlAlchemy. Этот брокер сообщений используется в крупных приложениях для асинхронного отказоустойчивого обмена данными. Для асинхронного Python не имеет альтернатив.
* Uvicorn — реализация веб-сервера ASGI для Python. До недавнего времени в Python отсутствовал минимальный низкоуровневый интерфейс сервера / приложения для асинхронных фреймворков. Спецификация ASGI восполняет этот пробел и означает, что теперь мы можем приступить к созданию общего набора инструментов, который можно использовать во всех async-фреймворках.
* Pydantic — это библиотека Python, созданная Сэмюэлем Колвином, которая упрощает процесс проверки данных. Это универсальный инструмент, который можно использовать в различных сферах, таких как создание API, работа с базами данных и обработка данных в проектах. Библиотека имеет простой и интуитивно понятный синтаксис, позволяющий легко определять и проверять модели данных.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:usdocs/add_product_API.git
cd add_product_API
```

Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```

Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
alembic upgrade head
```

Запустить проект:
```bash
uvicorn app.main:app
```

Также запустить проект можно в контейнере:
Создать образ:
```bash
docker build -t add_product_API .
```

Запустить контейнер:
```bash
docker run -d --name add_product_API add_product_API 
```


#### Список запросов API находится в документации

Ознакомиться с функционалом и примерами можно по эндпоинту http://127.0.0.1:8000/redoc или http://127.0.0.1:8000/docs


Автор: [Балакин Андрей](https://github.com/usdocs)
