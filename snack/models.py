from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class Snacks(models.Model):
    purchaser = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.name
