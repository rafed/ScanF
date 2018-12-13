
from sqlalchemy import create_engine
from datetime import datetime

from model.website import Website
from model.cookie import Cookie
from model.page import Page
from model.form import Form
from model.field import Field
from model.constraint import Constraint
from model.test import Test

from model.sql import SQLiStr
from model.xss import XssStr

DB_URI = 'sqlite:///scanf.db'
engine = create_engine(DB_URI)

# (CREATE TABLES)
# Website.__table__.create(engine)
# Cookie.__table__.create(engine)
# Page.__table__.create(engine)
# Form.__table__.create(engine)
# Field.__table__.create(engine)
# Constraint.__table__.create(engine)
# Test.__table__.create(engine)
# SQLiStr.__table__.create(engine)
XssStr.__table__.create(engine)

# (SQLi STRINGS)
# with open('data/sqli.txt') as f:
#     strings = f.readlines()

# content = [x.strip() for x in strings]
# for c in content:
#     if c and not c.startswith('#'):
#         SQLiStr(c).save_to_db()

# (XSS STRINGS)
with open('data/xss.txt') as f:
    strings = f.readlines()

content = [x.strip() for x in strings]
for c in content:
    if c:
        XssStr(c).save_to_db()