from flask import Flask,jsonify
from flask_cors import CORS, cross_origin
import champion_data as champion_data
import data
import json
import random
champions = data.champions
app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/champion_stats')
def champion_stats():
    name = champions[random.randint(0, 158)]
    icon_url = 'http://ddragon.leagueoflegends.com/cdn/12.13.1/img/champion/'+name+'.png'
    return jsonify({
        'Name': champion_data.getChampionName(name),
        'Gender': champion_data.getChampionGender(name),
        'Range type': champion_data.getChampionRangeType(name),        
        'Release date': champion_data.getChampionReleaseDate(name),
        'Positions': champion_data.getChampionPositions(name),
        'Species': champion_data.getChampionSpecies(name),
        'Regions': champion_data.getChampionRegions(name),
        'IconURL': icon_url
    })



if __name__ == '__main__':
    app.run(port=80)

