from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image/%Y/%m/%d/', null=True, blank=True)
    release_date = models.CharField(max_length=15)
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, )
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name