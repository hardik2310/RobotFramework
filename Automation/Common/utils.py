from datetime import datetime


def sort_dates_in_list(list_of_dates):
    list_of_dates.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
