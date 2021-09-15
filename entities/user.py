class RegisteredUserConstants:
    """Preregistered user data"""

    NAME = 'John'
    SURNAME = 'Smith'
    EMAIL = 'dr.john@gmail.com'
    PASSWORD = '123456'


class User:
    """Defines users personal data"""

    def __init__(self, name='', surname='', email='', password=''):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    @staticmethod
    def get_registered_user():
        """Returns User with preregistered personal data"""

        name = RegisteredUserConstants.NAME
        surname = RegisteredUserConstants.SURNAME
        email = RegisteredUserConstants.EMAIL
        password = RegisteredUserConstants.PASSWORD
        return User(name, surname, email, password)
