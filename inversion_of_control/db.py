from abc import ABC, abstractmethod

import boto3

from inversion_of_control import model


class UserDatabase(ABC):

    @abstractmethod
    def save_user(self, user: model.User):
        """
        saves a user to the database.

        :param user: The user to be saved
        :return:
        """


class UserDynamoDB(UserDatabase):

    def __init__(self):
        self.table = boto3.resource('dynamodb').Table('users')

    def save_user(self, user: model.User):
        self.table.put_item(
            Item={
                'email': user.email
            }
        )


