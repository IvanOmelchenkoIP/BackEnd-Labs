import uuid

from backend.utils.utils import select


class UsersStorage:
    def __init__(self):
        self.users = []

    def add(self, user_data):
        user = {
            "user_id": uuid.uuid4().int,
            **user_data
        }
        self.users.append(user)
        return user

    def get_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        return select(self.users, "user_id", user_id)

    def get_user_by_name(self, user_name):
        return select(self.users, "user_name", user_name)

    def set_user_currency(self, user_id, user_currency):
        selected = select(self.users, "user_id", user_id)
        if not selected:
            return None
        selected[0]["user_currency"] = user_currency
        return selected
