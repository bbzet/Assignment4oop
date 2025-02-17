from User import User

class UserService:
    users = {}
    @classmethod
    def add_user(cls, user:User):
        user_id = user.user_id
        cls.users[user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def __delete__(cls, user_id):
        cls.users.pop(user_id)
        return cls.users

    @classmethod
    def update_user(cls, user_id, user_update):
        user = cls.users.get(user_id)
        if user:
            user.name = user_update.name
            user.surname = user_update.surname
            user.email = user_update.email
            user.password = user_update.password
            user.birthday = user_update.birthday
            return user

        return None

    @classmethod
    def get_numbers(cls):
        return len(cls.users)



