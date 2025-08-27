from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    clas = models.TextField(max_length=10)

    def __str__(self):
        return self.first_name



class Daily(models.Model):
    user = models.ForeignKey(Users, null=True   , on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{Daily.user}'s daily"


class Thoughts(models.Model):
    owner = models.CharField(max_length=120, null=False)
    student = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"by {Thoughts.owner} {Thoughts.student}"
