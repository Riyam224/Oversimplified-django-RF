from django.db import models

# Create your models here.
from django.utils.translation import gettext as _

class Item(models.Model):
 

    name = models.CharField(_("name"), max_length=250)
    created = models.DateTimeField(_("created"),  auto_now_add=True)

    # TODO: Define fields here

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
