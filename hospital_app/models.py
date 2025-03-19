from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    appointment_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.appointment_date}"