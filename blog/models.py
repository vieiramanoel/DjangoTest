from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
