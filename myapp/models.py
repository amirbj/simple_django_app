"""
Model and manager used by the model-based activation workflow. If
you're not using that workflow, you don't need to have 'registration'
in your INSTALLED_APPS.

This is provided primarily for backwards-compatibility with existing
installations; new installs of django-registration should look into
the HMAC activation workflow in registration.backends.hmac, which also
provides a two-step process but requires no models or storage of the
activation key.

"""

import datetime
import hashlib
import re
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models, transaction
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from myapp import validators
from django.db import models


class Regform(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should take care when overriding ``save()`` to respect
    the ``commit=False`` argument, as several registration workflows
    will make use of it to create inactive user accounts.

    """
    email = forms.EmailField(
        help_text= ('email address'),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        fields = [
            User.USERNAME_FIELD,
            'email',
            'password1',
            'password2'
        ]
        required_css_class = 'required'

    def clean(self):
        """
        Apply the reserved-name validator to the username.

        """
        # This is done in clean() because Django does not currently
        # have a non-ugly way to add a validator to a field; the
        # standard approach is to re-declare the entire field in order
        # to specify the validator. That's not an option here because
        # we're dealing with the user model and we don't know -- given
        # custom users -- how to declare the username field.
        #
        # So defining clean() and attaching the error message (if
        # there is one) to the username field is the least-ugly
        # solution.
        username_value = self.cleaned_data.get(User.USERNAME_FIELD)
        if username_value is not None:
            try:
                if hasattr(self, 'reserved_names'):
                    reserved_names = self.reserved_names
                else:
                    reserved_names = validators.DEFAULT_RESERVED_NAMES
                validator = validators.ReservedNameValidator(
                    reserved_names=reserved_names
                )
                validator(username_value)
            except forms.ValidationError as v:
                self.add_error(User.USERNAME_FIELD, v)


class RegistrationFormTermsOfService(Regform):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(
        widget=forms.CheckboxInput,
        label= ('I have read and agree to the Terms of Service'),
        error_messages={
            'required': "You must agree to the terms to register",
        }
    )


class RegUniqueEmail(Regform):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.

    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(validators.DUPLICATE_EMAIL)
        return self.cleaned_data['email']
   




	































		


