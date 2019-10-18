# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django import forms

from django.db import models

# Create your models here.

class postt(models.Model):
    title = models.CharField(max_length=120,verbose_name='başlık')
    content = models.TextField(verbose_name='içerik')
    publishing_date = models.DateTimeField(verbose_name='yayınlanma tarihi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', self.title)



        #return reverse('detail', kwargs=('id':self))