# importing geopy library and harvesine library
# these libraries are not included in python interpreter, 
# use pip install geopy and pip install harvesine in cmd to install these libraries
from geopy.geocoders import Nominatim
import haversine as hs
def distance(source, destination):
    
        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")
        coordinates = []
        city = [source, destination]
        for location in city: 
    # entering the location name
          getLoc = loc.geocode(location)
      # printing address
          print(getLoc.address)
        # getting longitude and latitude
          print("Latitude = ", getLoc.latitude)
          print("Longitude = ", getLoc.longitude)
          coordinates.append([getLoc.latitude, getLoc.longitude]) # list of coordinates
        print(coordinates)
        dis = hs.haversine(coordinates[0],coordinates[1])
        print(f'Distance between {source} and {destination} is {round(dis,3)} km')
    

    
# getting distance 
source = input('Enter Source Location : ')
destination = input('Enter Destination Location : ')
distance(source, destination)