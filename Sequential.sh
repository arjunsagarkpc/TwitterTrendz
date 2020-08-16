MYVAR=`python3 twitter_trends.py | tr -d '[],'`
echo $MYVAR

arr=($MYVAR)

echo ${arr[0]}
python3 GetOldTweets3.py --querysearch "${arr[0]}" --lang en --maxtweets 500
python3 -c 'from Create import copy_csv1;copy_csv1()'

echo ${arr[1]}
python3 GetOldTweets3.py --querysearch "${arr[1]}" --lang en --maxtweets 500
python3 -c 'from Create import copy_csv2;copy_csv2()'

echo ${arr[2]}
python3 GetOldTweets3.py --querysearch "${arr[2]}" --lang en --maxtweets 500
python3 -c 'from Create import copy_csv3;copy_csv3()'

echo ${arr[3]}
python3 GetOldTweets3.py --querysearch "${arr[3]}" --lang en --maxtweets 500
python3 -c 'from Create import copy_csv4;copy_csv4()'

echo ${arr[4]}
python3 GetOldTweets3.py --querysearch "${arr[4]}" --lang en --maxtweets 500
python3 -c 'from Create import copy_csv5;copy_csv5()'
