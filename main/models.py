import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu Bola'),
        ('jersey', 'Jersey'),
        ('training', 'Celana Training'),
        ('jaket', 'Jaket')
        ('bola', 'Bola'),
        ('tas', 'Tas Bola'),
        ('poster', 'Poster'),
        ('figur', 'Figur Pemain'),
        ('aksesoris', 'Aksesoris'),
    ]

    SIZE_CHOICES = [
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L')
        ('xl', 'XL'),
        ('xxl', 'XXL'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='update')
    jumlah_keranjang = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()