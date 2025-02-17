from datetime import datetime


def perform_time(start_time: datetime, end_time: datetime):
    # Calculate the time difference
    time_difference = end_time - start_time

    # Extract seconds, minutes, and hours
    seconds = time_difference.seconds
    minutes = seconds // 60
    hours = minutes // 60

    # Show the difference in a readable format
    if hours > 0:
        print( f"Time taken: {hours} hour(s), {minutes % 60} minute(s), {seconds % 60} second(s)")
    elif minutes > 0:
        print( f"Time taken: {minutes} minute(s), {seconds % 60} second(s)")
    else:
        print( f"Time taken: {seconds} second(s)")