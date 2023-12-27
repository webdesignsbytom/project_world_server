from flask import Flask
from routes.user_routes import user_blueprint
from routes.event_routes import event_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(event_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
