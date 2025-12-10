from flask import Flask
from routes.home import home_route
from routes.library import library_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(library_route, url_prefix='/library')

if __name__ == "__main__":
    app.run(debug=True)