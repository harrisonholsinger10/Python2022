# Harrison Holsinger

# This program asks for a number of seconds and converts to eiter minutes, hours, or days

# Input
seconds = int(input("Enter a number of seconds: "))

# Check first range
if seconds >= 60 and seconds < 3600:
    minutes = seconds / 60      # Calculate minutes
    # Output results. Round to 2 decimals, format so that numbers over one thousand have a comma
    # Change grammar to avoid saying "There are 1 minutes in 60 seconds"
    if round(minutes, 2) == 1.00:
        print("There is " + str(round(minutes, 2)) + " minute in " + '{:,}'.format(seconds) + " seconds.")
    else:
        print("There are " + str(round(minutes, 2)) + " minutes in " + '{:,}'.format(seconds) + " seconds.")

# Check seconds range
elif seconds >= 3600 and seconds < 86400:
    hours = seconds / 3600
    # Output results. Round to 2 decimals, format so that numbers over one thousand have a comma
    # Change grammar to avoid saying "There are 1 hourss in 3600 seconds"
    if round(hours, 2) == 1.00:
        print("There is " + str(round(hours, 2)) + " hour in " + '{:,}'.format(seconds) + " seconds.")
    else:
        print("There are " + str(round(hours, 2)) + " hours in " + '{:,}'.format(seconds) + " seconds.")

# Check third range
elif seconds >= 86400:
    days = seconds / 86400
    # Output results. Round to 2 decimals, format so that numbers over one thousand have a comma
    # Change grammar to avoid saying "There are 1 days in 86400 seconds"
    if round(days, 2) == 1.00:
        print("There is " + str(round(days, 2)) + " day in " + '{:,}'.format(seconds) + " seconds.")
    else:
        print("There are " + str(round(days, 2)) + " days in " + '{:,}'.format(seconds) + " seconds.")

# Check final range. If it cannot convert to another metric, it remains in seconds
else:
    print(str(seconds) + " seconds is just " + str(seconds) + " seconds.")
