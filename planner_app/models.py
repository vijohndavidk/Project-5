from django.db import models
from django.contrib.auth.models import User

   


class Subject(models.Model):

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name=models.CharField(
        max_length=100
    )

    hours=models.IntegerField()

    streak=models.IntegerField(
default=0
)

    completed=models.IntegerField(
        default=0
    )



class Timetable(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    plan = models.TextField()


class Progress(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    percentage = models.IntegerField(
        default=0
    )


