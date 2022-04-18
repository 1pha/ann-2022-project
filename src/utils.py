from datetime import datetime as dt


def get_today():

    td = dt.today()

    return (
        str(td.year)
        + str(td.month).zfill(2)
        + str(td.day).zfill(2)
        + "-"
        + str(td.hour).zfill(2)
        + str(td.minute).zfill(2)
    )
