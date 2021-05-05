from datetime import timedelta
import time , datetime

def nowtime():

    now = datetime.datetime.now()




    now_year = now.year
    now_month = now.month
    now_day = now.day
    now_date_string = '{}-{}-{}'.format(now_year, now_month, now_day)
    
    print('date :', now_date_string)


    now_hour = now.time().hour
    now_minute = now.time().minute
    now_second = now.time().second
    now_time_string = '{}:{}:{}'.format(now_hour, now_minute, now_second)

    print('time :', now_time_string)


nowtime()


### https://www.w3schools.com/python/python_datetime.asp