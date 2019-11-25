from inversion_of_control.db import UserDatabase


class UserRegistration:

    def __init__(self, database: UserDatabase):
        self.db = database

    def handle_user_registration(self, event, context):
        body = event['body']

        if 'e-mail' not in body:
            raise Exception('Bad request')

        email = body['e-mail']
        user = model.User(email)

        self.db.save_user(user)

        return {
            'status_code': 200
        }
