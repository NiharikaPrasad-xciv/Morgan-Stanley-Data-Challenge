# data_fetcher.py
# Author(s): Nitin Sharma

import logging
import yfinance
import pandas as pd


class DataFetcher:
    @staticmethod
    def fetch(tickers, start='2011-01-01', end='2021-06-30'):
        data = []
        for ticker in tickers:
            logging.debug(f'Fetching {ticker} data')
            df = yfinance.Ticker(ticker).history(start=start, end=end).reset_index()
            min_ = df['Close'].min()
            max_ = df['Close'].max()
            df['normalized'] = 100 * (df['Close'] - min_) / (max_ - min_)
            df['ticker'] = ticker
            data.append(df)
        data = pd.concat(data)
        return data
