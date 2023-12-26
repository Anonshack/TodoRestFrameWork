from django.db import models


class Todo(models.Model):
    STATUS_CHOICES = (
        ('CURRENT', 'Current'),
        ('COMPLETED', 'Completed'),
        ('CREATE', 'Create'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
