from django.db import models

class SushiCard(models.Model):
    TYPES = [
        ('nigiri', 'Nigiri'),
        ('sashimi', 'Sashimi'),
        ('roll', 'Roll'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sushi_type = models.CharField(max_length=10, choices=TYPES)
    image = models.ImageField(upload_to='sushi_images/')

    def __str__(self):
        return self.title
