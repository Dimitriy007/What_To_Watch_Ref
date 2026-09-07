from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

# Разрешаем UTF-8 в JSON
app.json.ensure_ascii = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импортируем модули В КОНЦЕ файла, чтобы избежать циклических импортов
from . import cli_commands, error_handlers, models, views