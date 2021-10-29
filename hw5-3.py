# Author: IBN (AMDG) 10/29/2021
import calendar

# Question 1
calendar.TextCalendar().pryear(2020)
# Question 2
calendar.TextCalendar(firstweekday=6).pryear(2020)
# Question 3
calendar.TextCalendar().prmonth(2021, 11, w=0, l=0)
# Question 4
#calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020) <- doesn't work
# Question 5
print(calendar.isleap(2022))
# It looks for a year, It returns True or False, it's a boolean.