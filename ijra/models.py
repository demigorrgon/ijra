from ijra import db, bcrypt
import datetime


class AuthUser(db.Model):
    __tablename__ = "auth_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode("UTF-8")

    def check_password(self, password_to_check):
        return bcrypt.check_password_hash(self.password, password_to_check)

    def __repr__(self):
        return self.username


class ToDoAction(db.Model):
    __tablename__ = "ToDoAction"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    created_by = db.Column(
        db.String, db.ForeignKey("auth_user.username"), nullable=False
    )


class Category(db.Model):
    # TODO: add many-to-many relationship with todoaction in order to dynamically fill table in frontend
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner = db.Column(db.String, db.ForeignKey("auth_user.username"), nullable=False)
    actions = db.relationship("ToDoAction", backref="category")
