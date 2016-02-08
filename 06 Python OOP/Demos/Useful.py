from datetime import datetime, date

d = date.today()

print(isinstance(d, date))  # True

print(isinstance(d, datetime))  # False

d = date.today()
dt = datetime.now()

hasattr(d, 'year')   # True
hasattr(dt, 'year')  # True

hasattr(d, 'hour')   # False
hasattr(dt, 'hour')  # True

print(getattr(d, 'year'))   # 2016

print(getattr(d, 'hour', 'no hour is defined in d'))   # default value if the attribute does not exist

print(getattr(d, 'hour'))   # will raise an AttributeError
