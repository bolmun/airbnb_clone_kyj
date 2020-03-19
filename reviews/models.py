from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    location = models.IntegerField()
    communication = models.IntegerField()
    check_in = models.IntegerField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.review} : {self.room}"

    def rating_average(self):
        avg = (
            self.location
            + self.communication
            + self.check_in
            + self.accuracy
            + self.cleanliness
            + self.value
        ) / 6
        return round(avg, 1)

    rating_average.short_description = "Avg."
