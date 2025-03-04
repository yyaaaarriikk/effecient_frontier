import numpy as np
import datetime as dt
import yfinance as yf

# import data

# getData імпортує дані з Yahoo Finance
def getData(stocks, start, end):
    stockData = yf.download(stocks, start=start, end= end)
    stockData = stockData['Close']

# обчислюємо статисктику
# meanReturns - середній дохід
# covMatrix - матриця коваріації(відношення однієї акції до іншої)
# pct_change() - обчислюємо зміну відсотків
# mean() - обчислюємо середнє значення
# cov() - обчислюємо коваріацію
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()

    return meanReturns, covMatrix


def portfolioPerfomance(weights, meanReturns, covMatrix):
    # формула річного доходу
    returns = np.sum(meanReturns*weights)*252
    # формула річної волатильності
    std = np.sqrt( np.dot(weights.T, np.dot(covMatrix, weights)) ) * np.sqrt(252)
    # зберігає результати(повертає їх)
    return returns, std

stockList = ['AAPL', 'TSLA', 'META', 'AMZN', 'MSFT']
stocks = stockList

# date range(діапазон дат)
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365)

weights = np.array([0.2, 0.2, 0.1, 0.2, 0.3])

# присовюємо значення функцій getData та portfolioPerfomance
meanReturns, covMatrix = getData(stocks, start=startDate, end=endDate)
returns, std = portfolioPerfomance(weights, meanReturns, covMatrix)

# вивід результатів у %
print(round(returns*100,2), round(std*100,2))