# NepsePredictor
NepsePredictor is a full-stack application designed to predict stock prices for the Nepal Stock Exchange (NEPSE). It leverages modern technologies for data scraping, machine learning, and visualization to provide users with accurate and insightful stock predictions.

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

## Overall Tech Stack
| Layer              | Technology / Library                          |
|--------------------|-----------------------------------------------|
| **Data Scraping**  | Python 3.8+, requests, BeautifulSoup4         |
| **Database**       | PostgreSQL (or MySQL)                         |
| **Backend / API**  | Python + Flask                                |
| **ML / Modeling**  | scikit-learn, TensorFlow/Keras                |
| **Data Processing**| pandas, NumPy                                 |
| **Scheduling**     | cron (Linux) or Task Scheduler (Windows)      |
| **Frontend**       | React (create-react-app) + Chart.js           |
| **Testing**        | pytest (backend), Jest + React Testing Library|
| **Version Control**|       GitHub                                  |

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