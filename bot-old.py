import logging
from telegram import Update, ReplyKeyboardMarkup, InputMediaPhoto, Bot
from requests import get
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from bot_app.rocket_manager import RocketManager, image_data
from bot_app.message_manager import MessageManager

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class ToInfinityAndBeyondBot:

    def __init__ (self, token):
        """
        Initializes the bot with the provided token and sets up command and message handlers.
        """
        self.TOKEN = token
        self.application = ApplicationBuilder().token(self.TOKEN).build()

        self.reply_markup = ReplyKeyboardMarkup([['Yes', 'No']], one_time_keyboard=True, resize_keyboard=True)

        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('restart', self.restart))
        self.application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.echo))
        self.application.add_handler(MessageHandler(filters.COMMAND, self.unknown))

    def run(self):
        """
        Runs the bot by starting the polling loop.
        """
        self.application.run_polling()

    async def new_rocket(self, chat_id: int, text: str, bot: Bot):
        """
        Sends a new rocket image to the chat and asks if the rocket launched.
        """
        rocket = RocketManager.get_rocket_image()
        image = get(rocket.image_url).content
        await bot.send_message(chat_id=chat_id, text=text)
        rocket_image = await bot.send_media_group(chat_id=chat_id, media=[InputMediaPhoto(image, caption="")])
        await bot.send_message(chat_id=chat_id, text="Did the rocket launch?", reply_markup=self.reply_markup)
        await MessageManager.save_message(rocket, chat_id=chat_id, msg_id=rocket_image[0].message_id)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles the /start command and initiates the challenge.
        """
        chat_id = update.effective_chat.id
        last_message: image_data = await MessageManager.get_last_message(chat_id)

        if last_message is not None and not last_message.is_rocket_launched:
            await context.bot.send_message(chat_id=chat_id, reply_to_message_id=last_message.message_id, reply_markup=self.reply_markup, text="please, responde si ha despegado solo con si o no")
        else:
            await self.new_rocket(chat_id=chat_id, text="Comenzamos con el reto", bot=context.bot)

    async def restart(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles the /restart command and restarts or starts the challenge.
        """
        chat_id = update.effective_chat.id
        last_message: image_data = await MessageManager.get_last_message(chat_id)

        if last_message is not None and not last_message.is_rocket_launched:
            text = "Yo want to restart the challegne, so we are going to restart"
        else:
            text = "There is nothing to restart, so we are going to start the challenge"
        await self.new_rocket(chat_id=chat_id, text=text, bot=context.bot)

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles user text responses during the challenge.
        """
        chat_id = update.effective_chat.id
        last_message: image_data = await MessageManager.get_last_message(chat_id)

        if last_message is None:
            await context.bot.send_message(chat_id=chat_id, text="Texto de bienvenida")
            return

        if not last_message.is_rocket_launched:
            user_response = update.message.text.lower()
            if user_response == "yes" or user_response == "no":
                next_rocket = RocketManager.get_next_image(
                    image_data(
                        image_url=last_message.image_url,
                        max_frame=last_message.max_frame,
                        min_frame=last_message.min_frame,
                        step=last_message.step,
                        max_steps=last_message.max_steps,
                        current_frame=last_message.current_frame,
                        url=last_message.url,
                        is_rocket_launched=user_response
                    )
                )

                #print(f"max_frame: {next_rocket.max_frame},\nmin_frame: {next_rocket.min_frame},\ncurrent_frame: {next_rocket.current_frame}, \nsetp: {next_rocket.step}")
                image = get(next_rocket.image_url).content

                await context.bot.send_message(chat_id=chat_id, text=f"You said {user_response}, so let's continue the challenge.")
                await MessageManager.update_response_message(last_message.id, response=user_response)

                rocket_image = await context.bot.send_media_group(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, caption="")])
                if next_rocket.step < next_rocket.max_steps:
                    await context.bot.send_message(chat_id=chat_id, text="Did the rocket launch?", reply_markup=self.reply_markup, )
                    await MessageManager.save_message(next_rocket, chat_id=chat_id, msg_id=rocket_image[0].message_id)
                else:
                    await context.bot.send_message(chat_id=chat_id, text="congratulation, el reto acabo maldito hd")
            else:
                await context.bot.send_message(chat_id=chat_id, reply_to_message_id=last_message.message_id, reply_markup=self.reply_markup, text="please, responde si ha despegado solo con si o no")
        else:
            return await context.bot.send_message(chat_id=chat_id, text="comenzar el reto de 0")

    async def unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles unknown commands.
        """
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
