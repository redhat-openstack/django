"""
Django Unit Test and Doctest framework.
"""

from django.test.client import Client, RequestFactory
from django.test.testcases import (TestCase, TransactionTestCase,
    SimpleTestCase, LiveServerTestCase, skipIfDBFeature,
    skipUnlessDBFeature
)
from django.test.utils import Approximate

# To simplify Django's test suite; not meant as a public API
try:
    from unittest import mock  # NOQA
except ImportError:
    try:
        import mock  # NOQA
    except ImportError:
        pass
