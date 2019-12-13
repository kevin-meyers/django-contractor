from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User



class Kit(models.Model):
    """ Represents a single kit. """
    name = models.CharField(
        max_length=100, unique=True,
        help_text='Name of the kit.'
    )

    curator = models.ForeignKey(
        User, on_delete=models.PROTECT,
        help_text='The name of the curator that maintains this kit.'
    )

    slug = models.CharField(
        max_length=100, blank=True, editable=False,
        help_text='Generated url path.'
    )

    description = models.TextField(
        help_text='Write the description of your kit!'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='The date and time the kit was created.'
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        help_text='The date and time this kit was updated.'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kit-details-page', {'slug': self.slug})

    def save(self, *args, **kwargs):
        ''' creates a slug url when new kit is created. '''
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)

            return super(Kit, self).save(*args, **kwargs)
