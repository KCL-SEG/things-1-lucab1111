from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Thing(AbstractUser):
    name = models.CharField(
        blank=False,
        max_length=30,
        unique=True,
    )

    description = models.CharField(
        blank=False,
        max_length=120,
        unique=False,
    )

    quantity = models.IntegerField(
        unique=False,
        validators=[
            MinLengthValidator(0, message="Please enter a number between 0 and 100"),
            MaxLengthValidator(100, message="Please enter a number between 0 and 100"),
        ],
    )
