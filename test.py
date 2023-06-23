import datetime
dt = datetime.datetime.now()
# print(dt.year, dt.month, dt.day, dt.hour, dt.minute, type(dt.second))
print(f"{dt.year}-{str(dt.month).zfill(2)}-{dt.day} {dt.hour}:{dt.minute}")