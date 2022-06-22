from ijra import ma
from ijra.models import AuthUser, ToDoAction, Category
from marshmallow_sqlalchemy import auto_field


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthUser
        fields = ["username", "email"]


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class ToDoActionSchema(ma.SQLAlchemyAutoSchema):
    # created_by = fields.Nested(UserSchema, many=True)
    created_by = auto_field(dump_only=True)
    category_id = auto_field(dump_only=True)

    class Meta:
        model = ToDoAction
        include_relationships = True
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "category_id",
            "created_by",
        ]


action_schema = ToDoActionSchema()
actions_schema = ToDoActionSchema(many=True)


class CategorySchema(ma.SQLAlchemyAutoSchema):
    owner = auto_field(dump_only=True)

    class Meta:
        model = Category
        # fields = ["__all__"]


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
