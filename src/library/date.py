from datetime import datetime


def date():
    date = datetime.now().strftime('%m.%Y')
    return date
