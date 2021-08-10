# Portfolio_Metrics
You will be able to calculate an optimal portfolio to invest.

First of all, you need to download the Metrics_lib.py that is in my repository.
I added a database of the NASDAQ stocks in .csv for the code.

I cleaned the database based on technical analysis (RSI, Stoch) and financial analysis (Sharpe ratio, Treynor ratio, P/B).
It let you standardize the data and then group by clusters (4 clusters is the standard quantity but you can change it).
For clustering I based the algorithim in "Elbow Method".
The clustering will be used two times.

You need to select the optimal cluster based on the mean of each cluster.
Once the optimal cluster is selected, the prices will be downloaded and the portfolio metrics will be created.

Also, you need to be sure about the composite in the lines, it will depend of the database you will use.

Thanks for using this code.
