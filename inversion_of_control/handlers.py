"""
Example event handler for Python using imperative programming
"""
from inversion_of_control.factory import get_user_registration


def handle_user_registered(event: dict, context) -> dict:
    """
    Process an event and return the result.

    The event is handled by looking up a user in the database and sends out an e-mail.
    :param event:
    :param context:
    :return:
    """
    user_registration = get_user_registration()
    return user_registration.handle_user_registration(event, context)
