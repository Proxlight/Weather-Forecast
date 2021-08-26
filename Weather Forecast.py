import weather_forecast as wf

location=input("Enter Location Here :")
print('Displaying Weather report for: ' + location)#output:

Weather= wf.forecast(place = location)

print(Weather)