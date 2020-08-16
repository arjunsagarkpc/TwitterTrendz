from flask import Flask, Markup, render_template
import pandas as pd
import json

from sentiment_score_calculator import get_and_process_tweets

final_list = get_and_process_tweets()
#print(len(final_list))

list_values = [val for d in final_list for val in d.values()]
list_values = list_values[::-4]

#json_list = []
#for x in range(len(list_values)):
    #json_list.append([x,list_values[x]])

json_list = [[x,list_values[x]] for x in  range(len(list_values))]
#print(json_list)

df_json = pd.DataFrame(json_list)
#print(df_json.head(10))
#df_json.to_json("static/data/sentiment_score.json")


with open('static/data/sentiment_score.json', 'w') as F:
    F.write(json.dumps(json_list))




col_series = pd.Series(['variable 1','variable 2', 'variable 3', 'variable 4', 'variable 5'])
col_series = col_series.repeat(500)

df = pd.DataFrame(data={"type":col_series,"value": list_values})
df.to_csv("static/data/sentiment_score.csv", sep=',',index=False)


from twitter_trends import list_of_hashtags
hash_list = list_of_hashtags()

print ("hash_list is", repr(hash_list))

hash_dict={}
hash_dict['variable 1'] = hash_list[0]
hash_dict['variable 2'] = hash_list[1]
hash_dict['variable 3'] = hash_list[2]
hash_dict['variable 4'] = hash_list[3]
hash_dict['variable 5'] = hash_list[4]

print(hash_dict)


strng=json.dumps(hash_dict)




app = Flask(__name__)


@app.route('/sentiment')

def bar():
    
    return render_template('index.html', result = strng)

@app.route('/live')

def live():
    
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

