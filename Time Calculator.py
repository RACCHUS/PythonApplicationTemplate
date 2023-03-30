def add_time(start, duration, starting_day=""):
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    # Separate the start into hours and minutes
    parts = start.split()
    time = parts[0].split(":")
    end = parts[1]

    # Calculate 24-hour clock format
    if end == "PM":
        hour = int(time[0]) + 12
        time[0] = str(hour)

    # Separate the duration into hours and minutes
    dur_time = duration.split(":")

    # Add hours and minutes
    total_minutes = int(time[0]) * 60 + int(time[1]) + int(dur_time[0]) * 60 + int(dur_time[1])
    days_add, total_minutes = divmod(total_minutes, 1440)  # 1440 minutes in a day
    new_hour, new_minutes = divmod(total_minutes, 60)

    # Find AM and PM
    end = "PM" if new_hour >= 12 else "AM"

    # Convert to 12-hour clock format
    new_hour = new_hour % 12 or 12

    if days_add > 0:
        days_later = f" ({days_add} days later)" if days_add > 1 else " (next day)"
    else:
        days_later = ""

    if starting_day:
        starting_day = starting_day.lower().capitalize()
        day_index = (week_days.index(starting_day) + days_add) % 7
        day = f", {week_days[day_index]}"
    else:
        day = ""

    new_time = f"{new_hour}:{new_minutes:02d} {end}{day}{days_later}"
    return new_time

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)