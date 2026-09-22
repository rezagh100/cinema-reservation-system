from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='halls')
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.cinema.name}"
    
class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=5)
    number = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Row {self.row}, Seat {self.number} - {self.hall.name}"