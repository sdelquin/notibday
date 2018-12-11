# Notibday

**Notibday** comes from **Noti**fication of **B**irth**day**.

It allows you to send notifications via `#Telegram` to a concrete user with information about the birthdays of the contacts you have stored in `Gmail`.

## Development

~~~console
$ pipenv install
$ vi .env    # set the corresponing values
...
~~~

Launch the app:

~~~console
$ pipenv run python main.py
~~~

### VIP file

When obtaining next birthdays a `vip.dat` file can be filled in with those *very important people* who we want to be aware of their birthdays from.

The structure of this file is as simple as writing the **whole name (and surname)** of the person at each line.

### Telegram Bot

It will be also necessary to create a **Telegram Bot** using [BotFather](https://telegram.me/BotFather). You will get an identifier (*token*) for your bot. Write this token into de configuration file.

You will need a **user identifier** of Telegram in order to the messages be delivered only to you. You can use [this bot](https://telegram.me/get_id_bot).

### Google Calendar API

[Here](https://developers.google.com/calendar/quickstart/python) you can enable the Google Calendar API and obtain a `credentials.json` which will be located at root of the project.

### Cron

Obviously you can run the project when you want, but in my case, I have set up the running of the program twice a day with `crontab`:

~~~console
30 7 * * * ~/notibday/run.sh
0 17 * * * ~/notibday/run.sh
~~~
