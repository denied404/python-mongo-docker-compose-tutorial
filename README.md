# Пример использования Mongo DB в python приложении с [docker-compose](https://docs.docker.com/compose/) конфигурацией

## Краткая информация о проекте
Данный проект является простейшей реализацией бэкенда для приложения TODO-List: приложения, в котором можно создавать, редактировать и удалять TODO карточки.
Проект создан с помощью простого и интуитивного веб-фреймворка для python под названием [Flask](https://flask.palletsprojects.com/en/2.0.x/). Весь проект состоит из одного файла `app.py`, в котором описаны основные endpoints: для вывода полного списка карточек, для вывода только тех карточек, которые ещё не выполнены, и так далее. Также внутри `app.py` находится код инициализации клиента для MongoDB.

### requirements.yml
Данный файл содержит описание [pip](https://pypi.org/project/pip/) пакетов, необходимых для запуска нашего Flask приложения

### Dockerfile
Данный проект включает в себя [Dockerfile](https://docs.docker.com/engine/reference/builder/) - набор инструкций описывающих docker-образ для нашего Flask приложения

### docker-compose.yml
Данный файл содержит описание конфигурации [docker-compose](https://docs.docker.com/compose/). По сути, это описание всех сервисов, которые необходимы для полноценного функционирования нашего приложения и будут запущены в отдельных docker-контейнерах

## Некоторые сведения о docker и docker-compose
Тут я собрал некоторые статьи, которые помогут вам постичь основы того, чем являются docker контейнеры и образы, и чем они не являются:
- [Что такое Docker: простыми словами о контейнеризации](https://blog.ithillel.ua/articles/chto-takoe-docker-prostymi-slovami-o-konteynerizatsii)
- [Docker-tutorial для новичков. Изучаем докер так, если бы он был игровой приставкой](https://badcode.ru/docker-tutorial-dlia-novichkov-rassmatrivaiem-docker-tak-iesli-by-on-byl-ighrovoi-pristavkoi/)
- [Руководство по docker-compose для начинающих](https://habr.com/ru/company/ruvds/blog/450312/)

Разумеется, основным источником информации является официальная документация по docker и docker-compose, ссылки на которую уже содержатся выше в описании данного проекта
