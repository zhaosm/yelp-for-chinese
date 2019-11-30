from flask import Flask, jsonify, request
from flask_cors import CORS
import time


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/totalItems', methods=['GET'])
def ping_pong():
    time.sleep(5)
    forChinese = request.args.get('forChinese')
    if forChinese == 'true':
        totalItems = [{
              'img': 'https://s3-media0.fl.yelpcdn.com/bphoto/hd7Ith2Gm3QnrQqOzI_JvA/ls.jpg',
              'rank': i + 1,
              'rating': 4.5,
              'numReviews': 3019,
              'cost': 2,
              'name': 'Poor Calvin\'s',
              'type': 'Asian Fusion, Southern, Comfort Food',
              'phone': '(404) 254-4051',
              'address': '510 Piedmont Ave NE',
              'neighborhood': 'Downtown',
              'popularReviews': ['“Amazing place! Took an off from work just to experience this place! It was so worth it! Amazing food. Tried \'The Beast\' sandwich and the \'shawrma platter\'.…”']
            } for i in range(101)]
    else:
        totalItems = [{
            'img': 'https://s3-media0.fl.yelpcdn.com/bphoto/_x61pM4WZiji4d2jq1GnYw/ls.jpg',
            'rank': i + 1,
            'rating': 5.0,
            'numReviews': 1433,
            'cost': 2,
            'name': 'Aviva by Kameel',
            'type': 'Mediterranean, Juice Bars & Smoothies, Middle Eastern',
            'phone': '(404) 698-3600',
            'address': '225 Peachtree St NE',
            'neighborhood': 'Downtown',
            'popularReviews': ['“Hubby and I were in town for the weekend from CA and wanted to try some yummy fried chicken so took to Yelp to search. Came across Gus\'s and was super happy…”']
            } for i in range(101)]
    return jsonify(totalItems)


if __name__ == '__main__':
    app.run()
