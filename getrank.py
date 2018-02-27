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
    date = result[0]

    pipe_line2 = [
            {
                '$group':{
                    '_id':'$user_id',
                    'total_score':{'$sum':'$score'},
                    'total_time':{'$sum':'$submit_time'}
                    },
                '$match':{
                    '$or':[
                        {'total_score':{'$gt':data['total_score']}},
                        {'total_time':{}}
                        ]
                    }

            },

    return rank, score, submit_time

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Parameter Error")
        exit()
    usr_id = int(sys.argv[1])
    pint(get_rank(usr_id))
