#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    os.environ.setdefault('DJANGO_SUPERUSER_USERNAME', 'admin')
    os.environ.setdefault('DJANGO_SUPERUSER_EMAIL', 'admin@admin.admin')
    os.environ.setdefault('DJANGO_SUPERUSER_PASSWORD', 'admin')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        execute_from_command_line(sys.argv)
    except:
        if sys.argv[1] == 'createsuperuser':
            pass
        else:
            time.sleep(3)
            main()


if __name__ == '__main__':
    main()
