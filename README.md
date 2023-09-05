# 🚀 Did the rocket launch? 🚀

This project is all about helping you discover the exact date when a rocket launch happened. 🛰️ We've got a cool Telegram bot that'll make it feel like a game! You can find it on Telegram under the name [@ToInfinityAndBeyondKBot](https://t.me/ToInfinityAndBeyondKBot) (requires a running server).

## Prerequisites 🛠️

Before you embark on this rocket adventure, make sure you have the following ready:

1. 🐍 [Python 3.11.5](https://www.python.org/downloads/release/python-3115/) installed on your system.
2. 🌟 [Pyenv](https://github.com/pyenv/pyenv) set up for managing Python versions.

## Setting Up Your Python Environment with Pyenv 🐍

1. If you haven't already, install Pyenv by following the instructions in the [official Pyenv repository](https://github.com/pyenv/pyenv).

2. Install Python 3.11.5 with Pyenv:

```bash
   # windows powershell
   pyenv install 3.11.5
```

3. Set Python 3.11.5 as your local version using Pyenv and create a virtual environment:
```bash
   # windows powershell
   pyenv local 3.11.5
```
4. Confirm that Python 3.11.5 is active:
```bash
   # windows powershell
   python version
```

### Creating Your Telegram Bot 🤖

1. Start by creating a Telegram bot using BotFather on Telegram. Don't forget to grab that bot token!

>Follow these [steps](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

2. Next, clone this repository to your local machine:

```bash
   git clone https://github.com/kambouidev/to_infinity_and_beyond_bot.git
```

3. Navigate to your project directory:
```bash
   cd to_infinity_and_beyond_bot
```

4. Install the necessary Python packages with pip
```bash
   pip install -r requirements.txt
```

5. Now, it's time to configure your environment. Create and fill the .env file with your settings:

> For an example, refer to the .env-template file. You can find an example configuration there.


```bash
# .env

TELEGRAM_TOKEN=your_telegram_bot_token
DEBUG=True or False
SECRET_KEY=your_django_secret_key

# Database specifications
ENGINE=django.db.backends.postgresql
NAME=your_database_name
USER=your_database_user
PASSWORD=your_database_password
HOST=your_database_host
```
### Setting Up Your PostgreSQL Database 🐘

1. If you haven't already, install [PostgreSQL](https://www.postgresql.org/download/) on your system.
2. Create a new PostgreSQL database for your project.

## Running the Bot toInfinityAndBeyond 🚀

1. Apply the database migrations:
```bash
    python manage.py makemigrations
    python manage.py migrate
```

2. Start the Django development server:
```bash
    python manage.py start_bot
``` 

## How to Use the Telegram Bot 📱

1. Search for your bot on Telegram and start a conversation
2. The bot will show you frames from the rocket launch video.
3. Reply with "Yes" if you think the rocket has taken off or "No" if it hasn't.
4. The bot will continue to send you frames until it identifies the frame where the rocket launch is happening, approximately around the 16th image.

### Why I Undertook This Project:

This project was undertaken at the request of a company as part of a challenging test, and I found the experience highly enjoyable. It provided an opportunity to explore and implement innovative functionalities.

To ensure code maintainability, several key strategies were employed:

**Comments and Documentation**: Thorough comments and docstrings were added to clarify code functionality, making it comprehensible for both current and future developers.

**Descriptive Naming**: Meaningful variable and function names were chosen to enhance code readability, reducing the need for excessive comments.

**Class-Based Structure**: The code adheres to a structured, class-based format, which simplifies the organization of related functions and data, especially in larger projects.

**Constants**: Important values like messages and text strings were centralized at the top of the file, enabling easy adjustments without the need to search throughout the codebase.

**Modularization**: The code is modularized into separate components, like **RocketManager** and **MessageManager**, housed within the **bot_app** folder. This modularity allows for independent management of various application aspects.

**Configurability**: Configuration parameters, such as the Telegram token and keyboard markup, are conveniently located at the beginning of the code for effortless customization.

**Separation of Concerns**: Different sections of the code are dedicated to specific tasks, ensuring that each part can be modified or debugged independently.
