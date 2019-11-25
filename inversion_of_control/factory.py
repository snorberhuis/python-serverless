from inversion_of_control.db import UserDynamoDB, UserDatabase
from inversion_of_control.user_registration import UserRegistration


def get_user_database() -> UserDatabase:
    return UserDynamoDB()


def get_user_registration() -> UserRegistration:
    """
    construct a UserRegistration
    :return:
    """
    database = get_user_database()

    return UserRegistration(database)