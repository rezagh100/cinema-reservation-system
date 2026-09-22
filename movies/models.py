from django.db import models



class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    age_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    