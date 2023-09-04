import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_project.settings')
django.setup()

from django.utils import timezone
from .tuplas import image_data
from .models import Message
from asgiref.sync import sync_to_async

class MessageManager:
    """
    This class manages interactions with the database for storing and retrieving rocket-related messages.
    """

    @sync_to_async
    def save_message(self, rocket_info: image_data, chat_id=int, msg_id=int):
        """
        Saves a new rocket-related message to the database.
        """
        Message.objects.create(
            user_id=chat_id,
            created_at=timezone.now(),
            image_url=rocket_info.image_url,
            max_frame=rocket_info.max_frame,
            min_frame=rocket_info.min_frame,
            current_frame=rocket_info.current_frame,
            step=rocket_info.step,
            url=rocket_info.url,
            is_rocket_launched=rocket_info.is_rocket_launched,
            message_id=msg_id,
            max_steps=rocket_info.max_steps
        )

    @sync_to_async
    def update_response_message(self, pk=int, response=str):
        """
        Updates the response message of a rocket-related message.
        """
        Message.objects.filter(pk=pk).update(is_rocket_launched=response)
    

    @sync_to_async
    def get_last_message(self, chat_id) -> image_data | None:
        """
        Retrieves the latest rocket-related message for a given chat ID.
        """
        try:
            message = Message.objects.filter(user_id=chat_id).latest('created_at')
            return message
        except Message.DoesNotExist:
            return None
