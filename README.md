# Notibday

**Notibday** comes from **Noti**fication of **B**irth**day**.

It allows you to send notifications via `#Telegram` to a concrete user with information about the birthdays of the contacts you have stored in `Gmail`.

## Configuration

```console
$> cp config.py.example config.example
```

Set the corresponding values in the file.

### Virtualenv

The program expects to have the virtualenv installed in `~/.virtualenvs/notibday`.

### Project directory (production)

The program expects to have the project deployed in `~/notibday`.

### Server name (production)

The program expects to have the name of the production server as `production`. You can change it in `/etc/hosts`.

### Gcalcli

In order to run properly the code, you must install the command [gcalcli](https://github.com/insanum/gcalcli) and configure it in a right way. When it is configured you will get a file `~/.gcalcli_oauth` with the access credentials to all your Google calendars.

### Telegram Bot

It will be also necessary to create a **Telegram Bot** using [BotFather](https://telegram.me/BotFather). You will get an identifier (*token*) for your bot. Write this token into de configuration file.

You will need a **user identifier** of Telegram in order to the messages be delivered only to you. You can use [this bot](https://telegram.me/get_id_bot).

### Cron

Obviously you can run the project when you want, but in my case, I have set up the running of the program twice a day with `crontab`:

```console
30 7 * * * ~/notibday/run.sh
0 17 * * * ~/notibday/run.sh
```
