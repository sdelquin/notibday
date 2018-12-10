import config
from notibday import NotiBday

postman = NotiBday(config.CONTACTS_CAL_ID)
postman.notify_today_birthdays()
