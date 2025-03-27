from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Location (models.Model):
    name = models.CharField(max_length=256, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=True)
    pub_date = models.DateField(blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True
    )
    is_published = models.BooleanField(default=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)
