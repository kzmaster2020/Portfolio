from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import User  

class CreateFighter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER_IDENTITY = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other')

    )
    gender = models.CharField(max_length=1, choices=GENDER_IDENTITY)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="fighters")
    
    picture = models.ImageField(null=True, blank=True) 
    ranking = models.IntegerField(default=99)
    ranking_points = models.IntegerField(default=0)
    WEIGHT_CLASS = (
        ('1', 'Lightweight'),
        ('2', 'Heavyweight'),
        ('3', 'Titan')
    )
    weight = models.CharField(max_length=1, choices=WEIGHT_CLASS)
    
    
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # def sample_view(request):
        # current_user = request.user
        # print (current_user.id)