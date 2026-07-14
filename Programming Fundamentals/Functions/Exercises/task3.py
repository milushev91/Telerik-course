# # 3. Write a function that 
# # converts a number of seconds into
# #  a formatted time string "hours:minutes:seconds".

def seconds_to_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds - (hours * 3600)) // 60
    seconds = time_in_seconds -  (hours * 3600 + minutes * 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(seconds_to_time(45))
# x = seconds_to_time(3661)  # x should be "01:01:01"
# x = seconds_to_time(45)    # x should be "00:00:45"
