from django.db import models
from django.contrib.auth.models import User

class Sushi(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sushi'
        verbose_name = 'sushi'
        verbose_name_plural = 'sushis'
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return self.name
