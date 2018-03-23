import json
import pandas as pd
import sys

def analysis(file, user_id):
    time = 0
    minutes = 0
    data = pd.read_json(file)
    times = len(data[data['user_id']==user_id])
    minutes =data[data['user_id']==user_id]['minutes'].sum()  #用minurs可以直接用 .minutes; 其实也可以直接用groupby函数
    return times, minutes


if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Parameter Error, not enough!")
        exit()
    file = sys.argv[1]
    try:
        user_id = int(sys.argv[2])
    except ValueError:
        print("Parameter Error")
        exit()
    print(analysis(file, user_id))
    
