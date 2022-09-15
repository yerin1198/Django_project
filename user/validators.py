from django.utils.deconstruct import deconstructible
from django.core import validators
from django.utils.translation import gettext


@deconstructible
class CustomASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = gettext(
        'Please enter a valid username. You input something wrong.'
    )
