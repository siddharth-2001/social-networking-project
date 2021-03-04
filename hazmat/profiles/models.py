from django.db import models
from users.models import CustomUser

class Profile(models.Model):
    user            = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio             = models.TextField()
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0) 
    followers       = models.ManyToManyField(CustomUser, related_name='followers')
    following       = models.ManyToManyField(CustomUser, related_name='following')
    profile_image   = models.ImageField(default='none')
    private         = models.BooleanField(default=False)
 
    def __str__(self):
        return self.user.username