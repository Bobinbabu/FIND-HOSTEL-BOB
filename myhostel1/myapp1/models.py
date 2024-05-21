from django.db import models

class uregister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.username
class ulogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()
    def __str__(self):
        return self.username

class hregister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.username
class hlogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()
    def __str__(self):
        return self.username