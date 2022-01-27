import sqlalchemy
from sqlalchemy import DateTime, Enum

from main.constants import UserStatus
from main.database import metadata

Users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_id", sqlalchemy.Integer),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("country", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("city", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("district", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("village", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String),
    sqlalchemy.Column("status", Enum(UserStatus), default=UserStatus.inactive),
    sqlalchemy.Column('created_at', DateTime(timezone=True)),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)