import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import pandas as pd
import logging
from datetime import datetime, timedelta
from typing import List, Dict

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class NepseScraper:
    def __init__(self):
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        
    def fetch_symbols(self) -> Dict[str, str]:
        """Fetch symbols with company names"""
        try:
            response = self.session.get("https://www.sharesansar.com/company-list", timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'lxml')
            
            symbols = {}
            table = soup.find('table', {'class': 'table'})
            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                if len(cols) >= 3:
                    symbol = cols[1].text.strip()
                    name = cols[2].text.strip()
                    symbols[symbol] = name
            logger.info(f"Fetched {len(symbols)} symbols")
            return symbols
        except Exception as e:
            logger.error(f"Symbol fetch failed: {str(e)}")
            raise

    def fetch_historical_data(self, symbol: str, days: int = 365) -> pd.DataFrame:
        """Fetch historical data from Sharesansar API"""
        try:
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
            
            url = f"https://www.sharesansar.com/ajaxcompanystockgraph/{symbol}"
            params = {
                'fromdate': start_date,
                'todate': end_date,
                'isinno': 'undefined'
            }
            
            response = self.session.get(url, params=params, timeout=20)
            response.raise_for_status()
            
            data = response.json()
            if not data.get('success'):
                logger.error(f"API error for {symbol}: {data.get('message')}")
                return pd.DataFrame()
            
            df = pd.DataFrame(data['data'])
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.rename(columns={
                'Date': 'date',
                'Open Price': 'open',
                'High Price': 'high',
                'Low Price': 'low',
                'Close Price': 'close',
                'Total Traded Quantity': 'volume'
            })
            df['symbol'] = symbol
            return df[['date', 'symbol', 'open', 'high', 'low', 'close', 'volume']]
        except Exception as e:
            logger.error(f"Historical data fetch failed for {symbol}: {str(e)}")
            return pd.DataFrame()

    def fetch_all_data(self, symbols: Dict[str, str]) -> pd.DataFrame:
        """Batch fetch data with parallel processing"""
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        dfs = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(self.fetch_historical_data, symbol): symbol 
                      for symbol in symbols.keys()}
            
            for future in as_completed(futures):
                symbol = futures[future]
                try:
                    result = future.result()
                    if not result.empty:
                        dfs.append(result)
                        logger.info(f"Successfully fetched {symbol}")
                    else:
                        logger.warning(f"No data for {symbol}")
                except Exception as e:
                    logger.error(f"Error processing {symbol}: {str(e)}")
        
        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
