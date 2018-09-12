from geopy.geocoders import Nominatim
from geopy.distance import lonlat, distance

def geo_locator(query):
  geolocator = Nominatim(user_agent="my_application")
  location = geolocator.geocode(query)
  pos = (location.longitude, location.latitude)
  return pos

def result(loc1, loc2, one, two):
  x = (distance(lonlat(*one), lonlat(*two)).miles)
  print ("Distance between %s and %s is %s miles." % (loc1, loc2, str(x)))

#def test():
#  query = '1314 Chavez St, las vegas, nm'
#  query1 = '11105 walnut st, los angeles, ca'
#  print ("Testing: %s and %s on the geopy software." % (query, query1))
#  one = geo_locator(query)
#  two = geo_locator(query1)
#  result(query, query1, one,two)
#test()
def starting():
  pos1 = str(raw_input("Enter starting location: "))
  pos2 = str(raw_input("Enter ending location: "))
  one = geo_locator(pos1)
  two = geo_locator(pos2)
  result(pos2, pos1, one,two)
  return True

def end():
  return False
a = True
command = {1:starting, 2:end}
print ("This python code uses Python 2. An alternative solution is to replace raw_input with input. I am not sure if this method would work though.\n")
while a != False:
  try:
    ans = int(input("Enter 1 to start.\nEnter 2 to quit.\n>>"))
    a = command[ans]()
  except:
    pass

