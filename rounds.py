from flask import Flask
import json,requests

def riddle_ans(string):
    
    return str(string.split('-')[1])



def check_forked(username,repo):
    url = f"https;//github.com/{username}/{repo}"             #username = glugmvit, repo = yet to be created
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        is_forked = data.get('fork', False)
        return is_forked
    print("error in check forked")
    return False



def Rounds(request):
    
    if 'forkee' in request.keys():
        return 11

    elif 'issue' in request.keys():
        riddle_answer=[]
        if riddle_ans(str(request['comment']['body'])) in riddle_answer:
            return 21
        else:
            return 22               #pending {analyse the algo}
    
    elif check_forked('glugmvit','repo'):
        return 31



