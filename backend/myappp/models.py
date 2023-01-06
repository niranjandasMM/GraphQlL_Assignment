from django.db import models

# Create your models here.
from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

anime = Anime(name='Naruto', genre='Action')
anime.save()

from faker import Faker
fake = Faker()

for _ in range(10):
    anime = Anime(name=fake.name(), genre=fake.genre())
    anime.save()