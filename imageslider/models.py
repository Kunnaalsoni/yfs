from django.db import models

# Create your models here.
class imageslider(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='collabs/', blank=True, null=True)

    def __str__(self):
        return self.name