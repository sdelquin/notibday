import utils

contacts = utils.get_contacts()
if contacts:
    buf = list()
    buf.append("Hoy es el cumpleaños de:")
    for c in contacts:
        buf.append("🎂 *{}*".format(c))
    utils.send_message("\n".join(buf))
