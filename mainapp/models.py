from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bean(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Roast(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Syrup(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Powder(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    user=models.ForeignKey(User)
    name=models.CharField(max_length=225)
    bean=models.ForeignKey(Bean)
    syrup=models.ManyToManyField(Syrup, blank=True)
    powder=models.ManyToManyField(Powder, blank=True)
    roast=models.ForeignKey(Roast)
    espresso_shots=models.PositiveIntegerField(default=1)
    water=models.FloatField(default=0)
    steamed_milk=models.BooleanField(default=False)
    foam=models.FloatField(default=0)
    extra_instruction=models.TextField(blank=True)

    def __str__(self):
        return self.name
