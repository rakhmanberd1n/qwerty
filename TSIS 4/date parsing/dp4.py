import datetime
def seconds_between(x,y):
    senonds=today-some_day
    return senonds.days*24*3600+senonds.seconds

    
today=datetime.datetime.now().replace(microsecond=0)
some_day=datetime.datetime(2023,1,15,16,25,15)
print(seconds_between(today,some_day))