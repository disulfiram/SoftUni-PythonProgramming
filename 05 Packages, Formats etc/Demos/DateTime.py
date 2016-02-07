from datetime import datetime

print(datetime.now())
print(datetime(2016, 1, 19))
print(datetime(2016, 1, 19, 20, 21, 22, 222425))
print(datetime(year=2016, month=1, day=19, hour=20, minute=21, second=22, microsecond=222425))
d = datetime.now()
print(str(d))
#print(d.strftime('година: %Y, месец: %m, ден: %d, час: %H минута: %M  секунда: %S'))
print(d.isoformat())
