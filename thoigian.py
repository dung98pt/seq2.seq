import datetime as dt

class thoigian:
    def __init__(self):
        pass
    def ntd(str):
        today = dt.datetime.now()
        #-----------------
        year = today.year
        mon = today.month
        day = today.day
        #-----------------
        date = today.date()
        time = today.time()
        hour = time.hour
        minute = time.minute
        if (str == "ngay"):
            return 'Ngày '+day.__str__()+' Tháng '+mon.__str__()+' Năm '+year.__str__()
        elif (str == "gio"):
            return hour.__str__() + ":" + minute.__str__()
        else:
            return time.__str__()







