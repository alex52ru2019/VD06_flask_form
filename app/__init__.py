from flask import Flask # импортируем Flask

app = Flask(__name__) # создаём приложение
app.config['SECRET_KEY'] = 'mysecretkey' # секретный ключ для конфиденциальности

from app import routes # импортируем файл routes из папки app