import uuid
from django.db import models

class product(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('socks', 'Socks'),
        ('exclusive', 'Exclusive'),
        ('away', 'Away'),
        ('home','Home'),
        ('third','Third'),
        ('badges','Badges'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    