from django.db import models

class Urls(models.Model):
    ourl = models.URLField()
    furl = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.ourl
