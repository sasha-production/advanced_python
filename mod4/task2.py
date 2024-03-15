from typing import Optional
from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _length(form, field):
        value = len(str(field.data))

        if value < min or value > max:
            raise ValidationError(message)
    return _length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form, field):
        value = len(str(field.data))
        if value < self.min or value > self.max:
            raise ValidationError(self.message)

