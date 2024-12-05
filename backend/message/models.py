from django.db import models

class Message(models.Model):
    content = models.TextField()  # El contenido del mensaje
    timestamp = models.DateTimeField(auto_now_add=True)  # Marca de tiempo automática

    def __str__(self):
        return f"{self.content[:50]} ({self.timestamp})" 
