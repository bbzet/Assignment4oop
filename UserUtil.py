import random
import string
from datetime import datetime
from UserService import UserService
from User import User
import re
class UserUtil:

    @staticmethod
    def generate_user_id():
        current_year = datetime.today().year % 100
        random_number = random.randint(1000000, 9999999)
        user_id_un = f'{current_year}{random_number}'
        if user_id_un in UserService.users:
            return UserUtil.generate_user_id()
        return user_id_un

    @staticmethod
    def generate_password():
        upper_case = random.choice(string.ascii_uppercase)
        lower_case = random.choice(string.ascii_lowercase)
        digits = random.choice(string.digits)
        special_characters = random.choice(string.punctuation)

        extra_chars = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(4)]
        password = [upper_case, lower_case, digits, special_characters] + extra_chars
        random.shuffle(password)
        return ''.join(password)

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return False
        upper_case =False
        lower_case = False
        digits = False
        special_characters = False
        for char in password:
            if char.isupper():
                upper_case = True
            if char.islower():
                lower_case = True
            if char.isdigit():
                digits = True
            if char in string.punctuation:
                special_characters = True
        return upper_case and lower_case and digits and special_characters

    @staticmethod
    def generate_email(name, surname):
        return f'{name.lower()}.{surname.lower()}@domain.com'
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@domain\.com$'  # Регулярное выражение
        return bool(re.match(pattern, email))

