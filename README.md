# After-Market Hours Data Pull Script

This script is designed to check if the current time falls within the designated after-market hours (4:10 PM to 5:00 PM EST) and allow data pulling during that period. It uses the `datetime` and `pytz` libraries to handle time conversions and checks.

## Features

- **Current Time Retrieval:** Obtains the current time in UTC.
- **Time Zone Conversion:** Converts UTC time to Eastern Standard Time (EST) using `pytz`.
- **After-Market Hours Check:** Determines if the current time is within the after-market hours (4:10 PM to 5:00 PM EST).
- **Conditional Data Pull:** Allows data pulling only during after-market hours.
- **Mock Time Test Case:** Includes a mock time test case for testing purposes.
- **Optional Time Output:** Optionally prints the current time in both UTC and EST for debugging.

## Usage

1. Get Current Time in UTC:
   The script first retrieves the current time in UTC.
   
   current_time = datetime.datetime.now(datetime.timezone.utc)

2. Convert to EST:
   It then converts the UTC time to Eastern Standard Time (EST) using pytz.
   
   current_time = datetime.datetime.now(datetime.timezone.utc)

3. Define After-Market Hours:
The after-market hours are defined as the period from 4:10 PM to 5:00 PM EST.

  after_market_hours_start = datetime.time(16, 10) # 4:10 PM
  after_market_hours_end = datetime.time(17, 00)   # 5:00 PM

4. Check Current Time Against After-Market Hours:
The script checks if the current EST time falls within the after-market hours.

    if after_market_hours_start <= current_time_est.time() <= after_market_hours_end:
    print("Market is closed. Proceed with data pull.")
   
else:
    print("Market is still open. Please wait until after market hours to pull data.").4

4.1 MOCK TIME TEST CASE 
    print("Current Time:", current_time)
    print("Current Time (EST):", current_time_est)

## License

This project is licensed under the MIT License.

    

