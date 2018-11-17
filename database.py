
from sqlalchemy import create_engine
from datetime import datetime

from model.website import Website
from model.cookie import Cookie
from model.page import Page
from model.form import Form
from model.field import Field
from model.constraint import Constraint
from model.test import Test

DB_URI = 'sqlite:///scanf.db'
engine = create_engine(DB_URI)

# (CREATE TABLES)
Website.__table__.create(engine)
Cookie.__table__.create(engine)
Page.__table__.create(engine)
Form.__table__.create(engine)
Field.__table__.create(engine)
Constraint.__table__.create(engine)
Test.__table__.create(engine)
