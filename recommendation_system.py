import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM


#fetch data and format it
data = fetch_movielens(min_rating=4.0)

#print training ant testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFM(loss='warp')
#train model
#model.fit(data['train'], epochs=30, num_treads=2)
model.fit(data['train'], epochs=30)


def sample_recommendation(model, data, user_ids):

    n_users, n_items = data['train'].shape

    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[
            user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]

        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)


sample_recommendation(model, data, [3, 25, 450])
