
'''
Test custom Django management commands
'''
# mock behavior of database

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# By adding @patch("core.management.commands.wait_for_db.Command.check")
#  as a decorator
# before your test method, you ensure that the patched_check argument
# is automatically injected
# into your test method by the decorator. This is the correct way to use @patch
# to mock the check method of the wait_for_db command for testing.
@patch("core.management.commands.wait_for_db.Command.check")
# SimpleTestCase below is imported from the above
class CommandTests(SimpleTestCase):
    # testing commands
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available"""
        patched_check.return_value = True

        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])
    # we use sleep cos we want to
    # check the database,
    # wait a few seconds and check again.

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        # the first two times we call the mocked method,
        # we raise Psycopg2OpError and
        # next 3 times we raise OperationalError,
        # 2 times and 3 times are just arbitrary value
        # the sixth times it's going to return true.
        # exception is going to check 6 times for this case
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        # This line asserts that the check method of the wait_for_db command
        # was called exactly once with the argument databases=['default'].
        # This ensures that the wait_for_db command is checking the
        #  availability
        #  of the default database during execution.
        patched_check.assert_called_with(databases=['default'])
