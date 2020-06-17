my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']

def uncommon_cities(my_cities: list, other_cities: list):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    my_cities = set(my_cities)
    other_cities = set(other_cities)
    uncommon_cities = my_cities.symmetric_difference(other_cities)
    return len(uncommon_cities)