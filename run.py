import os

from app import app

from routes import *

if not os.path.exists('scanf.db'):
    from database import *

if not os.path.exists('store/'):
    os.mkdir('store/')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
