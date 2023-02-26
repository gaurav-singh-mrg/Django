from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


# Create your views here.

def calender(request, year, month):
    year = year
    month = month.title()
    month_number = list(calendar.month_name).index(month)

    month_number = int(month_number)
    Cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'UserIndex.html', locals())
