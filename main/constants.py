from enum import Enum


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class IncomeStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class ExpenseStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class PlanStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class SuggestionStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class IncomeNotif(str, Enum):
    on = "on"
    off = "off"


class ExpenseNotif(str, Enum):
    on = "on"
    off = "off"
