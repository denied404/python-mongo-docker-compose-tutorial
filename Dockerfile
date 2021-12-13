# В качестве базового docker образа используем официальный образ python
# на базе Debian GNU/Linux 10 (Buster)
FROM python:3.8-slim-buster

# Указываем рабочую директорию внутри docker образа
# (там будут расположены все файлы нашего проекта)
WORKDIR app/

# Копируем всё содержимое текущей папки (в которой располагается наш проект)
# в ту папку, которую мы ранее выделили как WORKDIR
COPY . .

# Устанавливаем все необходимые пакеты python из requirements.txt
RUN pip3 install -r requirements.txt

# Запускаем наше Flask приложение командой `python3 -m flask run --host=0.0.0.0`
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
