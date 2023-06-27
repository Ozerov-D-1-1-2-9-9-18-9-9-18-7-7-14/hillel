from datetime import datetime, timedelta


def get_date_list(from_date: str, to_date: str) -> list[str]:
    date_format = "%Y-%m-%d"
    dates = []

    start_date = datetime.strptime(from_date, date_format)
    end_date = datetime.strptime(to_date, date_format)

    dates.append(start_date.strftime(date_format))

    while start_date < end_date:
        start_date += timedelta(days=1)
        dates.append(start_date.strftime(date_format))

    return dates


print(get_date_list("2023-06-04", "2023-06-25"))
