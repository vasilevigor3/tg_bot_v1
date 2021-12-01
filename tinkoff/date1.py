# from datetime import date, timedelta, datetime
# import numpy as np
#
# today = date.today()
# today_day = today.day
# today_month = today.month
# today_year = today.year
#
#
# def start_month(limit):
#     return (today - timedelta(days=limit)).month
#
#
# def start_day(limit):
#     return (today - timedelta(days=limit)).day
#
#
# def start_year(limit):
#     return (today - timedelta(days=limit)).year
#
#
# def calculate_date_for_MA(limit):
#     d = str(np.busday_offset(f'{today_year}-{today_month}-{today_day}', -limit, roll='backward'))
#     return datetime.strptime(d, '%Y-%m-%d').date()
#
