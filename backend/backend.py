from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import csv
import ast
import random


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

filename = './api_new.csv'
data = []
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for line in readCSV:
        if line[0] == 'img':
            continue
        data.append(line)


popular_reviews = ["Love this spot! Cheap, tasty Chinese food is hard to come by. The couple that runs the place is extremely nice  and a pleasure to interact with. They are cash only so be advised that you can't pay with a card. I highly recommend the General Tso chicken combo and the crab Rangoon, which is enough food for my girlfriend and I to split and still have leftovers.",
                   """THIS LADY IS SO LOUD- So please be prepared. She doesnt mean it, she just speaks very loud. She's also VERY inquisitive (meaning she will ask you a bunch of questions and talk you to death until you ignore her). She's a sweet heart tho :) . Her and her husband run the place, yes- just them so be patient. 
The interior is old, but she keeps it spotless. The carpet is ancient, but there isnt a spec of dust on it.

It's ok to eat inside, we did. Park in the front or the back and go thru the kitchen.

The food is pretty decent. There are the basic american dishes and a few  more authentic things. I have a hard time finding mushu pork with real pancakes when im out for Chinese- but they have it.

Tofu and Shrimp- is amazing. It has a kick of peppers and garlic in a heavy dark sauce with small diced and semi soft tofu and medium shrimp. The sauce and tofu over white rice was the stuff of dreams.
MuShu Pork- really good, i wish they gave me more pancakes.
General Tso's chicken- superb. The crunchy crispy coating was thin so you still got the bite of the chicken instead of batter. It was coated beautifully with a sweet but equally spicy sauce and served along side steamed broccoli that was the perfect al dente.

Soups were just okay for me.

But ill definitly come back.""",
                   "Came in on a Friday and the place was completely dead we were the only people there so able to get a table right away. The egg rolls are actually pretty big compared to most Chinese restaurants and they were nice and crispy, not soggy at all. I got the Hong Kong chow mein and they give you a big plate that is more than enough for 1 person. The chicken was cooked perfectly, again, not soggy like most Chinese places. The noodles were cooked just right and when we were all said and done our meal was only 11 dollars. I think this place is well worth the price and so far the best Chinese place I have found in the Dearborn area.",
                   """
Share review

Embed review

Compliment

Send message

Follow Liz P.

	12/11/2016
 3 photos

 2 check-ins

This place was definitely interesting. It's a hole in the wall in Dearborn, and has one waitress (Li) and her husband, I believe, who is the cook.

There's parking in the back and it's in kind of a dark alleyway. My boyfriend used to frequent this place, and he said that Li is always very kind to him and whomever he brings with him to dinner.

Prices ranged from $10-13ish for dinner but portions are GINORMOUS. A dinner plate could probably feed like 3-4 people. I had the cashew chicken and he had the General Tso's, and they also came with egg rolls (mostly veggie, but with some shrimp - unfortunately, since I don't like seafood), a big bowl of wonton soup, some bread, and some crispy wontons.

My cashew chicken was very good, and also came with shrimp fried rice (again, if you like shrimp, this is the place for you, LOL). Li also gave us some Chinese tea to go as well as an almond cookie and a fortune cookie each.

Be aware this place is *cash only*, too. The decor is definitely '70s/'80s-ish, but I liked it; I guess Kong Kow has been around since then.

The bathrooms are also very teeny (very narrow) but were clean. The food was delicious so I'd definitely come back here when in the area.

""",
                   """Gave this place a try the other night.  Haven't found a great Chinese restaurant around Dearborn.  Most are just adequate and this one is just a bit better.  Interesting place, though.  Small store front place that could probably seat 30 in a pinch.  They have an extensive menu as do most Chinese places.  Egg rolls were good and actually had shrimp in them.  Service was good and was friendly.  The place is very clean and orderly inside.  The wife had broccoli chicken.  The broccoli was not cooked enough so that it was a bit crunchy.  I had shrimp egg foo young.  It was loaded with shrimp!  Overall, I give it a C+.  The search continues.""",
                   """Ugh. Bland bland bland.

Thursday evening, 6:30pm, the place is empty, but the girl wanted to check it out.

Egg drop soup: bland! Like goopy nothingness with a few whisks of egg suspended stiffly mid-goop. The... crackers? wafers? oily crispy broken room-temperature... mini-chips / somethings: again, bland. Not a hint of salt or seafood flavoring... nada.

Sweet and Sour chicken: literally the smell of the reddish orangish goop burned my nose like ammonia. I wish I were joking. The breading was crisp with good texture and color, but as benign flavor-wise as the napkin in your lap. Same with the chicken! What, did they do, run everything in their kitchen thru a chemical process to strip it of flavor?

The shrimp-fried rice was a welcomed mediocre respite of the main dish with a light flavor of soy sauce having been used to fry the rice.

Spring rolls: great texture, came piping hot, and were appropriately flavored in what I would call a very mild (vegetably) way. The egg roll was probably the best thing in the table, it gets 3 stars for being average.

Fortune cookie No. 1: no fortune! No. 2: fortune cookie as meaningless as they come: "Aspiring man all around you. Keep close advice."

The water was cold and had no taste (in this case in a good way!). The place looked clean up front, home/family-run in the back, and the tiny lady's room was clean.

The server was watching Chinese soaps and spoke in very broken English -- and VERY LOUD! Her giant fake smile was obviously turned back to a "i-hate-my-life" grimace before she fully turned round. She made my little girl giggle. I think she might be hard of hearing, I mean this lady Yelled! Weird thing tho, the TV was not commensurately loud. Maybe she just enjoys SHOUTING at customers.  

The kid "loved it", eating pretty much an Entire quarter cup of fried rice and two whole bites of a spring roll -- but two broken-apart sweet-n-stale cookies. The cookies! The cookies had flavor! 2 stars for the cookie.

You couldn't drag me back into it his place, sorry.""",
                   """Old-school but fresh flavors, in a drab part of Detroit.

Parking is pretty easy on a weekday.  Cash only, so plan ahead (luckily I had enough.)  Prices are low enough that it's not a big deal.

It's small inside but comfy, cozy, not cramped.  The owner is super friendly, and asks and answers questions readily.  I went with a lunch portion of Szechuan chicken, which was in a flavorful sauce with plenty of veggies.  The chicken was good, but in such big chunks/slices that I had to cut them apart, and the sauce really didn't penetrate to flavor the meat well.  I asked for hot and I would say it was medium not- made me sweat but not uncontrollably.  

The egg roll and egg drop were standard, good not great.  The fried rice was the darkest I've ever seen, and pretty tasty.  My photo is blurry but shows them well enough...

I should try my standards, and their specialties, next time I'm in Detroit.  If you're already there, check it out."""]


# sanity check route
@app.route('/totalItems', methods=['GET'])
def total_items():
    global data
    forChinese = request.args.get('forChinese')
    forChinese = True if (forChinese == 'true') else False
    keywords = request.args.get('keywords')
    filter = request.args.get('filter')
    print(forChinese, keywords, filter)

    if forChinese:
        data = sorted(data, key=lambda x: x[1], reverse=True)
    else:
        data = sorted(data, key=lambda x: x[2], reverse=True)

    key = keywords.split()
    print(key)
    tmp_out = data
    for item in key:
        tmp_data = []
        for datam in tmp_out:
            if item.lower() in datam[5].lower():
                tmp_data.append(datam)
        tmp_out = tmp_data

    filter = ast.literal_eval(filter)
    matching = {'img': 0, 'rating_Chinese': 1, 'rating': 2, 'numReviews': 3, 'price': 4, 'name': 5, 'type': 6,
                'address': 7, 'business_id': 8, 'categories': 9, 'phone': 10}

    if not (filter['category'] == [] and filter['price'] == [] and filter['rating'] == []):
        tmp_data = []
        for datam in tmp_out:
            scores = []
            answers = []
            if filter['category'] != []:
                answers.append(1)
                for word in filter['category']:
                    if word in datam[matching['categories']]:
                        scores.append(1)
            else:
                answers.append(0)
            if filter['price'] != []:
                answers.append(1)
                for price in filter['price']:
                    if len(datam[matching['price']]) == price:
                        scores.append(1)
            else:
                answers.append(0)
            if filter['rating'] != []:
                answers.append(1)
                for rating in filter['rating']:
                    rating = rating.split('-')
                    min, max = int(rating[0]), int(rating[1])
                    if forChinese and (min <= float(datam[matching['rating_Chinese']])) and (float(datam[matching['rating_Chinese']]) <= max):
                        scores.append(1)
                    if (not forChinese) and (min <= float(datam[matching['rating']])) and (float(datam[matching['rating']]) <= max):
                        scores.append(1)
            else:
                answers.append(0)
            if sum(scores) == sum(answers):
                tmp_data.append(datam)

        tmp_out = tmp_data

    res = ['img', 'rating_Chinese', 'rating', 'numReviews', 'cost', 'name', 'type', 'address', 'business_id',
           'categories', 'phone']

    results = []
    for i, tmp in enumerate(tmp_out):
        result = {
            'img': tmp[matching['img']],
            'rank': i + 1,
            'rating': float('%.1f' % (float(tmp[matching['rating_Chinese']] if forChinese else tmp[matching['rating']]))),
            'numReviews': int(float(tmp[matching['numReviews']])),
            'cost': tmp[matching['price']].count('$'),
            'name': tmp[matching['name']],
            'type': ','.join(tmp[matching['categories']].split(';')),
            'phone': tmp[matching['phone']],
            'neighborhood': 'Downtown',
            'popularReviews': [random.choice(popular_reviews)[:700] + "..."]
        }
        results.append(result)
    return jsonify(results)


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
