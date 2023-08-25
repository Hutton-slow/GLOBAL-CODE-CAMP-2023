from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="DOM")

in1 = input("please enter first location\n")
in2 = input("please enter second location\n")


first_location = geolocator.geocode(in1)
second_location = geolocator.geocode(in2)

print(f"\nThe first location was {first_location.address}")
print(f"The second location was {second_location.address}")

first_cordinates = (first_location.latitude, first_location.longitude)
second_cordinates = (second_location.latitude, second_location.longitude)

print(f"The distance between {in1} and {in2} is {geodesic(first_cordinates, second_cordinates).miles} miles")