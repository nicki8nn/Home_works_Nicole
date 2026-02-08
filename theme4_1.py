import datetime

today = datetime.datetime.today()
date_string = "2020-10-09"
from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between a given date string and today.
    
    Example:
    >>> # Note: This test's success depends on the current date.
    >>> # If today was 2020-10-10, the result below would be -1.
    >>> isinstance(get_days_from_today("2020-10-09"), int)
    True
    """
    given_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today().date()
    return (given_date.date() - today).days

if __name__ == "__main__":
    import doctest
    doctest.testmod()

result = get_days_from_today(date_string)
print (result)


