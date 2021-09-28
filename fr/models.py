from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth import models as am
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Opros(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField()
    finish = models.DateField()
    desc = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['start']

class Vopros(models.Model):
    TXT = "00"
    ONE = "01"
    MANY = "02"
    tips = [(TXT, "Текст"),(ONE, "Один"), (MANY, "Много")]
    vopros = models.TextField()
    tip = models.CharField(max_length=2, choices=tips)
    opros = models.ForeignKey(Opros, on_delete=models.CASCADE)
    standart_otvet = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.opros.name + "|" + self.vopros

class Otvet(models.Model):
    user_id = models.IntegerField()
    vopros = models.ForeignKey(Vopros, on_delete=models.CASCADE)
    otvet = models.CharField(max_length=1000)
    def __str__(self):
        return self.vopros.vopros + "|" + str(self.id_polzovatel) + "|" + self.otvet