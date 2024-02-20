import datetime
today=datetime.date.today()
five_days_before=today-datetime.timedelta(5)
print(five_days_before)