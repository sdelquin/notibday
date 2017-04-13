# Notibday

**Notibday** viene de **Noti**fication of **B**irth**day**.

Permite enviar notificaciones vía `#Telegram` a un usuario en concreto de los cumpleaños de cada día, según los contactos guardados en `Gmail`.

## Configuración

```console
$> cp config.py.example config.example
```

Establecer los valores correspondientes.

### Gcalcli

Para que funcione correctamente, se debe tener instalado el comando [gcalcli](https://github.com/insanum/gcalcli) y configurado correctamente. Cuando se configura, se crea un fichero `~/.gcalcli_oauth` con las credenciales de acceso a los calendarios de Google del usuario.

### Bot de Telegram

También será necesario crear un **bot de Telegram** utilizando [BotFather](https://telegram.me/BotFather). Se te asignará un identificador del bot, que tendrás que utilizar en el fichero de configuración.

También necesitarás tu **identificador de usario** de Telegram para que los mensajes sólo te lleguen a ti. Para ello, puedes hacer uso de [este bot](https://telegram.me/get_id_bot).
