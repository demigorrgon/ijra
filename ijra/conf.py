# import os

# from dotenv import load_dotenv
# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
# from flask_bcrypt import Bcrypt
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS

# load_dotenv()

# app = Flask(__name__)
# ma = Marshmallow(app)
# cors = CORS(app)
# app.config["CORS_HEADERS"] = "Content-Type"
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URI")
# app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# bcrypt = Bcrypt(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# jwt = JWTManager(app)
