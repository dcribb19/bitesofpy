from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    data = data.splitlines()
    tup_list = []
    # remove headers
    data.pop(0)
    for line in data:
        line = line.split(',')
        first_name = line[1]
        last_name = line[0]
        country = line[2]
        name = first_name + ' ' + last_name
        tup_list.append((country, name))
    
    for country, name in tup_list:
        countries[country].append(name)

    return countries
    