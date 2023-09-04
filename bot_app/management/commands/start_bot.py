from django.core.management.base import BaseCommand
from bot_app.telegram_bot.bot import ToInfinityAndBeyondBot
from bot_project.settings import TELEGRAM_TOKEN

class Command(BaseCommand):
    """
    Django management command to start the Telegram bot challenge.
    """
    help = 'Starts the Telegram bot challenge'

    def handle(self, *args, **options):
        """
        Executes the command to start the Telegram bot challenge.
        """
        TOKEN = TELEGRAM_TOKEN
        bot = ToInfinityAndBeyondBot(TOKEN)
        bot.run()
