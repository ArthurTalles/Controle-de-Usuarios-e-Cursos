from flask_migrate import Migrate
from .db import db

migrate = Migrate(db=db)