# Determine Leap Years
year_beg = 1901
year_end = 2000


def check_leap_year(check_year):
    if check_year % 4 == 0:
        if check_year % 100 == 0 and check_year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'September',
          'October',
          'November',
          'December']

days_in_month = {'January': 31,
                 'February': 28,
                 'March': 31,
                 'April': 30,
                 'May': 31,
                 'June': 30,
                 'July': 31,
                 'August': 31,
                 'September': 30,
                 'October': 31,
                 'November': 30,
                 'December': 31}

days_of_week = ['Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday']

month_bound_non_leap = []
total = 0
for key in days_in_month:
    total += days_in_month[key]
    month_bound_non_leap.append(total)

month_bound_leap = []
total = 0
for key in days_in_month:
    if key == 'February':
        total += 1
    total += days_in_month[key]
    month_bound_leap.append(total)


def find_date(day_number, is_leap_year):
    if is_leap_year:
        check_list = month_bound_leap
    else:
        check_list = month_bound_non_leap
    for j in range(0, 11):
        if day_number <= check_list[0]:
            return months[0], day_number
        elif check_list[j] < day_number <= check_list[j + 1]:
            return months[j], day_number - check_list[j]


sunday_count = 0

total_count = 0
for year in range(1900, year_end+1):
    leap_year = check_leap_year(year)
    if leap_year:
        num_days_in_year = 366
    else:
        num_days_in_year = 365

    for day_count in range(1, num_days_in_year + 1):
        month, day_of_month = find_date(day_count, leap_year)
        day = days_of_week[total_count % 7]
        if day == 'Sunday' and day_of_month == 1 and year_beg <= year:
            sunday_count += 1
        total_count += 1
print(sunday_count)
