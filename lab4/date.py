# import datetime => datetime.datetime, datetime.date, datetime.timedelta, or:
from datetime import timedelta, date, datetime
date1=date.today()
# 1
delta=timedelta(days=5)
print(f"Subtracting 5 days from the current date: {date1-delta}")

# 2
td=timedelta(days=1)
print(f"Yesterday: {date1-td}, today: {date1}, tomorrow: {date1+td}")

# 3
x=datetime.today().replace(microsecond=0)
print(x)

# 4
dt1=datetime.today()
dt2=datetime(2018, 6, 1)
diff=dt1-dt2
print(diff.total_seconds())