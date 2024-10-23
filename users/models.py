from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Metadata of the model
    class Meta:
        ordering = ['name']  # Orders by 'name' field by default
        verbose_name = 'Users'  # Gives a readable name for this model in the admin interface
