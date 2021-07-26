# main.py
# Author(s): Nitin Sharma

from data_fetcher import DataFetcher
import pandas as pd
from textblob import TextBlob

data = DataFetcher.fetch(['AAL', 'DIS', 'PEP', '^GSPC'])
data['ticker'] = data['ticker'].str.replace('^GSPC', 'S&P 500', regex=False)
data.to_csv('data.csv', index=None)

vstack_data = data.pivot(index='Date', columns='ticker', values='Close')
vstack_data.columns.name = ''
print(vstack_data.corr()['S&P 500'])

# CAGR
CAGR = (vstack_data.iloc[-1] / vstack_data.iloc[0]) ** (1 / 10.5) - 1  # In Fraction
print('CAGR Percentage', CAGR * 100)

# Twitter
pep = pd.read_csv('tweets/pep.csv')
assessment = pep['tweet'].apply(lambda x: TextBlob(x).sentiment_assessments)
pep['sentiment_polarity'] = assessment.apply(lambda x: x[0])
pep['sentiment_subjectivity'] = assessment.apply(lambda x: x[1])
pep['sentiment_assessment'] = assessment.apply(lambda x: x[2])

pep_sent = pep[
    ['created_at', 'tweet', 'language', 'sentiment_polarity', 'sentiment_subjectivity', 'sentiment_assessment']]
pep_sent = pep_sent[pep_sent['language'] == 'en']
pep_sent = pep_sent[(pep_sent['sentiment_polarity'] != 0) & (pep_sent['sentiment_subjectivity'] != 0)]
pep_sent.to_csv('pep_sent.csv', index=None)


####
def add_csv(ticker):
    df = pd.read_csv(f'tweets/{ticker}.csv')
    print(len(df))
    df = df.append(pd.read_csv(f'tweets/{ticker}2.csv'))
    print(len(df))
    df = df.append(pd.read_csv(f'tweets/{ticker}3.csv'))
    print(len(df))
    df.to_csv(f'{ticker}_tweets.csv')
    return df


aal_tweets = add_csv('aal')
pep_tweets = add_csv('pepsi')
dis_tweets = add_csv('dis')

aal_tweets = aal_tweets.drop_duplicates(keep=False, inplace=True)
pep_tweets = pep_tweets.drop_duplicates(keep=False, inplace=True)
dis_tweets = dis_tweets.drop_duplicates(keep=False, inplace=True)


def sentiment_analysis(ticker_df, ticker):
    assessment = ticker_df['tweet'].astype(str).apply(lambda x: TextBlob(x).sentiment_assessments)
    ticker_df['sentiment_polarity'] = assessment.apply(lambda x: x[0])
    ticker_df['sentiment_subjectivity'] = assessment.apply(lambda x: x[1])
    ticker_df['sentiment_assessment'] = assessment.apply(lambda x: x[2])

    ticker_df_sent = ticker_df[
        ['created_at', 'tweet', 'language', 'sentiment_polarity', 'sentiment_subjectivity', 'sentiment_assessment']]
    ticker_df_sent = ticker_df_sent[ticker_df_sent['language'] == 'en']
    ticker_df_sent = ticker_df_sent[(pep_sent['sentiment_polarity'] != 0) & (pep_sent['sentiment_subjectivity'] != 0)]
    ticker_df_sent.to_csv(f'{ticker}_sent.csv', index=None)
    ticker_df_sent.groupby('created_at').describe()
    return ticker_df_sent


aal_tweets = pd.read_csv('aal_tweets.csv')
aal_tweet_analysis = sentiment_analysis(aal_tweets, 'aal')
pep_tweets = pd.read_csv('pepsi_tweets.csv')
pep_tweet_analysis = sentiment_analysis(pep_tweets, 'pep')
dis_tweets = pd.read_csv('dis_tweets.csv')
dis_tweet_analysis = sentiment_analysis(dis_tweets, 'dis')


def show_stats(df):
    df = df.groupby('created_at').des