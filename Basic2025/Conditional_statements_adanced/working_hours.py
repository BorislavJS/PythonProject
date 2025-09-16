hours = int(input())
day = input()

working_hours = 10 <= hours <= 18

if working_hours and (day == "Monday" or day == "Tuesday" or day == "Wednesday"
                        or day == "Thursday" or day == "Friday" or day == "Saturday"):
    print("Open")
else:
    print("Closed")


