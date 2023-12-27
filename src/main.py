import os
from flask import Flask
from routes.user_routes import user_blueprint
from routes.event_routes import event_blueprint
from routes.image_routes import image_blueprint

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

app.register_blueprint(user_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(image_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
