import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_percentage_error, mean_absolute_error, root_mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler

# data imported
train_df = pd.read_csv('train.csv')

# drop any rows with empty values
train_df = train_df.dropna(how='any')

# convert acres to sqft
train_df.loc[train_df['lot_size_units'] == 'acre', 'lot_size'] =\
    train_df.loc[train_df['lot_size_units'] == 'acre', 'lot_size'].mul(43560)

# drop redundant columns
train_df = train_df.drop(['lot_size_units', 'size_units', 'zip_code', 'lot_size'], axis=1)

# Data exploration
# corr_matrix = train_df.corr()
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".1f")
# plt.show()
#
# plt.scatter(train_df['size'], train_df['price'])
# plt.title('Scatter Plot')
# plt.xlabel('Size')
# plt.ylabel('Price')
# plt.show()
#
# plt.scatter(train_df['beds'], train_df['price'])
# plt.title('Scatter Plot')
# plt.xlabel('Bedrooms')
# plt.ylabel('Price')
# plt.show()
#
# plt.scatter(train_df['baths'], train_df['price'])
# plt.title('Scatter Plot')
# plt.xlabel('Bathrooms')
# plt.ylabel('Price')
# plt.show()

# outlier handling
min_beds = train_df['beds'].min()
max_beds = train_df['beds'].max()
min_baths = train_df['baths'].min()
max_baths = train_df['baths'].max()
min_size = train_df['size'].min()
max_size = train_df['size'].max()
min_price = train_df['price'].min()
max_price = train_df['price'].max()

outlier_index = train_df[train_df['price'] == max_price].index
train_df = train_df.drop(outlier_index)

outlier_index = train_df[train_df['beds'] == max_beds].index
train_df = train_df.drop(outlier_index)

max_beds = train_df['beds'].max()
outlier_index = train_df[train_df['beds'] == max_beds].index
train_df = train_df.drop(outlier_index)

max_beds = train_df['beds'].max()
outlier_index = train_df[train_df['beds'] == max_beds].index
train_df = train_df.drop(outlier_index)

max_baths = train_df['baths'].max()
outlier_index = train_df[train_df['baths'] == max_baths].index
train_df = train_df.drop(outlier_index)

size_outlier_condition = (train_df['price'] == 6250000) & (train_df['beds'] == 2)
outlier_index = (train_df[size_outlier_condition]).index
train_df = train_df.drop(outlier_index)

# data inspection
# print("beds:")
# max_beds = train_df['beds'].max()
# print(min_beds)
# print(max_beds)
#
# print("baths")
# print(min_baths)
# print(max_baths)
#
# max_size = train_df['size'].max()
# print("size")
# print(min_size)
# print(max_size)
#
# max_price = train_df['price'].max()
#
# print("price")
# print(min_price)
# print(max_price)
#
# print("price")
# max_price = train_df['price'].max()
# print(min_price)
# print(max_price)

# Data exploration
# corr_matrix = train_df.corr()
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".1f")
# plt.show()
#
# plt.scatter(train_df['size'], train_df['price'])
# plt.title('Scatter Plot')
# plt.xlabel('Size')
# plt.ylabel('Price')
# plt.show()
#
# plt.scatter(train_df['beds'], train_df['price'])
# plt.title('Scatter Plot')
# plt.xlabel('Bedrooms')
# plt.ylabel('Price')
# plt.show()
#
# plt.scatter(train_df['baths'], train_df['price'])
# plt.title('Scatter Plot')
# plt.xlabel('Bathrooms')
# plt.ylabel('Price')
# plt.show()

'''
FITTING
'''
# fit model

y = train_df.price
training_features = ['beds', 'baths', 'size']
X = train_df[training_features]
seattle_model = DecisionTreeRegressor(random_state=1, splitter='best', max_depth=9, min_samples_split=8)

# test data

test_df = pd.read_csv('test.csv')
test_df = test_df.dropna()
test_df.loc[test_df['lot_size_units'] == 'acre', 'lot_size'] =\
    test_df.loc[test_df['lot_size_units'] == 'acre', 'lot_size'].mul(43560)
test_df = test_df.drop(['lot_size_units', 'size_units', 'zip_code', 'lot_size'], axis=1)
X_test = test_df[training_features]

seattle_model.fit(X, y)
predicted_prices = seattle_model.predict(X_test)
y_test = test_df['price']

# mape = mean_absolute_percentage_error(y_test, predicted_prices)
# r2 = r2_score(y_test, predicted_prices)
# mae = mean_absolute_error(y_test, predicted_prices)
# rmse = root_mean_squared_error(y_test, predicted_prices)
# print("R^2:", r2)
# print("MAPE:", mape * 100)
# print("MAE:", mae)
# print("RMSE", rmse)

flag = False

while not flag:
    beds = int(input('Enter the number of bedrooms, bathrooms, and size in square footage of the house below. '
                     '\nBedrooms: '))
    baths = float(input('Bathrooms: '))
    size = int(input('Size (sqft): '))
    prediction_features = pd.DataFrame([[beds, baths, size]], columns=training_features)
    price_prediction = seattle_model.predict(prediction_features)
    formatted_price = "{:.2f}".format(price_prediction[0])
    print(formatted_price)
    session_state = str(input('Would you like to make another estimate? (Yes or No): '))
    if session_state.lower() == 'no':
        flag = True
