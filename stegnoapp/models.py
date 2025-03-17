
# Create your models here.
from django.db import models

class StegoImage(models.Model):
    image = models.ImageField(upload_to='stego_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    encoded_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"StegoImage {self.id} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"