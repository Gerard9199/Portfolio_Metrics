import yfinance as yf
import pandas as pd
import numpy as np
import pandas as pd
from datetime import date
import Metrics

Risk_Free_Rate = float(input("Enter the risk free rate: "))
Year = int(input("Enter the years to calculate: "))
today = date.today()
start = today.replace(year=today.year - Year)
Shares = []
composite = '^IXIC' #composite for nasdaq database
data = pd.read_csv('C:/xampp/csv/dataset_github.csv')
data = data.loc[(data['RSI'] > 20) & (data['RSI']< 90) & (data['STOCH'] > 10) & (data['STOCH']< 90) & (data['SHARPE'] < 10) & (data['SHARPE']> 0) & (data['TREYNOR'] > 0) & (data['TREYNOR']< 80) & (data['P/VL'] > 0) & (data['P/VL']< 3.1)]
df = Metrics.standardization(data)
df = Metrics.clustering(df)
n = data.shape[1]
data.insert(n, "CLUSTERS",df['CLUSTERS'])
print("CLUSTERS:")
print(data['CLUSTERS'].value_counts())
means = data.groupby('CLUSTERS').mean()
print(means)
k = int(input("Enter the optimal cluster: "))
selected = data[data['CLUSTERS'] == k]
portfolio = Metrics.standardization(selected)
portfolio = Metrics.clustering(portfolio)
selected = selected.drop(['CLUSTERS'], axis=1)
n = selected.shape[1]
selected.insert(n, "CLUSTERS", portfolio['CLUSTERS'])
print("CLUSTERS:")
print(selected['CLUSTERS'].value_counts())
means = selected.groupby('CLUSTERS').mean()
print(means)
k = int(input("Enter the optimal cluster: "))
selected_portfolio = selected[selected['CLUSTERS'] == k]
portfolio = (np.random.choice(selected_portfolio['TICKER'], 5, replace=False)).tolist()
prices = yf.download(portfolio, start = start, end = today, interval="1d" )['Adj Close']
prices[composite] = yf.download(composite, start = start, end = today, interval="1d" )['Adj Close']
Last_price = yf.download(portfolio, today)['Adj Close']
prices = prices.fillna(method='bfill')
prices = prices.fillna(prices.mean())
prices, portfolio = Metrics.null_portfolio(prices, portfolio, selected_portfolio)
print("PORTFOLIO")
print(portfolio)
for i in range(0, len(portfolio)):
            n = int(input("Enter the quantity of shares for {} ".format(portfolio[i])))
            Shares.append(n)
Ponderation, Average_Daily_Return, Portfolio_Daily_Risk, Portfolio_Annual_Return, Portfolio_Annual_Risk = Metrics.risk(portfolio, composite, prices, Last_price, Risk_Free_Rate, sum(Shares), Year)
print(f"Portfolio Annual Return: {round((float(Metrics.cleaner(Portfolio_Annual_Return)) * 100),2)}%")
print(f"Portfolio Daily Risk: {round((float(Metrics.cleaner(Portfolio_Daily_Risk)) * 100),2)}%")
print(f"Portfolio Annual Risk: {round((float(Metrics.cleaner(Portfolio_Annual_Risk)) * 100),2)}%")

