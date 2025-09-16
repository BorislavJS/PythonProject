number_of_pages = int(input())
read_pages_for_one_hour = int(input())
number_of_days_for_reading_book = int(input())

total_time_reading_book = number_of_pages // read_pages_for_one_hour
needed_hour_for_day = total_time_reading_book // number_of_days_for_reading_book

print(needed_hour_for_day)
