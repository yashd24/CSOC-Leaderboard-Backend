import redis
from redis.commands.json.path import Path
import json

r = redis.Redis()

def updateUserScore(username,round,score):

    if round ==11:
        points = 10
    elif round==21:
        points = 20
    elif round==22 and score!=0:
        points = 30
    elif round==31:
        points = 40

    if round != 11:
        data = json.loads(r.get(username))      #deserializes into json format converts into dict
        data['score'] = points
        data['round'] = round
        r.set(username,json.dumps(data))        #converts dict to json and updates the database

    # else:

    return 'success'


