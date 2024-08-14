from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user class
class User(AbstractUser):
    """User model definition"""

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        EN = ("en", "English")
        KR = ("kr", "Korean")

    class CurrencyChoices(models.TextChoices):
        CAD = "cad", "Canadian Dollar"
        USD = "usd", "Dollar"

    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    # blank=True -> make it not required
    avatar = models.ImageField(blank=True)

    is_host = models.BooleanField(default=False)

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
