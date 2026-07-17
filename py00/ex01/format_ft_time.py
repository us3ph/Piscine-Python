import time
from datetime import datetime

# Get the current time in seconds since the epoch (January 1, 1970)
seconds = time.time()

# Print the current time in seconds since the epoch with formatting
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
# {seconds:,.4f} formats the number with a thousands separator and 4 decimal places
# {seconds:.2e} formats the number in scientific notation with 2 decimal places
# Format the current time in a human-readable format
now = datetime.now()
# Print the current time in a human-readable format
print(now.strftime("%b %d %Y"))