import uuid
from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
    CATEGORY_CHOICES = [
        ('scarves', 'Scarves'),
        ('socks', 'Socks'),
        ('accessories', 'Accessories'),
        ('away', 'Away Jersey'),
        ('home','Home Jersey'),
        ('third','Third Jersey'),
        ('badges','Badges'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    # Allow longer thumbnails (some CDNs or signed URLs can exceed 200 chars)
    thumbnail = models.URLField(max_length=2000, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.name
