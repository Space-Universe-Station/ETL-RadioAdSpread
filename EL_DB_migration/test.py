from datetime import datetime
import pytz

# Create a datetime object with the current date and time
dt = datetime(1970, 1, 1, 0, 0, 0,tzinfo=pytz.UTC)
# Parse the string into a datetime object
# Convert the datetime object to a string in the ISO 8601 format
timestamp_str = dt.isoformat()
print(timestamp_str)