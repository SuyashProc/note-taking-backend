from tortoise import Model, fields
from tortoise.fields.relational import ReverseRelation

from .note import Note


class User(Model):
    id = fields.IntField(pk=True)

    username = fields.CharField(
        max_length=50,
        unique=True
    )

    email = fields.CharField(
        max_length=255,
        unique=True
    )

    hashed_password = fields.CharField(
        max_length=255
    )

    created_at = fields.DatetimeField(
        auto_now_add=True
    )

    notes: ReverseRelation["Note"]

    class Meta:
        table = "users"

    def __str__(self):
        return self.username