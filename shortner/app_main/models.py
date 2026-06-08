from django.db import models
from django.contrib.auth.models import User

class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='short_urls')
    original_url = models.URLField(max_length=2000)
    short_key = models.CharField(max_length=50, unique=True,null=True)  
    short_url = models.URLField(max_length=500)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.short_key} -> {self.original_url[:50]}"
    
    class Meta:
        ordering = ['-created_at']