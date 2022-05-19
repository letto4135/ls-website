from django.db import models
from cloudinary.models import CloudinaryField


class Giving(models.Model):
    larger_text = models.TextField()
    smaller_text = models.TextField()


class Link(models.Model):
    link_name = models.TextField()
    link = models.TextField()
    service = models.ForeignKey("Service", on_delete=models.CASCADE,
                                help_text="Links can be added to outside resources can be added to services here. "
                                          "Service must already exist.")


class Service(models.Model):
    text = models.TextField(help_text="Links can be added to services through the Links tab. "
                                      "Service must be created first.")

    def __str__(self):
        return f'{self.text}'


class SmallGroup(models.Model):
    group_name = models.TextField()
    led_by = models.TextField()
    when = models.TextField()
    location = models.TextField()


class Staff(models.Model):
    image = CloudinaryField('image', folder='lsc/staff')
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    view_order = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Staff"
