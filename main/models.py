import sqlalchemy
from sqlalchemy import DateTime, Enum

from main.constants import UserStatus, IncomeStatus, ExpenseStatus, PlanStatus, SuggestionStatus, IncomeNotif, \
    ExpenseNotif
from main.database import metadata

Users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_id", sqlalchemy.Integer),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("country", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("city", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("district", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("village", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", Enum(UserStatus), default=UserStatus.inactive),
    sqlalchemy.Column("income_notif", Enum(IncomeNotif), default=IncomeNotif.off),
    sqlalchemy.Column("expense_notif", Enum(ExpenseNotif), default=ExpenseNotif.on),
    sqlalchemy.Column('created_at', DateTime(timezone=True)),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)

Income = sqlalchemy.Table(
    "income",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("source", sqlalchemy.String),
    sqlalchemy.Column("amount", sqlalchemy.Float),
    sqlalchemy.Column("status", Enum(IncomeStatus), default=IncomeStatus.active),
    sqlalchemy.Column('created_at', DateTime(timezone=True)),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True),

    sqlalchemy.Column("telegram_id", sqlalchemy.Integer)
)

Expense = sqlalchemy.Table(
    "expense",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("reason", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
    sqlalchemy.Column("status", Enum(ExpenseStatus), default=ExpenseStatus.active),
    sqlalchemy.Column('created_at', DateTime(timezone=True)),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True),

    sqlalchemy.Column("telegram_id", sqlalchemy.Integer)
)

Plans = sqlalchemy.Table(
    "plans",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.String),
    sqlalchemy.Column("time", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", Enum(PlanStatus), default=PlanStatus.active),
    sqlalchemy.Column('created_at', DateTime(timezone=True)),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True),

    sqlalchemy.Column("telegram_id", sqlalchemy.Integer)
)

Suggestions = sqlalchemy.Table(
    "suggestions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("feedback", sqlalchemy.String),
    sqlalchemy.Column("status", Enum(SuggestionStatus), default=SuggestionStatus.active),
    sqlalchemy.Column('created_at', DateTime(timezone=True)),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True),

    sqlalchemy.Column("telegram_id", sqlalchemy.Integer)
)
