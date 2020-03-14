from django.db import models
from core import models as core_models
from users import models as user_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    location = models.IntegerField()
    communication = models.IntegerField()
    check_in = models.IntegerField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
