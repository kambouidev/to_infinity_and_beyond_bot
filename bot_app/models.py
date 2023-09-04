from django.db import models

class Message(models.Model):
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField()
    max_frame = models.IntegerField()
    min_frame = models.IntegerField()
    current_frame = models.IntegerField()
    step = models.IntegerField()
    url = models.TextField()
    is_rocket_launched = models.TextField()
    message_id=models.IntegerField()
    max_steps=models.IntegerField()
