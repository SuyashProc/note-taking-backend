from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "notes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "owner_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmF1v2jAUhv9K5KtOYhNlpa24Syldu7YwlWyrOk2WSQ4hamJT2xlFHf99svMdCIOp7Q"
    "bjLjkf8clznPi1n1DAHPDFuy6TgFrGE6IkUBcFe81AZDzOrMogycDXgZRJ0BYyEJITW6KW"
    "MSS+gJqBHBA298bSYxS1DBr6vjIyW0juUTczhdR7CAFL5oIcAUct49v3moE86sAjiOR2fI"
    "+HHvhOoU7PUWNrO5bTsbZdUHmmA9VoA2wzPwxoFjyeyhGjabRHpbK6QIETCerxkoeqfFVd"
    "/JrJG0WVZiFRibkcB4Yk9GXudQc4syGMuz0L9zsWxmgNQDajCq5HpaLxhFxVwtvG/sHRwf"
    "H7w4PjmoF0manlaBYNnYGJEjWeroVm2k8kiSI04wyq9KQP81zbI8IXg00TSmyF5GW2Ccll"
    "cBNDRjebUa+BNyCP2AfqypFi2mwugfnFvGmfmzd7jWbzjRqScWJHH0Y3djUinyKeEbYZlR"
    "BNvCJjCx4rJm8uZSsoL4FqdW4t9eRAiAc/z3Lv2rzVmINp7LnqdT8k4Tn27aveSRk5BwUH"
    "kwXUT4kE6QVQQb6QWYLvxKnvkosNbAXiQJwe9afxf2xZay6uO33LvP5U6M+paXWUp1HoTW"
    "LdOyx9GulDjK8X1rmhbo27Xrej8TIhXa5HzOKsO6RqIqFkmLIJJk7ul5tYE2qFrodj5w+7"
    "Xszcdf1f6XrCKNf2uPqs62xCgeO1tEE+5fcKYRPa+wwiQcmu4f1CjaB5zfM9Yxw8l17CVG"
    "O+oEISai/SBrHC/Cyix2wY3RhdZs3+R5xMUqFamFaMYgd80Eobtc1+2zztIM14QOz7CeEO"
    "LsBWHtZgJUsaO+8KGkHZQihxNR31GqroPPYFgj9pR7XgDwXwneDfLsGveqqv19D8+ZznEa"
    "R/F3FB9DfrK2j+Zr1S8itXUX5CQDx/Hb5pwtbBfZEd1YiIETh4TISYMO6sQ3pB6lbssF5j"
    "H7vbVP0nm6o5KVitW7LpkR4OFmfGSZx2dnkDPtFgK/VhcgK5Jfpw9pKizgTu2aNFsi72LB"
    "V2JIvZKbttUXY/gIv4+1p1Ocyl7JbB1ZZB9VGtQTgO30K6+/VVhPN+vVo5a9+Kh+Uf+73u"
    "uofljmdL46fhe2ITD3Vm1XAVjOWH5uXz8ZIwUA9Qh+ZrrPTPv5jNfgEvBh8A"
)
