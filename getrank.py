# /usr/bin/env python3
import sys
from pymongo import MongoClient

def get_rank(usr_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    pipe_line1 = [
            {'$match':{'user_id':usr_id}},
            {
                '$group':{
                    '_id':'$user_id',
                    'total_score': {'$sum':'$score'},
                    'total_time':{'$sum':'$submit_time'}
                 }
            }
    ]
    result = list(db.contests.aggregate(pipe_line1))
    if(len(result) == 0):
        return 0, 0, 0
    data = result[0]

    pipe_line2 = [
            {
                '$group':{
                    '_id':'$user_id',
                    'total_score':{'$sum':'$score'},
                    'total_time':{'$sum':'$submit_time'}
                    }
            },
            {
                '$match':{
                    '$or':[
                        {'total_score':{'$gt':data['total_score']}},
                        {
                            'total_score':data['total_score'],
                            'total_time':{'$lt':data['total_time']}
                        }]
                    }
            },
            {
                '$group':{
                        '_id':None,
                        'count':{'$sum':1}
                        }
            }]
    result = list(db.contests.aggregate(pipe_line2))
    if len(result) == 0:
        rank = 1
    else:
        rank = result[0]['count'] + 1
    return rank, data['total_score'], data['total_time']

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Parameter Error")
        exit()
    usr_id = int(sys.argv[1])
    print(get_rank(usr_id))
