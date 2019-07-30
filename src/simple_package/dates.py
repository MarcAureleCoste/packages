import arrow


def str_to_datetime(date: str):
    """Return datetime representation of the string passed as parameter."""
    return arrow.get(date).datetime


def now():
    return arrow.now()


def plus_hour():
    return arrow.now().shift(hours=1)


def minus_hour():
    return arrow.now().shift(hours=-1)
