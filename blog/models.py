from django.db import models

# Anytime you create a model you will have to migrate
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title