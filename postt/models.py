# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django import forms
from django.db import models
# Create your models here.
from ckeditor.fields import RichTextField


class postt(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='yazar', related_name='posts')
    title = models.CharField(max_length=120, verbose_name='başlık')
    content = RichTextField(verbose_name='içerik')
    publishing_date = models.DateTimeField(verbose_name='yayınlanma tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', self.title)

    def get_delete_url(self):
        return reverse('post:delete', self.title)

    class Meta:
        ordering = ['publishing_date']

class comment(models.Model):
    postt = models.ForeignKey('postt.postt', related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name='isim')
    content = models.TextField(verbose_name='yorum')

    created_date = models.DateTimeField(auto_now_add=True)





        #return reverse('detail', kwargs=('id':self))