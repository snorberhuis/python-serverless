import unittest
from unittest import mock

import imperative
import imperative.db
import imperative.handlers
from imperative import db, handlers
from imperative.handlers import handle_user_registered


# Let's test the function handling a bad request.
class TestHandleUserRegistered(unittest.TestCase):

    def test_missing_email(self):
        event = {
            'body': {
            }
        }
        context = {}

        with self.assertRaises(Exception):
            handle_user_registered(event, context)


# It is a bit more complicated,
# because I need to mock the database call.
class TestHandleUserRegisteredMock(unittest.TestCase):

    @mock.patch('imperative.handlers.db.save_user', None)
    def test_missing_email(self):
        event = {
            'body': {
            }
        }
        context = {}

        with self.assertRaises(Exception):
            handlers.handle_user_registered(event, context)


# Can I not just ignore it as I will be mocking it?
class TestHandleUserRegisteredSetUp(unittest.TestCase):

    def setUp(self) -> None:
        db.client = None

    @mock.patch('imperative.handlers.db.save_user', None)
    def test_missing_email(self):
        event = {
            'body': {
            }
        }
        context = {}

        with self.assertRaises(Exception):
            handlers.handle_user_registered(event, context)


# I just need to mock the function inside the other module.
class TestHandleUserRegisteredMockBoto3(unittest.TestCase):

    @mock.patch('imperative.handlers.db.save_user', None)
    @mock.patch('imperative.db.boto3.resource', None)
    def test_missing_email(self):
        event = {
            'body': {
            }
        }
        context = {}

        with self.assertRaises(Exception):
            handlers.handle_user_registered(event, context)


if __name__ == '__main__':
    unittest.main()
