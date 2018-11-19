from services.crawler import Crawler

from datetime import datetime

# c = Crawler()
# c.crawl("http://localhost:8080/tgnet/")

from model.website import Website
# from model.page import Page
# from model.form import Form
# from model.field import Field
# from model.constraint import Constraint
# from model.test import Test
# from model.cookie import Cookie

# Website('www.facebook.com', None).save_to_db()
# Website('www.mala.com', None).save_to_db()

# Page(1, 'www.facebook.com/rafed123', None).save_to_db()

# Form(1, 'get', '/rafed123.php').save_to_db()

# Field(1, 'input', 'name', 'Rafed').save_to_db()

# Constraint(1, 'maxlength', 20).save_to_db()

# Test(1, 'asdfsd', 'asdfad', 'asdfads', datetime.now(), 2.5, None).save_to_db()

# Cookie(1, 'session', '42342p9dn29nq293n').save_to_db()

w = Website.query.filter(Website.id==1).first()
w.delete()