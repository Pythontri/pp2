from datetime import datetime, timedelta

x = datetime.now()
y = datetime.now() - timedelta(days = 1)
print(y.strftime("%A"))
print(x.strftime("%A"))
y = datetime.now() + timedelta(days = 1)
print(y.strftime("%A"))