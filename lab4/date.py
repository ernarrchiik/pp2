from datetime import datetime
#1
x = datetime.datetime.now()
new = x - datetime.timedelta(days=5)
print(new)
#2
x = datetime.datetime.now()
yest = x - datetime.timedelta(days=1)
tomm = x + datetime.timedelta(days=1)
print(yest.strftime("%d-%m-%Y"))
print(x.strftime("%d-%m-%Y"))
print(tomm.strftime("%d-%m-%Y"))
#3
x = datetime.datetime.now()
micro = x.microsecond
print(micro)
#4
date1 = '2025-02-12 14:30:00'
date2 = '2025-02-11 13:30:00'
date_format = '%Y-%m-%d %H:%M:%S'
date_1 = datetime.strptime(date_format,date1)
date_2 = datetime.strptime(date_format,date2)
new = date_2-date_1
result = new.total_seconds()
print(result)