from datetime import datetime


def date():
    date = datetime.now().strftime('%d.%m.%Y')
    return date
