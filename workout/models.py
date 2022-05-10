
from django.db import models
from PIL.Image import Image


class Exercise(models.Model):

    EXERSICE_TYPE = (
        (1, 'Pull-ups'),
        (2, 'Push-ups'),
        (3, 'Static Elements'),
        (4, 'Dynamic elements'),
        (5, 'Compound')
    )

    LEVEL = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advanced')
    )

    exercise = models.CharField(max_length=256, unique=True)
    exercise_type = models.SmallIntegerField(choices=EXERSICE_TYPE)
    level = models.SmallIntegerField(choices=LEVEL)
    description = models.TextField(max_length=1024)
    group_of_muscles = models.CharField(max_length=1024)
    image = models.ImageField()
