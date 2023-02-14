from django.db import models


class Valor(models.Model):
    num = models.IntegerField()

    def __str__(self):
        return str(self.num)