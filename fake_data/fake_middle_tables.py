from faker import Faker
import random

fake = Faker()

restaurants = ['ChIJNZloNTd-j4ARxGMOXZp7KfI',
                 'ChIJfcaly4eAhYARSIvvfFpH64w',
                 'ChIJlfC_eYKAhYARhcWC559q0jc',
                 'ChIJVRnYLHyAhYARhl2ZVJFi5iU',
                 'ChIJ5UiqQJCAhYAR5L5rAgjuf_0',
                 'ChIJKT_dq7GAhYARpHV3vs0HUWQ',
                 'ChIJMygdeCZ-j4ARKDtpQiICwUo',
                 'ChIJzf0lTbCAhYARqz-tqaIyJaY',
                 'ChIJh_24QJ-AhYAR_xbUNVN2Xns',
                 'ChIJk8dm4J6AhYAR8MCM6inxTgE']

dishes = ['Tea-Smoked Garlic Chicken',
            'Fire-Roasted Pepper & Mango Lamb',
            'Roasted Beets & Orange Tuna',
            'Pickled Sugar Pasta',
            'Pan-Fried Confit of Rice',
            'Gentle-Fried Blueberry & Mushroom Taco',
            'Melon and Cranberry Jam',
            'Mandarin and Banana Toast',
            'Kiwi Whip',
            'Lime Pastry']


for i in range(10):
    dish = dishes[i]
    dish_id = i + 1

    for j in range(10):
        review_id = random.randint(1,100)
        dish_comment = fake.paragraph()
        restaurant_id = random.choice(restaurants)

        print("""{}|{}|{}|{}|{}""".format(dish_id,
                                          dish,
                                          review_id,
                                          dish_comment,
                                          restaurant_id))