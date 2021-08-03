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
CAGR = (vstack_data.iloc[-1] / vstack_data.iloc[0])**(1/10.5) - 1  # In Fraction
print('CAGR Percentage', CAGR*100)

# Twitter
pep = pd.read_csv('tweets/pep.csv')
assessment = pep['tweet'].apply(lambda x: TextBlob(x).sentiment_assessments)
pep['sentiment_polarity'] = assessment.apply(lambda x: x[0])
pep['sentiment_subjectivity'] = assessment.apply(lambda x: x[1])
pep['sentiment_assessment'] = assessment.apply(lambda x: x[2])

pep_sent = pep[['created_at', 'tweet', 'language', 'sentiment_polarity', 'sentiment_subjectivity', 'sentiment_assessment']]
pep_sent = pep_sent[pep_sent['language'] == 'en']
pep_sent = pep_sent[(pep_sent['sentiment_polarity'] != 0) & (pep_sent['sentiment_subjectivity'] != 0)]
pep_sent.to_csv('pep_sent.csv', index=None)
