from datetime import datetime
from . import db

class StockPrice(db.Model):
    __tablename__ = 'stock_prices'
    
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.BigInteger)

    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'date': self.date.isoformat(),
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume
        }
