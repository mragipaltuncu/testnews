from django.db import models

# Create your models here.
class ArticleTitle(models.Model):
    title = models.CharField(max_length=255)

#Enter your dreams here

    def __str__(self):
        return self.title