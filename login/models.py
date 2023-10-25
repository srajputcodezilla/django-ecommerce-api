from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    user_id=models.CharField(max_length=500, null=False, default="" ,blank=True)
    token = models.CharField(max_length=500, null=True, default="" ,blank=True)
    def __str__(self):
        return "{} -{}".format(self.username, self.email)