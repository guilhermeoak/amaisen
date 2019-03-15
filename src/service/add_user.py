from src.model.user import User
from src.util import connection as con
import getpass


class AddUser:

    def __init__(self):
        print('\nNew user registration\n')

        name = str(input('Name: '))
        last_name = str(input('Last name: '))
        tp = str(input('Type of account[admin or common user]: '))
        login = str(input('Login: '))
        password = getpass.getpass(prompt='Password: ')
        email = str(input('Email: '))

        new_user = User(name, last_name, tp, email, login, password)

        query = (
                "INSERT INTO USER (TYPE, LOGIN, PASSWORD, NAME, LASTNAME, EMAIL) VALUES('%s', '%s','%s', '%s', '%s', "
                "'%s')" %
                (str(new_user.tp), str(new_user.login), str(new_user.password), str(new_user.name),
                 str(new_user.last_name), str(new_user.email)))

        con.insert_data(query)
