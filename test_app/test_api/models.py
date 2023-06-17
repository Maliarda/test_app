from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Letters(models.TextChoices):
    A = 'а'
    B = 'б'
    C = 'в'
    D = 'г'
    E = 'д'


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=10, unique=True, null=True)

    def __str__(self):
        return self.login


class IQTestResult(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    time_taken = models.DateTimeField(auto_now_add=True)


class EQTestResult(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    letters = ArrayField(models.CharField(max_length=2, choices=Letters.choices), size=5)
    time_taken = models.DateTimeField(auto_now_add=True)
