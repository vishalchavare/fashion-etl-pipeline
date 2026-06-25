🚀 ETL Pipeline Project (Python Data Engineering)

A production-style ETL (Extract, Transform, Load) pipeline built using Python that scrapes fashion product data, cleans and transforms it, and loads it into multiple destinations for analytics and reporting.

📌 Project Overview

This project demonstrates a complete end-to-end Data Engineering ETL pipeline:

Extracts fashion product data from a web source
Cleans and transforms raw, messy data into structured format
Loads processed data into multiple storage systems

It simulates real-world data pipeline workflows used in analytics and BI systems.

⚙️ Tech Stack
Python 🐍
Pandas 📊
BeautifulSoup 🌐
Requests
SQLAlchemy
PostgreSQL 🐘
Google Sheets API
dotenv
🔄 ETL Workflow
1️⃣ Extract (Data Collection)

Scrapes product data from:

https://fashion-studio.dicoding.dev/
Extracted fields:
Product Title
Price
Rating
Colors
Size
Gender
Timestamp
2️⃣ Transform (Data Cleaning & Processing)
Remove invalid records:
Unknown Product
Invalid ratings
Unavailable prices
Remove duplicates and null values
Convert data types properly:
Price → float (standardized)
Rating → numeric
Colors → integer
Normalize structured dataset using Pandas
3️⃣ Load (Data Storage)

Cleaned data is stored in:

📁 CSV file (fashion_product.csv)
📊 Google Sheets (via API integration)
🐘 PostgreSQL database
📂 Project Structure
.
├── main.py
├── requirements.txt
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
├── fashion_product.csv
└── README.md
🚀 How to Run This Project
1. Clone Repository
git clone https://github.com/vishalchavare/fashion-etl-pipeline.git
cd fashion-etl-pipeline
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create .env file:

SPREADSHEET_ID=your_google_sheet_id
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
5. Run ETL Pipeline
python main.py
6. Run Tests
pytest tests/ -v
📊 Output

After successful execution:

Clean dataset saved in CSV
Data pushed to Google Sheets
Data stored in PostgreSQL database
Fully tested ETL pipeline (pytest coverage included)
💡 Key Learnings
Web scraping using BeautifulSoup
Data cleaning & preprocessing with Pandas
ETL pipeline design
Database integration using SQLAlchemy
Google Sheets API automation
Real-world data engineering workflow
🏆 Highlights
Production-style ETL architecture
Multi-destination data loading
Clean modular Python code
Test-driven development (pytest)
Real-world data pipeline simulation
📌 Author

Vishal Chavare
📍 Pune, India
🔗 GitHub: https://github.com/vishalchavare
