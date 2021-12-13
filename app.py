from flask import Flask
from flask import request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import os

# Инициализация Flask-приложения
app = Flask(__name__)

# Адрес хоста и порт берутся из переменных окружения MONGO_HOST и MONGO_PORT соответственно.
# Если они не заданы - используются значения по-умолчанию.
mongodb_host = os.environ.get('MONGO_HOST', 'mongo')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))

# Инициализация клиента MongoDB
client = MongoClient(mongodb_host, mongodb_port)

# Инициализация БД внутри MongoDB сервера (если хранилища с таким именем не существует,
# оно будет создано)
db = client['todo']

# Инициализация коллекции внутри БД `todo` (если коллекции с таким именем не существует,
# она будет создана)
collection = db['todos']


# http://localhost:5000/
# Method: GET
# Возвращает все todo задачи которые не отмечены как выполненные
@app.route("/")
def root():
    return dumps(collection.find({"done": "no"}))


# http://localhost:5000/all
# Method: GET
# Возвращает все todo задачи
@app.route("/all")
def all():
    return dumps(collection.find())


# http://localhost:5000/completed
# Method: GET
# Возвращает все todo задачи которые отмечены как выполненные
@app.route("/completed")
def completed():
    return dumps(collection.find({"done": "yes"}))

# http://localhost:5000/search_by_name?name=...
# Method: GET
# Возвращает все todo задачи с заданным именем
@app.route("/search_by_name")
def search_by_name():
    name = request.values.get("name")
    return dumps(collection.find({"name": name}))


# http://localhost:5000/mark_as_done?_id=...
# Method: GET
# Принимает параметр _id, помечает соответствующую todo карточку как выполненную
@app.route("/mark_as_done")
def mark_as_done():
    todo_id = request.values.get("_id")
    collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"done": "yes"}})
    return redirect("/")


# http://localhost:5000/add
# Method: POST
# Принимает параметры name, desc, date и создаёт новую todo карточку помеченную как невыполненная
@app.route("/add", methods=['POST'])
def add():
    name = request.values.get("name")
    desc = request.values.get("desc")
    date = request.values.get("date")
    collection.insert_one({
        "name": name,
        "desc": desc,
        "date": date,
        "done": "no"
    })
    return redirect("/list")


# http://localhost:5000/delete?_id=...
# Method: GET
# Принимает параметр _id, удаляет соответствующую todo карточку из коллекции
@app.route("/delete")
def remove():
    key = request.values.get("_id")
    collection.delete_one({"_id": ObjectId(key)})
    return redirect("/")
