"""
Example event handler for Python using imperative programming
"""
from imperative import db
from imperative import model


def handle_user_registered(event: dict, context) -> dict:
    """
    Process an event and return the result.

    The event is handled by looking up a user in the database and sends out an e-mail.
    :param event:
    :param context:
    :return:
    """
    body = event['body']

    if 'e-mail' not in body:
        raise Exception('Bad request')

    email = body['e-mail']
    user = model.User(email)

    db.save_user(user)

    return {
        'status_code': 200
    }


