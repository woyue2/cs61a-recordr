""" Lab 04: Mutability and Data Abstraction """

from city import *

# Q2
from math import sqrt


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    #selector
    # c1d1 = city1[1]
    # c1d2 = city1[2]
    # c2d1 = city2[1]
    # c2d2 = city2[2]
    # #constructor
    # distance =sqrt((c1d1-c2d1)**2 + (c1d2-c2d2)**2)
    # return distance
    x1 = get_lat(city1)  #比我写的好！
    x2 = get_lat(city2)
    y1 = get_lon(city1)
    y2 = get_lon(city2)
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Q3
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    #constructor
    # citynow = make_city('',lat,lon)
    # city1distance = distance(city1,citynow)
    # city2distance = distance(city2,citynow)
    # return 'city1' if city1distance < city2distance else 'city2'
    given_city = make_city("Some random name", lat, lon)
    if (distance(given_city, city1) < distance(given_city, city2)):
        return get_name(city1)  #give_name函数是city.py定义的
    else:
        return get_name(city2)


# Q4
# This is another implementation of the City ADT. Make sure
# your code works for both the previous and the following versions
# of the constructor and selectors!
#这里是重写方法，不使用city.py里面的构造函数了
make_city = lambda name, lat, lon: {'name': name, 'lat': lat, 'lon': lon}
get_name = lambda city: city['name']
get_lat = lambda city: city['lat']
get_lon = lambda city: city['lon']