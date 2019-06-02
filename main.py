'''
Usage:
    main.py [options]

Options:
    -t --today    Send TODAY birthdays
    -n --next     Send NEXT birthdays
'''
from docopt import docopt

from notibday import NotiBday


if __name__ == '__main__':
    arguments = docopt(__doc__)
    postman = NotiBday()
    if arguments['--today']:
        postman.notify_today_birthdays()
    elif arguments['--next']:
        postman.notify_next_birthdays()
