from django.db import models

class Vaccina(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    dose_count = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()  

    class Meta:
        verbose_name = 'Вакцины'