# Author(s): Niharika Prasad


# Acessing the reddit api

import pandas as pd
import praw
import datetime as dt
from psaw import PushshiftAPI


def get_reddit(search_word):
    reddit = praw.Reddit(client_id="**",  # my client id
                         client_secret="**",  # your client secret
                         user_agent="Niharika Prasad",  # user agent name
                         username="**",  # your reddit username
                         password="")  # your reddit password

    api = PushshiftAPI()

    start_time = int(dt.datetime(2010, 1, 1).timestamp())
    end_time = int(dt.datetime(2021, 1, 1).timestamp())

    list_ = list(api.search_submissions(after=start_time, before=end_time, subreddit=search_word,
                                        filter=['url', 'author', 'title', 'subreddit']))
    df = pd.DataFrame(list_)
    df.to_csv(f'{search_word}_reddit.csv')


get_reddit('Disney')
get_reddit('Pepsi')
get_reddit('American Airlines')


##########################################################################################
##########################################################################################
##########################################################################################

query = 'Disney'

reddit = praw.Reddit(client_id="jYeVrY-WQPdk-bR4WLdoxA",  # my client id
                     client_secret="ozDKmaQQ_Q6q8sC8tkVWHxO2XQ9olg",  # your client secret
                     user_agent="Niharika Prasad",  # user agent name
                     username="niharikap24",  # your reddit username
                     password="")  # your reddit password

api = PushshiftAPI()

start_time = int(dt.datetime(2010, 1, 1).timestamp())
end_time = int(dt.datetime(2021, 1, 1).timestamp())

list_pep = list(api.search_submissions(after=start_time, before=end_time, subreddit='Pepsi',
                                       filter=['url', 'created_utc', 'author', 'title', 'subreddit']))
df_pep = pd.DataFrame(list_pep)

df2 = pd.DataFrame(list_pep)
df1 = pd.DataFrame(list_pep)
df = pd.DataFrame(list_pep)
df.to_csv(f'{query}_reddit.csv')
df3 = pd.DataFrame()
df3 = df.append(df2)

pep_reddit = pd.read_csv('pep_reddit.csv')
