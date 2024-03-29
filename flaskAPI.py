import math
import csv
from flask import Flask, jsonify, request, abort
import json
import requests
app = Flask(__name__)

def distance(xi,xii,yi,yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

@app.route("/api/hello")
def hello_world():
    return "Hello, World!"

@app.route("/api/getlonglat", methods = ['GET'])
def getlonglat():
    address = request.args.get('address', None)
    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'sensor': 'false',
        'region': 'us'
    }
   # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']

    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']

    lat = geodata['lat']
    lng = geodata['lng']

    return json.dumps({'latituted': lat, 'longitude': lng})



@app.route("/api/nearby", methods = ['GET'])
def nearby():
    longitude = float(request.args.get('longitude', None))
    latituted = float(request.args.get('latituted', None))
    if longitude is None or latituted is None:
        abort(404)
    close1 = None
    close2 = None
    close3 = None
    shortDistance1 = 3000000000000
    shortDistance2 = 3000000000000
    shortDistance3 = 3000000000000
    with open('foodpantrydata.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            if (row[0] != 'Latitude'):
                floatLat = float(row[0])
                floatLong = float(row[1])
                thisDistance = distance(latituted, floatLat, longitude, floatLong)
                if thisDistance < shortDistance1:
                    shortDistance3 = shortDistance2
                    shortDistance2 = shortDistance1
                    shortDistance1 = thisDistance
                    close3 = close2
                    close2 = close1
                    close1 = row
                elif thisDistance < shortDistance2:
                    shortDistance3 = shortDistance2
                    shortDistance2 = thisDistance
                    close3 = close2
                    close2 = row
                elif thisDistance < shortDistance3:
                    shortDistance3 = thisDistance
                    close3 = row
    if close1 is None or close2 is None or close3 is None:
        return json.dumps({'Locations':'Error, None found within range.'})

    return json.dumps({'Locations': [{'Longitude': close1[0], 'Latitude': close1[1], 'Name': close1[2], 'Address': close1[3] + ', ' + close1[4] + ', ' + close1[5] + ' ' + close1[6]}, {'Longitude': close2[0], 'Latitude': close2[1], 'Name': close2[2], 'Address': close2[3] + ', ' + close2[4] + ', ' + close2[5] + ' ' + close2[6]}, {'Longitude': close3[0], 'Latitude': close3[1], 'Name': close3[2], 'Address': close3[3] + ', ' + close3[4] + ', ' + close3[5] + ' ' + close3[6]}]})

@app.route("/api/nearbyfood", methods = ['GET'])
def nearbyfood():
    address = request.args.get('address', None)
    if address is None:
        abort(404)
    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'sensor': 'false',
        'region': 'us'
    }
    counter = 0
    while True:
        try:
            # Do the request and get the response data
            req = requests.get(GOOGLE_MAPS_API_URL, params=params)
            res = req.json()

            # Use the first result
            result = res['results'][0]
            break
        except IndexError:
            print("Google failed to respond")
            if counter > 10:
                abort(404)
            counter += 1


    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']

    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']

    lat = geodata['lat']
    lng = geodata['lng']

    print(str(lat) + ', ' + str(lng))

    longitude = float(lat)
    latituted = float(lng)
    close1 = None
    close2 = None
    close3 = None
    shortDistance1 = 3000000000000
    shortDistance2 = 3000000000000
    shortDistance3 = 3000000000000
    with open('foodpantrydata.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            if (row[0] != 'Latitude'):
                floatLat = float(row[0])
                floatLong = float(row[1])
                thisDistance = distance(latituted, floatLat, longitude, floatLong)
                if thisDistance < shortDistance1:
                    shortDistance3 = shortDistance2
                    shortDistance2 = shortDistance1
                    shortDistance1 = thisDistance
                    close3 = close2
                    close2 = close1
                    close1 = row
                elif thisDistance < shortDistance2:
                    shortDistance3 = shortDistance2
                    shortDistance2 = thisDistance
                    close3 = close2
                    close2 = row
                elif thisDistance < shortDistance3:
                    shortDistance3 = thisDistance
                    close3 = row
    if close1 is None or close2 is None or close3 is None:
        return json.dumps({'Locations':'Error, None found within range.'})

    return json.dumps({'Locations': [{'Longitude': close1[0], 'Latitude': close1[1], 'Name': close1[2], 'Address': close1[3] + ', ' + close1[4] + ', ' + close1[5] + ' ' + close1[6]}, {'Longitude': close2[0], 'Latitude': close2[1], 'Name': close2[2], 'Address': close2[3] + ', ' + close2[4] + ', ' + close2[5] + ' ' + close2[6]}, {'Longitude': close3[0], 'Latitude': close3[1], 'Name': close3[2], 'Address': close3[3] + ', ' + close3[4] + ', ' + close3[5] + ' ' + close3[6]}]})
