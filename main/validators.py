from django.core.exceptions import ValidationError
import re


def validate_item_name(value):
    p = re.compile('^[a-zA-Z0-9][ a-zA-Z0-9-]*[a-zA-Z0-9]$')
    if not p.match(value):
        raise ValidationError("A valid item name must be entered in")
    else:
        return value
