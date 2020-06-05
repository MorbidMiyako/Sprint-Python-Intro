# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
cities = []


class City:
    # def __init__(self, city, state_name, county_name, lat, lng, population, density, timezone, zips):
    def __init__(self, city, lat, lng):
        self.name = city
        self.lat = float(lat)
        self.lon = float(lng)

    def __str__(self):
        return f"'{self.name}', {self.lat}, {self.lon}"


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    # cities_file = open("cities.csv", "r")
    # all_lines = cities_file.readlines()
    # all_lines.pop(0)
    # for line in lines:
    #     (City(*line.split(",")))for line in lines:
    with open('cities.csv') as csvfile:
        all_lines = csv.reader(csvfile, delimiter=',')
        for current_line in all_lines:
            if current_line[0] == "city":
                # print(current_line)
                pass
            else:
                # print(City("Seattle", 47.6217, -122.3238))
                # print(City(current_line[0], current_line[3], current_line[4]))
                cities.append(
                    City(current_line[0], current_line[3], current_line[4]))

        # all_lines.pop(0)
    # for next_line in all_lines:
    #     a, b, c, d, e, f, g, h, i = next_line.split(",")
    #     # new_city = City(a, b, c, d, e, f, g, h, i)
    #     # print(new_city)
        # cities.append(City(a, d, e))

        # return [City(*next_line.split(",")) for next_line in all_lines]
    return cities


cities = cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)
    # print(f"{c.name}, {c.lat}, {c.lon}")

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    # within = []

    within_lat = []

    within_lon_too = []

    if lat1 < lat2:

        print("lat1 smaller than lat2")
        if lon1 < lon2:

            print("lon1 smaller than lon2")
            # lat1 smaller than lat2
            within_lat = [city for city in cities if lat1 < city.lat < lat2]
            # lon1 smaller than lon2
            within_lon_too = [
                city for city in within_lat if lon1 < city.lon < lon2]

        else:

            print("lon1 bigger than lon2")
            # lat1 smaller than lat2
            within_lat = [city for city in cities if lat1 < city.lat < lat2]
            # lon1 bigger than lon2
            within_lon_too = [
                city for city in within_lat if lon1 > city.lon > lon2]

    else:

        # print("lat1 bigger than lat2")
        if lon1 < lon2:

            # print("lon1 smaller than lon2")
            # lat1 bigger than lat2
            within_lat = [city for city in cities if lat1 > city.lat > lat2]
            # lon1 smaller than lon2
            within_lon_too = [
                city for city in within_lat if lon1 < city.lon < lon2]

        else:

            # print("lon1 bigger than lon2")
            # lat1 bigger than lat2
            within_lat = [city for city in cities if lat1 > city.lat > lat2]
            # lon1 bigger than lon2
            within_lon_too = [
                city for city in within_lat if lon1 > city.lon > lon2]

        # TODO Ensure that the lat and lon valuse are all floats
        # Go through each city and check to see if it falls within
        # the specified coordinates.

    return within_lon_too


# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120

print(cityreader_stretch(45, -100, 32, -120, cities))
