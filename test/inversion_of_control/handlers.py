import unittest

from inversion_of_control import model
from inversion_of_control.db import UserDatabase
from inversion_of_control.user_registration import UserRegistration


class StubUserDatabase(UserDatabase):

    def save_user(self, user: model.User) -> None:
        pass


class TestUserRegistration(unittest.TestCase):

    def test_register_user_bad_request(self):

        event = {
            'body': {
            }
        }
        context = {}

        user_registration = UserRegistration(StubUserDatabase())

        with self.assertRaises(Exception):
            user_registration.handle_user_registration(event, context)


if __name__ == '__main__':
    unittest.main()
