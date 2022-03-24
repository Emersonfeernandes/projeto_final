from django.db import models
from datetime import datetime as dt


class Url_Scraper(models.Model):
    URL_save = models.URLField(max_length=200)
    URL_save1 = models.URLField(max_length=200)
    URL_save2 = models.URLField(max_length=200)
    URL_save3 = models.URLField(max_length=200)
    URL_save4 = models.URLField(max_length=200)
    URL_save5 = models.URLField(max_length=200)
    URL_save6 = models.URLField(max_length=200)
    URL_save7 = models.URLField(max_length=200)
    URL_save8 = models.URLField(max_length=200)
    URL_save9 = models.URLField(max_length=200)

    def __str__(self):
        return self.URL_save
