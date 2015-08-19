A Word About This Django Fork
=============================

This is an unofficial fork of Django_, which focuses entirely on backporting
official, publicly-announced security fixes to Django 1.6.11. It does not
contain any other bug fixes or features, and any branches other than
``security-backports/1.6.x`` are unlikely to be up-to-date.

Django 1.6.x is the last release cycle of Django to support Python 2.6, but
both Django 1.6.x and Python 2.6.x are no longer officially supported by
either project, and will no longer be receiving any official security fixes.

We recognize that many organizations and products are still tied to these
releases, which is why we've built this fork. However, we *strongly* recommend
that you use modern, official versions of both Django and Python, if at all
possible.

We're not guaranteeing long-term support on this codebase. We're maintaining
this for `Review Board`_ customers so long as we support the versions
currently using Django 1.6.x.

We're also not actively looking for new security vulnerabilities. If you find
a new vulnerability in this release, check to be sure it does not apply to any
other versions currently supported by the Django project.

.. _Django: https://www.djangoproject.com/
.. _`Review Board`: https://www.reviewboard.org/


Downloads
---------

All security backport releases will be posted to our `downloads page`_. They
are not available via PyPI.


Reporting Bugs
--------------

If you hit any bugs with this release, please verify whether they still occur
with the official Django 1.6.11 release, or ideally, the latest supported
version.

If they're absolutely upstream Django bugs, you can file it against the
`Django bug tracker`_. However, if they're our problem, please file it against
`our bug tracker`_.

.. _`downloads page`: http://downloads.reviewboard.org/releases/Django/1.6/
.. _`Django bug tracker`: https://code.djangoproject.com/newticket
.. _`our bug tracker`: https://www.reviewboard.org/bugs/new/


About Django
------------

*(The following is the official information about Django itself. Please
remember not to bother them about anything related to this fork.)*

Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "docs" directory and online at
http://docs.djangoproject.com/en/dev/. If you're just getting started, here's
how we recommend you read the docs:

* First, read docs/intro/install.txt for instructions on installing Django.

* Next, work through the tutorials in order (docs/intro/tutorial01.txt,
  docs/intro/tutorial02.txt, etc.).

* If you want to set up an actual deployment server, read
  docs/howto/deployment/index.txt for instructions.

* You'll probably want to read through the topical guides (in docs/topics)
  next; from there you can jump to the HOWTOs (in docs/howto) for specific
  problems, and check out the reference (docs/ref) for gory details.

* See docs/README for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think they
should be clarified in any way, please take 30 seconds to fill out a ticket
here:

http://code.djangoproject.com/newticket

To get more help:

* Join the #django channel on irc.freenode.net. Lots of helpful people hang out
  there. Read the archives at http://django-irc-logs.com/.

* Join the django-users mailing list, or read the archives, at
  http://groups.google.com/group/django-users.

To contribute to Django:

* Check out http://www.djangoproject.com/community/ for information about
  getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  docs/internals/contributing/writing-code/unit-tests.txt, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests
