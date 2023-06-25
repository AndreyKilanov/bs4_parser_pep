# Парсер документации Python и PEP
Имеет логирование, прогресс-бар. Умеет сохранять в csv-файл или выводить данные
в консоль ввиде таблицы.
Есть возможность отдельным аргументом очищать кеш перед началом работы.

Парсер имеет 4 режима работы:
*   ```whats_new``` - выдает список ссылок на версии python 
*   ```latest_versions``` - выдает список последних версий
*   ```download``` - скачивает архивом документацию последней версии
*   ```pep``` - Парсит все PEP, проверяет их статусы и считает общее кол-во.
Выводит данные в виде таблицы в офрмате csv


## Как запустить проект

>*Клонировать репозиторий и перейти в него в командной строке:*

* ```bash
    git@github.com:AndyFebruary74/bs4_parser_pep.git
  ```
* ```bash
    cd bs4_parser_pep/
  ```
>*Создать и активировать виртуальное окружение:*
* ```bash
    python -m venv venv
  ```
>*Установить зависимости и перейти в рабочую директорию:*
* ```bash
    pip install -r requirements.txt
  ```
* ```bash
    cd src/
  ```
  
### *Посмотреть help можно командой:*
* ```bash
    python main.py -h
  ```
### *Пример работы:*
>*Режим работы latest-versions:*
* ```bash
    python main.py latest-versions -o pretty
  ```
>*Вывод в консоль в виде таблицы:*
* ```
    +--------------------------------------+--------------+----------------+
    | Ссылка на документацию               | Версия       | Статус         |
    +--------------------------------------+--------------+----------------+
    | https://docs.python.org/3.13/        | 3.13         | in development |
    | https://docs.python.org/3.12/        | 3.12         | pre-release    |
    | https://docs.python.org/3.11/        | 3.11         | stable         |
    | https://docs.python.org/3.9/         | 3.9          | security-fixes |
    | https://docs.python.org/3.8/         | 3.8          | security-fixes |
    | https://docs.python.org/3.7/         | 3.7          | security-fixes |
    | https://docs.python.org/3.6/         | 3.6          | EOL            |
    | https://docs.python.org/3.5/         | 3.5          | EOL            |
    | https://docs.python.org/2.7/         | 2.7          | EOL            |
    | https://www.python.org/doc/versions/ | All versions |                |
    +--------------------------------------+--------------+----------------+

  ```