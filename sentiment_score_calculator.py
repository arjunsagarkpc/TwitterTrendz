import string
import re
import csv
from afinn import Afinn

def get_and_process_tweets():

    hashtag_list = ['HT1.csv', 'HT2.csv', 'HT3.csv', 'HT4.csv', 'HT5.csv']
    print ("hashtag_list is", repr(hashtag_list))
    ss_list = []
    
    for tag in hashtag_list:
        
        with open(tag, "r") as csv_file:

            my_csv = csv.reader(csv_file, delimiter=',')
            afinn = Afinn()

            sum_scores = 0
            tweet_count = 0
            processed_tweet_list = []
            sentiment_list = []
            
            for row in my_csv:
                
                tweet = row[7]
                tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|#[A-Za-z0-9]|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

                date = row[1]
                user = row[2]

                score = afinn.score(tweet)

                sentiment_dict = {}
                       
                sentiment_dict['Date'] = date
                sentiment_dict['User'] = '@' + user
                sentiment_dict['Tweet'] = tweet
                sentiment_dict['Score'] = score
                
                sentiment_list.append(sentiment_dict)

                            
            del(sentiment_list[0])
            ss_list.append(sentiment_list)

    #print(ss_list)
    ss_list1 = ss_list[0]
    ss_list2 = ss_list[1]
    #ss_list3 = ss_list[2]
    ss_list4 = ss_list[3]
    ss_list5 = ss_list[4]
    ss_list = ss_list[0] + ss_list[1] + ss_list[2] + ss_list[3] + ss_list[4]
    #print(len(ss_list))
    return(ss_list)

#get_and_process_tweets()
        
