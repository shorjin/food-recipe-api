"""
Django command to wait for the database to be available
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import ConnectionHandler, OperationalError


class Command(BaseCommand):
    """Django command to pause execution until the database is available"""

    def handle(self, *args, **options):
        """Entrypoint for the command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        db_conn = ConnectionHandler()
        # the loop will continue running as long as db_up is False.
        while not db_up:
            try:
                # Use the 'default' database alias
                db_conn['default'].ensure_connection()
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
