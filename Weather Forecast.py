# Importing Packages
import weather_forecast as wf

# Taking user's location as an input
location=input("Enter Location Here :")

print('Displaying Weather report for: ' + location)

# Retriving the data using .forecast() method
Weather= wf.forecast(place = location)

# Printing the final results
print(Weather)