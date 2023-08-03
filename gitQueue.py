import json
from rounds import *
from challenge import *
from dbms import updateUserScore

def addData(request):
    request=json.loads(request)
    username=request['sender']['login']
    round=Rounds(request)

    status = 'none'

    if round == 11:
        score = Pull_req()
        status = updateUserScore(username, round, score)
        return status
    
    elif round == 21:
        score = Round2(round)
        status = updateUserScore(username, round, score)
        return status
    
    elif round == 22:
        score = Round2(round)
        status = updateUserScore(username, round, score)
        return status
    
    elif round == 21:
        score = Round2(round)
        status = updateUserScore(username, round, score)
        return status
    
    return status

