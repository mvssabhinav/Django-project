from django.db import models
from django.urls import reverse

# Create your models here.
class Exampledatabase(models.Model):
    director=models.CharField( max_length=50)
    movie_name=models.CharField( max_length=50)
    total_directed=models.IntegerField()
    
    class Meta:
        verbose_name = ("Exampledatabase")
        verbose_name_plural = ("Exampledatabases")

    def __str__(self):
        return self.director

    def get_absolute_url(self):
        return reverse("Exampledatabase_detail", kwargs={"pk": self.pk})
