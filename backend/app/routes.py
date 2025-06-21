import glob
import pandas as pd
from .models import StockPrice
from . import db
from datetime import datetime

def ingest_raw_csvs(pattern="data/raw/*.csv"):
    files = glob.glob(pattern)
    for fp in files:
        df = pd.read_csv(fp, parse_dates=['date'])
        records = []
        for _, row in df.iterrows():
            records.append(
                StockPrice(
                    symbol=row['symbol'],
                    date=row['date'].date(),
                    open=row['open'],
                    high=row['high'],
                    low=row['low'],
                    close=row['close'],
                    volume=int(row['volume'])
                )
            )
        if records:
            db.session.bulk_save_objects(records)
            db.session.commit()
