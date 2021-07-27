# scrape_reddit.py
# Author(s): Niharika Prasad

import praw
import datetime as dt
from psaw import PushshiftAPI

query = 'Disney'

reddit = praw.Reddit(client_id="jYeVrY-WQPdk-bR4WLdoxA",  # my client id
                     client_secret="ozDKmaQQ_Q6q8sC8tkVWHxO2XQ9olg",  # your client secret
                     user_agent="Niharika Prasad",  # user agent name
                     username="niharikap24",  # your reddit username
                     password="")  # your reddit password

api = PushshiftAPI()

start_time = int(dt.datetime(2015, 1, 1).timestamp())
end_time = int(dt.datetime(2017, 1, 1).timestamp())

list_ = list(api.search_submissions(after=start_time, before=end_time, subreddit=query,
                                    filter=['url','author', 'title', 'subreddit']))

df = pd.DataFrame(list_)
df.to_csv(f'{query}_reddit.csv')
