import calendar
from datetime import date


def calender():
    # Get the current year, month, and day
    current_year = date.today().year
    current_month = date.today().month
    current_day = date.today().day

    # Generate the calendar for the current month
    cal = calendar.monthcalendar(current_year, current_month)

    # Print the calendar with today's date indicated
    print(calendar.month_name[current_month], current_year)
    print(calendar.weekheader(3))
    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '   '
            elif day == current_day:
                week_str += f'[{day:2d}]'
            else:
                week_str += f' {day:2d} '
        print(week_str)


if __name__ == "__main__":
    calender()
