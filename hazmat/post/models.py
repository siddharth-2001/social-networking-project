from django.db import models
from users.models import CustomUser


class Post(models.Model):
    user    = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    image   = models.ImageField(default = 'none')
    caption = models.TextField()
    likes   = models.IntegerField()

    def __str__(self):
        return self.caption