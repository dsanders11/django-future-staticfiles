#!/usr/bin/env python

"""
Test runner for reusable apps as described in the advanced testing docs:
https://docs.djangoproject.com/en/1.7/topics/testing/advanced/
"""

import os
import shutil
import sys

import django
from django.conf import settings
from django.utils import six

def run_tests():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    sys.path.insert(0, tests_dir)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
    from django.test.utils import get_runner  # To keep Django 1.6 happy
    try:  # Django 1.7+
        django.setup()
    except:
        pass
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    shutil.rmtree(six.text_type(os.environ['TMPDIR']))
    sys.exit(bool(failures))

if __name__ == "__main__":
    run_tests()