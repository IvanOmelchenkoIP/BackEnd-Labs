from sqlalchemy import func
from backend.models.db import db

class CurrencyModel(db.Model):
    __tablename__ = "currencies"

    currency_id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(128), unique=True, nullable=False)
