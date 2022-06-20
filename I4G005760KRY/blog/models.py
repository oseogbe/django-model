from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title