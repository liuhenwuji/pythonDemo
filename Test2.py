import time
import datetime

now = datetime.datetime.now()
now2 = now.strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(now2)

time2 = datetime.datetime.strptime('2017-08-30 18:15:00', '%Y-%m-%d %H:%M:%S')
time3 = datetime.datetime.strptime("November of '63", "%B of '%y")
print(time2)
print(time3)

# # sleep 1 second
# time.sleep(1)

# 时间戳
time1 = time.time()
print(time1)

time4 = datetime.datetime.fromtimestamp(time.time())
print(time4)

