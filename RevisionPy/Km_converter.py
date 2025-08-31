# Write a program to convert kilometers to meters.
Meter = float(input("Enter Meter to convert Kilo meters: "))
Kilo_Meter = float(input("Enter Kilo meter to convert meters: "))

KM = Meter/1000.0
Meters = Kilo_Meter*1000.0

print(f"Convert Meter to KM:{Meter}M is {KM}km")
print(f"Convert KM to Meter:{Kilo_Meter}Km is {Meters}M")
