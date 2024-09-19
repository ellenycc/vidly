from django.db import models
from django.utils import timezone


class Genre(models.Model):
    # genre name limit to 255 char to prevent security attack
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # link movie with genre, pass Genre class and a keyword argument: on_delete - when a genre is deleted, all th movies related deleted (cascading)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    release_year = models.IntegerField(default=2000)
