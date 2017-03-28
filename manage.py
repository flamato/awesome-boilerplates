#!/usr/bin/env python

import os
import sys

import environ

env = environ.Env()
environ.Env.read_env()


if __name__ == "__main__":
    settings_module = env('DJANGO_SETTINGS_MODULE')

    if sys.argv[1] == 'test':
        if settings_module:
            print("Ignoring config('DJANGO_SETTINGS_MODULE') because it's test. "
                  "Using 'settings.test'")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.test")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
