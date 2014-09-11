from django.db import models
from django.utils.deconstruct import deconstructible

@deconstructible
class IgnoreFormatString(object):
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def __mod__(self, k):
        return self

class Product(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, error_messages={'invalid': IgnoreFormatString('Err, this is invalid.')})

