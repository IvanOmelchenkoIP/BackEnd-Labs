from backend.data.db.models.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(256), unique=True, nullable=False)
    user_currency = db.Column(
        db.Integer, db.ForeignKey("currencies.currency_id"), unique=False
    )
    user_password = db.Column(db.String, nullable=False)

    record_user = db.relationship(
        "RecordModel", back_populates="user", foreign_keys="RecordModel.user_id", lazy="dynamic"
    )
    record_currency = db.relationship(
        "RecordModel", back_populates="currency", foreign_keys="RecordModel.record_currency", lazy="dynamic"
    )
    currencies = db.relationship("CurrencyModel", back_populates="users")
