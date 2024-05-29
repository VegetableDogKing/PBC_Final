import pandas as pd
from sklearn.linear_model import LinearRegression

def clothes(high, low):
    temp = [[high, low]]
    
    data = pd.read_csv('up.csv')
    X = data.iloc[:, :-1].values
    Y = data.iloc[:, -1].values
    model = LinearRegression()
    model.fit(X, Y)
    up_pred = model.predict(temp)

    if up_pred < 16:
        data = pd.read_csv('down.csv')
        X = data.iloc[:, :-1].values
        Y = data.iloc[:, -1].values
        model = LinearRegression()
        model.fit(X, Y)
        down_pred = model.predict(temp)
    else:
        down_pred = 0
    
    data = pd.read_csv('shoes.csv')
    X = data.iloc[:, :-1].values
    Y = data.iloc[:, -1].values
    model = LinearRegression()
    model.fit(X, Y)
    shoes_pred = model.predict(temp)

    return int(up_pred[0]), int(down_pred[0]), int(shoes_pred[0])