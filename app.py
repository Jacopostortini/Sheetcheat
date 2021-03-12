
from datetime import timedelta


from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_uploads import configure_uploads, patch_request_class
from dotenv import load_dotenv

from resources.register import Register
from resources.authenticate import UserLogin, TokenRefresh
from resources.save_image import ImageUpload
from flask import render_template
from db import db
from flask_uploads import configure_uploads, patch_request_class
#from resources.createclass import CreateClass
#from resources.joinclass import JoinClass
from libs.image_helper import IMAGE_SET


app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")  # load default configs from default_config.py
app.config.from_envvar(
    "APPLICATION_SETTINGS"
)  # override with config.py (APPLICATION_SETTINGS points to config.py)
patch_request_class(app, 10 * 1024 * 1024)  # restrict max upload image size to 10MB
configure_uploads(app, IMAGE_SET)
api = Api(app)

jwt = JWTManager(app)

# app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)

#app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(weeks=100)

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup_page.html')
def get():
    return render_template('signup_page.html')

api.add_resource(Register, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh_token")
api.add_resource(ImageUpload, "/image_upload")

#api.add_resource(CreateClass, "/class/create")
#api.add_resource(JoinClass, "/class/join")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
