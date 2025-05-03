from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Review(models.Model):
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    main_review = models.CharField(max_length = 20, null = True)
    description = models.TextField(max_length = 200, null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.main_review