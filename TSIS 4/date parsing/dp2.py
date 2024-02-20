import datetime
today=datetime.date.today()
Yesterday=today-datetime.timedelta(1)
Tommorow=today+datetime.timedelta(1)
print(f"Yesterday: {Yesterday}\nToday: {today}\nTomorrow :{Tommorow}")