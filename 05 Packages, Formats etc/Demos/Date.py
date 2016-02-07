from datetime import date
from datetime import datetime


print(date(2016, 1, 19))
d = date.today()
print(d)

dt = datetime.now()
print(dt)
d = dt.date()  # създава нов обект date,  съдържащ само информацията за дата от обект datetime
print(d)