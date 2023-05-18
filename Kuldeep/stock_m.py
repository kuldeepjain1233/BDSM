import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matlotlib inline

import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

data = pd.read_csv('C:/Users/cycob/Downloads/Google_train_data.csv')
# tesla.info()

data["Close"] = pd.to_numeric(data.Close, errors='coerce')
data = data.dropna()
trainData = data.iloc[:,4:5].values

sc = MinMaxScaler(feature_range=(0,1))
trainData = sc.fit_transform(trainData)
# print(trainData.shape)


x_train = []
y_train = []

for i in range(60, 1149):
    x_train.append(trainData[i-60:i,0])
    y_train.append(trainData[i,0])

x_train, y_train = np.array(x_train),np.array(y_train)

x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))


model = Sequential()

model.add(LSTM(units=100, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=100,return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=100,return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(units=1))
model.compile(optimizer='adam',loss="mean_squared_error")

hist = model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2)

testdata = pd.read_csv('C:/Users/cycob/Downloads/Google_test_data.csv')
testdata["Close"] = pd.to_numeric(testdata.Close, errors='coerce')
testdata = testdata.dropna()
testdata = testdata.iloc[:,4:5]
y_test = testdata.iloc[60:,0:].values

inputclosing = testdata.iloc[:,0:].values
inputclosing_scaled = sc.transform(inputclosing)
x_test = []
length = len(testdata)
timestep = 60
for i in range(timestep,length):
    x_test.append(inputclosing_scaled[i-timestep:i,0])
x_test = np.array(x_test)
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

test_pred = model.predict(x_test)

predicted_price = sc.inverse_transform(test_pred)

plt.plot(y_test, color = 'red',label='Actual Price')
plt.plot(predicted_price, color ='green', label='Predicted Price')
plt.title('Google stock price prediction')
plt.xlabel('Time')
plt.ylabel('Stock price')
plt.legend()
plt.show()














# tesla['Date'] = pd.to_datetime(tesla['Date'])

# layout = go.Layout(
#     title='Stock Prices of Tesla',
#     xaxis=dict(
#         title = 'Date',
#         titlefont=dict(
#             family='Courier New, monospace',
#             size=18,
#             color='#7f7f7f'
#         )
#     ),
#     yaxis=dict(
#         title='Price',
#         titlefont=dict(
#             family='courier New, monospace',
#             size = 18,
#             color = '#7f7f7f'
#         )
#     )
# )

# # tesla_data = [[]]

# x = np.array(tesla.index).reshape(-1,1)
# y = tesla['Close']
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=101)

# scaler = StandardScaler().fit(x_train)

# lm = LinearRegression()
# lm.fit(x_train,y_train)

# trace0 = go.Scatter(
#     x = x_train.T[0],
#     y = y_train,
#     mode = 'markers',
#     name = 'Actual'
# )

# trace1 = go.Scatter(
#     x = x_train.T[0],
#     y = lm.predict(x_train).T,
#     mode = 'lines',
#     name = 'Predicted'
# )

# tesla_data = [trace0,trace1]
# layout.xaxis.title.text = 'Day'
# plot2 = go.Figure(data=tesla_data, layout=layout)

# iplot(plot2)

# scores = f'''
# {'Metric'.ljust(10)}{'Train'.center(20)}{'Test'.center(20)}
# {'r2_score'.ljust(10)}{r2_score(y_train, lm.predict(x_train))}\t{r2_score(y_test, lm.predict(x_test))}
# {'MSE'.ljust(10)}{mse(y_train,lm.predict(x_train))}\t{mse(y_test,lm.predict(x_test))}
# '''
# print(scores)