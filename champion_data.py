import db
def getChampionName(name):
    champion_name = {"championName": 1, "_id": 0}
    result_champion_name = db.mycol.find_one({"championName": name}, champion_name)
    champion_name = result_champion_name['championName']
    return champion_name

def getChampionGender(name):
    gender_querry = {"gender": 1, "_id": 0}
    result_gender = db.mycol.find_one({"championName": name}, gender_querry)
    if result_gender['gender'] == "M":
        result_gender = "Male"
    elif result_gender['gender'] == "F":
        result_gender = "Female"
    else:
        result_gender = "Other"
    return result_gender

def getChampionReleaseDate(name):
    release_date_querry = {"release_date": 1, "_id": 0}
    result_release_date = db.mycol.find_one({"championName": name}, release_date_querry)
    release_date = (result_release_date['release_date'])[0:4]
    return release_date

def getChampionRangeType(name):
    range_type_querry = {"range_type": 1, "_id": 0}
    result_range_type = db.mycol.find_one({"championName": name}, range_type_querry)
    range_type = result_range_type['range_type']
    return range_type

def getChampionPositions(name):
    positions = []
    positions_querry = {"positions": 1, "_id": 0}
    result_positions = db.mycol.find_one({"championName": name}, positions_querry)
    for x in range(len(result_positions['positions'])):
        positions.append(result_positions['positions'][x])
    return positions

def getChampionRegions(name):
    regions = []
    regions_querry = {"regions": 1, "_id": 0}
    result_regions = db.mycol.find_one({"championName": name}, regions_querry)
    for x in range(len(result_regions['regions'])):
        regions.append(result_regions['regions'][x])
    return regions

def getChampionSpecies(name):
    species = []
    species_querry = {"originalSpecies": 1, "_id": 0}
    result_species = db.mycol.find_one({"championName": name}, species_querry)
    for x in range(len(result_species['originalSpecies'])):
        species.append(result_species['originalSpecies'][x])
    return species
 



# http://ddragon.leagueoflegends.com/cdn/12.13.1/img/champion/Aatrox.png

