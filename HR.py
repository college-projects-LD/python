"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

age = int (input('How old are you? : '))

HR_Max = 220 - age

rec_max = HR_Max * .85
rec_min= HR_Max * .65

print(f'''When you exercise to strengthen your heart, you should
keep your heart rate between {rec_min} and {rec_max} beats per minute. btw your max hr is {HR_Max}''')

