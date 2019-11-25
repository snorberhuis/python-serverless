import boto3

from imperative import model

table = boto3.resource('dynamodb').Table('users')


def save_user(user: model.User) -> None:
    """
    saves a user to dynamodb.
    :param user: The user to be saved
    :return: 
    """
    table.put_item(
        Item={
            'email': user.email
        }
    )
