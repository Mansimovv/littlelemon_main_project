from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='menu_image/')

    def __str__(self):
        return f"{self.name} : {self.price}"