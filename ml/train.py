import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib
from ta import add_all_ta_features

def load_data():
    files = glob.glob('data/processed/*.csv')
    df = pd.concat([pd.read_csv(f) for f in files])
    return df.dropna()

def create_features(df):
    df = add_all_ta_features(df, 
                            open="open", high="high", low="low", 
                            close="close", volume="volume")
    return df.dropna()

def train_model():
    df = load_data()
    df = create_features(df)
    
    X = df.drop(['close', 'date', 'symbol'], axis=1)
    y = df['close']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'ml/models/linear_regression.pkl')
    
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"Model trained with RMSE: {rmse:.2f}")

if __name__ == "__main__":
    train_model()