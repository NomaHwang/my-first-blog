#!/usr/bin/python
# coding: UTF-8
__author__ = 'noma Hwang'
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)