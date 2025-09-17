import uuid
from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu Bola'),
        ('jersey', 'Jersey'),
        ('training', 'Celana Training'),
        ('jaket', 'Jaket'),
        ('bola', 'Bola'),
        ('tas', 'Tas Bola'),
        ('poster', 'Poster'),
        ('figur', 'Figur Pemain'),
        ('aksesoris', 'Aksesoris'),
    ]

    SIZE_CHOICES = [
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='update')
    items_views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
        
    def increment_views(self):
        self.items_views += 1
        self.save()