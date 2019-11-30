import sys
import os
import csv
import http.client
import json


data_dir = './data'


def get_restaurant_info():
    """
    get image_url phone, price for restaurants
    """
    key = sys.argv[1]
    client = http.client.HTTPSConnection('api.yelp.com', timeout=100)
    header = {
        'Authorization': 'Bearer ' + key
    }
    st = 184500
    with open(os.path.join(data_dir, 'business.csv'), 'r', encoding='utf-16') as f1:
        with open(os.path.join(data_dir, 'restaurant_info_%d.csv' % st), 'w') as f2:
            writer = csv.writer(f2)
            writer.writerow(['business_id', 'image_url', 'phone', 'price'])
            reader = csv.reader(f1)
            next(reader)
            for i, line in enumerate(reader):
                if i + 1 <= st:
                    continue
                if 'Restaurants' in line[1] or 'Food' in line[1]:
                    business_id = line[0]
                    client.request('GET', '/v3/businesses/' + business_id, headers=header)
                    response = client.getresponse().read()
                    response = json.loads(response.decode('utf-8'))
                    image_url = response['image_url'] if 'image_url' in response.keys() else ''
                    phone = response['display_phone'] if 'display_phone' in response.keys() else ''
                    price = response['price'] if 'price' in response.keys() else ''
                    if 'image_url' not in response:
                        print(response)
                    print(i + 1, business_id)
                    writer.writerow([business_id, image_url, phone, price])


def get_restaurant_business_id():
    business_ids = []
    with open(os.path.join(data_dir, 'business.csv'), 'r', encoding='utf-16') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            if 'Restaurants' in line[1] or 'Food' in line[1]:
                business_ids.append(line[0])
    with open(os.path.join(data_dir, 'restaurant_business_id.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['business_id'])
        for business_id in business_ids:
            writer.writerow([business_id])


if __name__ == '__main__':
    get_restaurant_info()
    # get_restaurant_business_id()
