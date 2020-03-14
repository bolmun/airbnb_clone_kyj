from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    GENDER_FEMALE = "Female"
    GENDER_MALE = "Male"
    GENDER_OTHERS = "Others"

    GENDER_CHOICES = (
        (GENDER_FEMALE, "Female"),
        (GENDER_MALE, "Male"),
        (GENDER_OTHERS, "Others"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    LANGUAGE_ENG = "english"
    LANGUAGE_KOR = "korean"

    LANGUAGE_CHOICES = ((LANGUAGE_ENG, "English"), (LANGUAGE_KOR, "한국어"))

    bio = models.TextField(default="", blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES, blank=True)
    superhost = models.BooleanField(default=False)
