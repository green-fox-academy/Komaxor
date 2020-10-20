current_hours = 14
current_minutes = 34
current_seconds = 42

time_passed = current_seconds + 60 * current_minutes + 3600 * current_hours
total_time = 24 * 60 * 60
time_remaining = total_time - time_passed
print(time_remaining)