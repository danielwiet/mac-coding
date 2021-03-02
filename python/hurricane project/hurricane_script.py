# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# Deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:

def damages_as_nums(my_list):
    # create conversion rate and empty list
    conversion = {'M': 1000000, 'B': 1000000000}
    updated_damages = []

    # loop through the list
    for damage in damages:
        if 'Damages' in damage:
            updated_damages.append(damage)
        # check if the sting has an M or B in the last index, and if so, remove, mult by conversion, and convert to float
        elif damage[-1] == 'M':
            updated_damages.append(float(damage.strip('M')) * conversion['M'])
        else:
            updated_damages.append(float(damage.strip('B')) * conversion['B'])
    return updated_damages

# call the function and store 
updated_damages = damages_as_nums(damages)
print(updated_damages)
# print(len(damages))
# print(len(updated_damages))


# write your construct hurricane dictionary function here:

def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages):

    hurricanes = {}

    for i in range(len(names)):
        hurricanes[names[i]] = {
            'Name': names[i],
            'Months': months[i],
            'Years': years[i],
            'Max Sustained Winds': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damages': updated_damages[i],
            'Deaths': deaths[i]
        }

    return hurricanes


# call the function and store in variable
hurricanes = hurricane_dictionary(
    names, months, years, max_sustained_winds, areas_affected, updated_damages)

#since it is a dictionary, we can specify what key we want to return values for
print(hurricanes)

# write your construct hurricane by year dictionary function here:

def hurricanes_by_year():
    # create empty dictionary
    year_dict = {}
    # iterate through each year in the years list
    for year in years:
        # for each instance of a year, it becomes the key value, and uses the values from the hurricanes dictionary if and when the 'Years' key value matches the year (in years)
        year_dict[year] = [
            hurricane for hurricane in hurricanes.values() if hurricane["Years"] == year]
    return year_dict

# call the function and store in a variable 
year_dictionary = hurricanes_by_year()
print(year_dictionary[2005])

# write your count affected areas function here:

def count_areas_affected():
    # create an empty list
    count_of_areas_affected = {}

    # loop through the area_affected dictionary
    for area in areas_affected:
        # loop through each element in the dictionary
        for i in area:
            # conditional to check if an area is in count_of_areas_affected. if not, set the key at index i to 1
            if i not in count_of_areas_affected:
                count_of_areas_affected[i] = 1
            # if i is in count_of_areas_affected, add 1 to the value of the key at index i
            else:
                count_of_areas_affected[i] += 1
    return count_of_areas_affected

count_of_areas_affected = count_areas_affected()
print(count_of_areas_affected)


# write your find most affected area function here:

def most_affected():
    values = list(count_of_areas_affected.values())
    keys = list(count_of_areas_affected.keys())
    
    highest_key = keys[values.index(max(values))]
    highest_key_value = values[values.index(max(values))]

    return highest_key, highest_key_value

area_with_highest_count = most_affected()
print(area_with_highest_count)
print('The area that has been most affected over the years by damaging hurricanes is {}. It has been hit {} times.'.format(area_with_highest_count[0], area_with_highest_count[1]))


# write your greatest number of Damages function here:

def greatest_num_deaths():
    # create base variables to compare values to
    deadliest_hurricane = ''
    deadliest_hurricane_count = 0

    # loop through the key(hurricane_name) and the values(stats) in the hurricane dictionary(as list using the .items() method)
    for hurricane_name, stats in hurricanes.items():
        # specify which substat you want to look at using the substat's subkey name
        if stats['Deaths'] > deadliest_hurricane_count:
            deadliest_hurricane_count = stats['Deaths']
            deadliest_hurricane = hurricane_name
    return deadliest_hurricane, deadliest_hurricane_count

deadliest_hurricane = greatest_num_deaths()
print("The deadliest hurrican on record is {} with {} fatalities attributed to the hurricane.".format(deadliest_hurricane[0], deadliest_hurricane[1]))
            

# write your catgeorize by damage_scale function here:

def categorize_by_death():
    
    damage_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

    damage_dict = {}

    damage_dict[0] = [hurricane for hurricane in hurricanes.values() if hurricane['Deaths'] == damage_scale[0]]
    damage_dict[1] = [hurricane for hurricane in hurricanes.values() if damage_scale[0] < hurricane['Deaths'] <= damage_scale[1]]
    damage_dict[2] = [hurricane for hurricane in hurricanes.values() if damage_scale[1] < hurricane['Deaths'] <= damage_scale[2]]
    damage_dict[3] = [hurricane for hurricane in hurricanes.values() if damage_scale[2] < hurricane['Deaths'] <= damage_scale[3]]
    damage_dict[4] = [hurricane for hurricane in hurricanes.values() if damage_scale[3] < hurricane['Deaths'] <= damage_scale[4]]
    damage_dict[5] = [hurricane for hurricane in hurricanes.values() if damage_scale[4] < hurricane['Deaths']]

    return damage_dict

hurricane_scale_by_death = categorize_by_death()
print(hurricane_scale_by_death[0])

# write your greatest damage function here:

def greatest_damage():
    # create base variables to compare values to
    costliest_hurricane = ''
    costliest_hurricane_amount = 0

    # loop through the key(hurricane_name) and the values(stats) in the hurricane dictionary(as list using the .items() method)
    for hurricane_name, stats in hurricanes.items():
        # specify which substat you want to look at using the substat's subkey name
        if stats['Damages'] == 'Damages not recorded':
            continue
        else:
            if stats['Damages'] > costliest_hurricane_amount:
                costliest_hurricane_amount = stats['Damages']
                costliest_hurricane = hurricane_name
    return costliest_hurricane, costliest_hurricane_amount

most_expensive = greatest_damage()
print('Hurricane {} was the most expensive hurricane with an estimated cost of ${:.2f}'.format(most_expensive[0], most_expensive[1]))


# write your catgeorize by damage function here:

def categorize_by_damage():
    damage_scale = {
        0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000
    }
                
    damage_dict = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }

    for hurricane, stats in hurricanes.items():
        if stats['Damages'] == 'Damages not recorded':
            continue
        else:
            if stats['Damages'] == damage_scale[0]:
                damage_dict[0].append(hurricane)
            if damage_scale[0] < stats['Damages'] <= damage_scale[1]:
                damage_dict[1].append(hurricane)
            if damage_scale[1] < stats['Damages'] <= damage_scale[2]:
                damage_dict[2].append(hurricane)
            if damage_scale[2] < stats['Damages'] <= damage_scale[3]:
                damage_dict[3].append(hurricane)
            if damage_scale[3] < stats['Damages'] <= damage_scale[4]:
                damage_dict[4].append(hurricane)
            if damage_scale[4] < stats['Damages']:
                damage_dict[5].append(hurricane)

    return damage_dict

hurricane_scale_by_damage = categorize_by_damage()
print(hurricane_scale_by_damage)