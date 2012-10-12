=====================
django_localflavor_ch
=====================

Country-specific Django helpers for Switzerland.

What's in the Switzerland localflavor?
======================================

* forms.CHIdentityCardNumberField: A form field that validates input as a
  Swiss identity card number. A valid number must confirm to the X1234567<0
  or 1234567890 format and have the correct checksums.

* forms.CHPhoneNumberField: A form field that validates input as a Swiss phone
  number. The correct format is 0XX XXX XX XX. 0XX.XXX.XX.XX and 0XXXXXXXXX
  validate but are corrected to 0XX XXX XX XX.

* forms.CHZipCodeField: A form field that validates input as a Swiss zip code.
  Valid codes consist of four digits.

* forms.CHStateSelect: A ``Select`` widget that uses a list of Swiss states as
  its choices.

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
