from persiantools.jdatetime import JalaliDate
# pip install persiantools
from datetime import timedelta
import time , datetime

now = datetime.datetime.now()


year = (now.strftime("%Y"))
day = (now.strftime("%d"))
month = (now.strftime("%m"))

now_date_string = '{}-{}-{}'.format(year, month, day)
print('date_en :', now_date_string)


now_year = now.year
now_month = now.month
now_day = now.day

date_fa = JalaliDate(datetime.date(now_year, now_month, now_day))
print('date_fa :', date_fa)



