from pyexpat import model
from tabnanny import verbose
from django.db import models
from PIL import Image

# Create your models here.


class Profile(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    fathersname = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length = 100, null=True)
    job = models.CharField(max_length = 15, null=True)
    phone = models.CharField(max_length =  10, null=True)
    email = models.CharField(max_length = 20, null=True)
    avatar=models.ImageField(upload_to='static/profile_image', blank=True)

    def __str__(self):
        return self.firstname 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.avatar.path)


class DetectedUsers(models.Model):
    user_id = models.CharField(max_length=100)
    action = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id

