from django.db import models

# Create your models here.
class Index(models.Model):
    my_name = models.CharField(max_length=50)
    my_description = models.TextField()
    languages_learnt = models.FilePathField(path='homepage/static/img')
    my_image = models.FilePathField(path='homepage/static/img')
    my_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.my_name