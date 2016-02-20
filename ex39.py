# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)


# study drill 1
# create a mapping of province to abbreviation
provinces = {
    'Zhejiang': 'ZJ',
    'Shaanxi': 'SX',
    'Anhui': 'AH',
    'Jiangsu': 'JS',
    'Jiangxi': 'JX'
}

# create a basic set of provinces and some cities in them
cities = {
    'ZJ': 'Wenzhou',
    'SX': 'Xi\'an',
    'AH': 'Hefei'
}

# add some more cities
cities['JS'] = 'Soochow'
cities['JX'] = 'Nanchang'

# print out some cities
print("ZJ Province has:", cities['ZJ'])
print("SX Province has:", cities['SX'])

# print some province
print("Zhejiang's abbreviation is: ", provinces['Zhejiang'])
print("Shaanxi's abbreviation is: ", provinces['Shaanxi'])

# do it by using the province then cities dict
print("Zhejiang has: ", cities[provinces['Zhejiang']])
print("Shaanxi has: ", cities[provinces['Shaanxi']])

# print every province's abbreviation
for province, abbrev in provinces.items():
    print("%s is abbreviated %s" % (province, abbrev))

# print every city in province
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
for province, abbrev in provinces.items():
    print("%s province is abbreviated %s and has city %s" % (
        province, abbrev, cities[abbrev]))

# safely get a abbreviation by province that might not be there
province = provinces.get('Guangdong')

if not province:
    print("Sorry, no Guangdong.")

# get a city with a default value
city = cities.get('GD', 'Does Not Exist')
print("The city for the province 'GD' is: %s" % city)
