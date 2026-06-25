# 🚀 ETL Pipeline Project (Python Data Engineering)

A production-style **ETL (Extract, Transform, Load) pipeline** built using Python that scrapes fashion product data, cleans and transforms it, and loads it into multiple destinations for analytics and reporting.

---

## 📌 Project Overview

This project demonstrates a complete end-to-end **Data Engineering ETL pipeline**:

- Extracts fashion product data from a web source  
- Cleans and transforms raw messy data into structured format  
- Loads processed data into multiple storage systems  
- Creates analytics-ready dataset for reporting & BI tools  

It simulates real-world data engineering workflows used in production systems.

---

## ⚙️ Tech Stack

- Python 🐍  
- Pandas 📊  
- BeautifulSoup 🌐  
- Requests  
- SQLAlchemy  
- PostgreSQL 🐘  
- Google Sheets API  
- python-dotenv  
- pytest 🧪  

---

## 🔄 ETL Workflow

### 1️⃣ Extract (Data Collection)

- Scrapes product data from:
  https://fashion-studio.dicoding.dev/

**Extracted Fields:**
- Product Title  
- Price  
- Rating  
- Colors  
- Size  
- Gender  
- Timestamp  

---

### 2️⃣ Transform (Data Cleaning & Processing)

- Remove invalid records:
  - Unknown products  
  - Invalid ratings  
  - Missing prices  
- Remove duplicates  
- Handle null values  
- Convert data types:
  - Price → float  
  - Rating → float  
  - Colors → integer  
- Clean and normalize dataset using Pandas  

---

### 3️⃣ Load (Data Storage)

Cleaned data is loaded into multiple destinations:

- 📁 CSV file → `fashion_product.csv`  
- 📊 Google Sheets (API integration)  
- 🐘 PostgreSQL database  

---

## 📂 Project Structure
.
├── main.py
├── requirements.txt
├── .env
├── fashion_product.csv
├── service_account.json
│
├── utils/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── tests/
│ └── test_etl.py
│
└── README.md



---

## 🚀 How to Run This Project

### 1. Clone Repository
```bash
git clone https://github.com/vishalchavare/fashion-etl-pipeline.git
cd fashion-etl-pipeline

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SPREADSHEET_ID=your_google_sheet_id
5. Add Google Credentials

Place your service account file:

service_account.json
6. Run ETL Pipeline
python main.py
7. Run Tests
pytest tests/ -v
📊 Output

After successful execution:

✅ Clean dataset saved as CSV
📊 Data uploaded to Google Sheets
🐘 Data stored in PostgreSQL
🧪 Tests executed successfully

📌 Features
End-to-end ETL pipeline
Web scraping automation
Data cleaning & preprocessing
Multi-destination loading
Modular Python architecture
Environment-based configuration
Test-driven development
💡 Key Learnings
Web scraping using BeautifulSoup
Data cleaning using Pandas
ETL pipeline design
SQL database integration (PostgreSQL)
Google Sheets API automation
Real-world data engineering workflow
🏆 Highlights
Production-style ETL architecture
Scalable modular design
Multi-output pipeline (CSV + DB + Sheets)
Real-world project simulation
Resume-ready project
👨‍💻 Author

Vishal Chavare
📍 Pune, India
🔗 GitHub: https://github.com/vishalchavare

⭐ Support

If you like this project, give it a ⭐ on GitHub 🚀
