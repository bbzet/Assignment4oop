from datetime import datetime

class User:
    def __init__(self, user_id:int, name:str, surname:str, email:str, passsword:str, birthday:datetime):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = passsword
        self.birthday = datetime.strptime(birthday, "%d%m%Y")

    def get_details(self):
        return f'User id: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Birthday: {self.birthday.strftime("%d-%m-%Y")}'

    def get_age(self):
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))