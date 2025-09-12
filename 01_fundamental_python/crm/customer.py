import re


class Customer:
    def __init__(self, c_id, name, age='None', phone='None', email='None'):
        self.c_id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod
    def check_id(c_id):
        return c_id.isdigit()

    @staticmethod
    def check_name(name):
        return name.isalpha()

    @staticmethod
    def check_age(age):
        return age.isdigit()

    @staticmethod
    def check_phone(phone):
        return True if re.match(r"^1[345789]\d{9}$", phone) else False

    @staticmethod
    def check_email(email):
        pattern = r"[\w!#$%&'*+-/=?^`{|}~.]+@[\w!#$%&'*+-/=?^`{|}~.]+\.[a-zA-Z]{2,}$"
        return True if re.match(pattern, email) else False

    def __str__(self):
        return (f"Id: {self.c_id:<5}, Name: {self.name:<10}, Age: {self.age:<5}, Phone: {self.phone:<15}"
                f", Email: {self.email:<25}")
