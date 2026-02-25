# Smartphone Market Intelligence & AI-Based Pricing Analysis


## Project Objective
 In this project, I set out to understand what drives smartphone pricing and how brand positioning influences profitability.
 Instead of using a ready-made dataset, I built a realistic market simulation myself and developed a complete analytics workflow — from data generation and ETL to machine learning and dashboard reporting.
 My goal was to combine technical execution with business reasoning.

## Data Engineering & ETL

* Generated 1,002 records (501 Apple, 501 Samsung) using Python + Faker.
* Loaded data from multiple sources (CSV, Excel, Text Input) to simulate real-world ingestion.
* Consolidated overlapping records using Pentaho.
* Removed duplicates and standardized structure.
* Final SQL dataset: **938 clean records**(Spoon).
* **Note on Brand Codes**:In all datasets and dashboards,0 refers to Apple (Premium) and 1 refers to Samsung (Mid-Range). This mapping was maintained throughout the Python, SQL, and Power BI workflows to ensure data integrity.
<img width="800" height="500" alt="ETL_pipeline_image" src="https://github.com/user-attachments/assets/182ce2a9-8590-4251-aaed-4e3ae11263da" />

***ETL pipeline built in Pentaho Spoon***

## Technical Workflow
1. ***Data Generation (Faker & Python)***-:I started by creating a custom dataset for Apple and Samsung using the Faker library in Python to simulate real-world market variety.

2. ***ETL Process (Spoon/Pentaho)***:-I performed the ETL (Extract, Transform, Load) process using Spoon. I combined different data sources using Text File Input, Excel Input, and Table Input to create one unified dataset.

3. ***Database Management (MYSQL)***:-I loaded the cleaned data into a SQL database as a table named product Analysis. I used SQL queries to handle missing data by filling in Average (AVG) values in the required columns to ensure data integrity.

4. ***Advanced Analysis (Jupyter Notebook)***:-I connected my Jupyter Notebook to the MYSQL database to import the table. From there, I completed the EDA, Hypothesis Testing, and Feature Engineering.

5. ***Machine Learning & Deployment***:-I built the Linear Regression model directly in Jupyter.This final model was then integrated into my Power BI Dashboard to provide the automated price predictions.


 ## Business Insights
**Using SQL and Python, I identified:**
* 84M simulated total revenue.
* 34.52% average profit margin.
* 8GB RAM + ~4200mAh battery as dominant configuration.
* **Strategic Brand Split**: I categorized the dataset into two primary segments to analyze different market behaviors. Brand 0 represents the Premium segment (averaging 103K INR), while Brand 1 represents the Mid-Range segment (averaging 75K INR).
## Predictive Modeling
* Built Linear Regression model.
* 80/20 train-test split.
* 37.49% prediction accuracy.

##  Dashboard & Visualization
***Developed an interactive Power BI dashboard to:***
* Compare Apple vs Samsung pricing strategies.
* Analyze revenue and profitability.
* Visualize hardware trends.
* Integrate ML-based price prediction.
***Focused on translating analysis into business-ready insights.***
<img width="900" height="500" alt="dashboard_image1" src="https://github.com/user-attachments/assets/5dc29878-e640-4be3-93f5-54dc5ec6ec4e" />
<img width="900" height="500" alt="dashboard_image2" src="https://github.com/user-attachments/assets/6d79b584-66ae-4fb1-89be-db2d10aecefa" />
<img width="900" height="500" alt="dashboard_image3" src="https://github.com/user-attachments/assets/fc08e47e-b987-45f8-b3c7-1cd8f59ececf" />

## Tools & Technologies

- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)  
- **MySQL**  
- **Pentaho (Spoon)** – ETL  
- **Jupyter Notebook**  
- **Power BI**

 ## Project Impact
  ***This project demonstrates the ability to design and execute a complete analytics pipeline — from multi-source data ingestion and ETL processing to predictive modeling and business visualization.
The work highlights strong data validation, analytical reasoning, and the translation of technical results into actionable pricing insights.***
