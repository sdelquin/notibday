# Notibday

**Notibday** comes from **Noti**fication of **B**irth**day**.

It allows you to send notifications via `#Telegram` to a concrete user with information about the birthdays of the contacts you have stored in `Gmail`.

## Development

```console
$ pipenv install
$ vi .env    # set the corresponing values
...
```

Launch the app:

~~~console
$ pipenv run python main.py
~~~

### Gcalcli

In order to run properly the code, you must install the command [gcalcli](https://github.com/insanum/gcalcli) and configure it in a right way. When it is configured you will get a file `~/.gcalcli_oauth` with the access credentials to all your Google calendars.

`gcalcli` should be on the PATH in order to be executed properly.

### Telegram Bot

It will be also necessary to create a **Telegram Bot** using [BotFather](https://telegram.me/BotFather). You will get an identifier (*token*) for your bot. Write this token into de configuration file.

You will need a **user identifier** of Telegram in order to the messages be delivered only to you. You can use [this bot](https://telegram.me/get_id_bot).

### Cron

Obviously you can run the project when you want, but in my case, I have set up the running of the program twice a day with `crontab`:

```console
30 7 * * * ~/notibday/run.sh
0 17 * * * ~/notibday/run.sh
```
