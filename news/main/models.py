from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    main_image = models.ImageField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
