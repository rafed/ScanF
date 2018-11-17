from app import app

# from routes.test_routes import *
# from routes.static_files_routes import *
# from routes.website_routes import *

from routes import *

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
