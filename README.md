
# **NepsePredictor**

> **A Stock Market Prediction System Based on NEPSE**
> *Semester Project – Learning Stock Analysis and Machine Learning*

[![Project Status](https://img.shields.io/badge/Status-Developing-brightgreen)]()
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)]()

---

##  NepsePredictor

**NepsePredictor** is a full-stack web app to predict stock prices based on the Nepal Stock Exchange (NEPSE). The system utilizes technologies such as **data scraping**, **machine learning models**, and **interactive visualizations** to provide users with insightful stock market predictions and trends.

```
nepse-stock-predictor/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── database.py
│   ├── scraper.py
│   ├── ml_pipeline.py
│   ├── routes/
│   │   └── api.py
│   ├── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components/
│   │   │   └── PredictionChart.js
│   │   ├── services/
│   │   │   └── api.js
│   ├── package.json
│
├── .env
├── README.md
```

## Features
- **Data Scraping**: Automatically fetches stock data from NEPSE using Python's `requests` and `BeautifulSoup4`.
- **Database Integration**: Stores and manages stock data using PostgreSQL or MySQL with SQLAlchemy ORM.
- **Machine Learning**: Predicts stock prices using scikit-learn and TensorFlow/Keras models.
- **Data Visualization**: Displays predictions in an interactive chart using React and Chart.js.
- **API**: Provides RESTful endpoints for frontend-backend communication using Flask.
- **Scheduling**: Automates data scraping and model training using cron jobs or Task Scheduler.
- **Testing**: Ensures code quality with `pytest` for the backend and `Jest` + `React Testing Library` for the frontend.


## Installation and Setup

### Prerequisites
- Python 3.8+
- Node.js and npm
- PostgreSQL or MySQL
- Git

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/prabinbessie/NepsePredictor.git
   cd nepse-stock-predictor/backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the `.env` file with your database credentials and other configurations.

5. Run the Flask application:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```

### Database Setup
1. Create a PostgreSQL or MySQL database.
2. Update the `.env` file with the database connection string.
3. Run the database migrations (if applicable).

### Running Tests
- **Backend**:
  ```bash
  pytest
  ```
- **Frontend**:
  ```bash
  npm test
  ```



## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.