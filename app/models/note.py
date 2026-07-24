from tortoise import Model, fields


class Note(Model):
    id = fields.IntField(pk=True)

    title = fields.CharField(max_length=255)

    content = fields.TextField()

    owner = fields.ForeignKeyField(
        "models.User",
        related_name="notes"
    )

    created_at = fields.DatetimeField(auto_now_add=True)

    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "notes"

    def __str__(self):
        return self.title