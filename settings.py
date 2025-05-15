import telegramtk
from prettyconf import config

GOOGLE_API_SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/contacts.readonly',
]

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
TELEGRAM_USER_ID = config('TELEGRAM_USER_ID')
CONTACTS_CAL_ID = config('CONTACTS_CAL_ID')
VIP_FILE = config('VIP_FILE', default='vip.dat')

telegramtk.init(TELEGRAM_BOT_TOKEN)
