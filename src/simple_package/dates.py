import arrow


def str_to_datetime(date: str):
    """Return datetime representation of the string passed as parameter."""
    return arrow.get(date).datetime
