from django.conf import settings
from django.db import models
from django.utils import timezone

class Formula(models.Model):
    title = models.CharField(max_length=40, blank=False, null=True)
    expression = models.TextField(blank=False)
    published_date = models.DateTimeField(default=timezone.now, editable=False)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #phone = models.CharField(max_length=50)
    #description = models.TextField(blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
