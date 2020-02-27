from datetime import datetime,timedelta
import locale
import calendar


def print_date(name_day, date_print):
    str_date = date_print.strftime('%A %d %B %Y')
    print(f'{name_day}{str_date}')


def date_time():
    locale.setlocale(locale.LC_ALL, "russian")
    date_now = datetime.now()


    print_date('Сегодня ', date_now)
  
    delta = timedelta(days=1)
    tomorrow = date_now + delta
    print_date('Завтра будет ', tomorrow)
 
    yesterday = date_now - delta
    print_date('Вчера был ', yesterday)

    year = date_now.year
    month = date_now.month
    if month == 1:
        year -= 1
        month = 1
    else:
        month -= 1
    delta_day = calendar.monthrange(year, month)[1]
    delta_month = timedelta(days=delta_day)
    last_month = date_now - delta_month
    print_date('Месяц назад был день ', last_month)

    date_string = '01/01/17 12:10:03.234567'
    date_dt = datetime.strptime( date_string, '%d/%m/%y %H:%M:%S.%f')
    print(date_dt)

if __name__ == "__main__":
    date_time()