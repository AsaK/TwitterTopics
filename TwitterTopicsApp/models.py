from django.db import models

# Create your models here.
class TrendingTopics(models.Model):

    text = models.CharField(max_length=140)

    def __str__(self):
        return self.Text
