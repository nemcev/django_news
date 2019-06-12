from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=200)
    img = models.URLField(max_length=200)
    text = models.TextField()
    pub_date = models.DateField('Дата публикации')    