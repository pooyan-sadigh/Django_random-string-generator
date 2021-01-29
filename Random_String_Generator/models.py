from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from YourModel.models import MODEL


class Tag(models.Model):
    title = models.CharField()
    slug = models.SlugField()
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    product = models.ManyToManyField(MODEL)


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
