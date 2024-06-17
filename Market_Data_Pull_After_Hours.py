import datetime
import pytz

# Convert current user's current time to EST
current_time = datetime.datetime.now(datetime.timezone.utc)
eastern_timezone = pytz.timezone('US/Eastern')
current_time_est = current_time.astimezone(eastern_timezone)

# Mock Time Test Case
# current_time_est = datetime.datetime(year=2024, month=3, day=13, hour=16, minute=30)

# After market hours ( Altering the After Market Hours can occur here)
after_market_hours_start = datetime.time(16, 10) # Translates to 4:10pm 
after_market_hours_end = datetime.time(17, 00) # Translates to 5pm

# Checks if current time is within after-market hours
if after_market_hours_start <= current_time_est.time() <= after_market_hours_end:
    print("Market is closed. Proceed with data pull.")

    # Data Pulling code here

else:
    print("Market is still open. Please wait until after market hours to pull data.")

# Test Case
# print("Current Time:", current_time)
# print("Current Time (EST):", current_time_est)











