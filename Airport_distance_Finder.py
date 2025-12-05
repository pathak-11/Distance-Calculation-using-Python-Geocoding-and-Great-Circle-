from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent='r-reticulate-demo')

address1 = 'Cincinnati Airport, KY, USA'
address2 = 'Dayton Airport, OH, USA'

location1 = geolocator.geocode(address1)
location2 = geolocator.geocode(address2)

if location1 is None or location2 is None:
    raise ValueError("One or both addresses could not be geocoded. Check spelling or simplify the address.")

coord1 = (location1.latitude, location1.longitude)
coord2 = (location2.latitude, location2.longitude)

distance_geo = distance.distance(coord1, coord2)
distance_gc = distance.great_circle(coord1, coord2)

print(f'Address 1 Coordinates: {coord1}')
print(f'Address 2 Coordinates: {coord2}')
print(f'Geodesic Distance: {distance_geo.km:.2f} km, {distance_geo.miles:.2f} miles')
print(f'Great Circle Distance: {distance_gc.km:.2f} km, {distance_gc.miles:.2f} miles')
