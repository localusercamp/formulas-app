from django.conf import settings
from django.db import models
from django.utils import timezone

class Note(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    phone = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    published_date = models.DateTimeField(default=timezone.now, editable=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
