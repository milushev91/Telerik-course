# get time 

input_line = input()

if " " in input_line and ":" in input_line:
    current_time, time_designator = input_line.split()
    hour, minutes = current_time.split(":")
 
    
    if hour.isdigit() and minutes.isdigit() and \
        (time_designator == "PM" or time_designator == "AM"):
        hour, minutes = int(hour), int(minutes)
        
        if time_designator == "PM":
            if hour == 12:
                print("non-beer time")
            else:
                print("beer time")
        else:
            if hour == 12 or hour < 3:
                print("beer time")
            else:
                print("non-beer time")
    else:
        print("invalid time")
        
else:
    print("invalid time")
