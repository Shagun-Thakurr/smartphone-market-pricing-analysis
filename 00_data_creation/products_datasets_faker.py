# Phase 1: Data Generation
# Target: Create raw datasets for Apple and Samsung (CSV)



import pandas as pd
import random
import numpy as np
from faker import Faker

fake = Faker()

apple_models = [
    "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15",
    "iPhone 13 Pro", "iPhone 14 Pro"
]

samsung_models = [
    "Galaxy S21", "Galaxy S22", "Galaxy S23",
    "Galaxy A52", "Galaxy A72", "Galaxy Z Flip"
]

regions = ["Asia", "Europe", "North America", "South America"]
channels = ["Online", "Offline", "Retail Store"]

def add_missing_values(df, missing_percent=0.08):
    cols_to_null = [
        "Price_INR", "Cost_INR", "Profit_INR",
        "Storage_GB", "RAM_GB", "Battery_mAh",
        "Rating", "Screen_Size_Inch",
        "Country", "Discount_Percent"
    ]
    
    for col in cols_to_null:
        df.loc[df.sample(frac=missing_percent).index, col] = np.nan
    return df

def generate_apple_data(rows=500):
    data = []
    for _ in range(rows):
        price = random.randint(60000, 150000)
        cost = random.randint(40000, price - 5000)

        data.append({
            "Brand": "Apple",
            "Model": random.choice(apple_models),
            "Price_INR": price,
            "Cost_INR": cost,
            "Profit_INR": price - cost,
            "Storage_GB": random.choice([64, 128, 256, 512]),
            "RAM_GB": random.choice([4, 6, 8]),
            "Battery_mAh": random.randint(2800, 4500),
            "Screen_Size_Inch": round(random.uniform(5.8, 6.7), 1),
            "Camera_MP": random.choice([12, 48]),
            "Rating": round(random.uniform(3.8, 5.0), 1),
            "Reviews_Count": random.randint(500, 20000),
            "Units_Sold": random.randint(5000, 500000),
            "Sales_Channel": random.choice(channels),
            "Region": random.choice(regions),
            "Country": fake.country(),
            "Launch_Date": fake.date_between(start_date="-4y", end_date="today"),
            "Warranty_Years": random.choice([1, 2]),
            "Discount_Percent": random.randint(0, 25),
            "Return_Rate_Percent": round(random.uniform(1.0, 8.0), 2)
        })
    df = pd.DataFrame(data)
    return add_missing_values(df)

def generate_samsung_data(rows=500):
    data = []
    for _ in range(rows):
        price = random.randint(30000, 120000)
        cost = random.randint(20000, price - 4000)

        data.append({
            "Brand": "Samsung",
            "Model": random.choice(samsung_models),
            "Price_INR": price,
            "Cost_INR": cost,
            "Profit_INR": price - cost,
            "Storage_GB": random.choice([64, 128, 256, 512]),
            "RAM_GB": random.choice([6, 8, 12]),
            "Battery_mAh": random.randint(3500, 6000),
            "Screen_Size_Inch": round(random.uniform(6.1, 6.9), 1),
            "Camera_MP": random.choice([50, 64, 108]),
            "Rating": round(random.uniform(3.5, 5.0), 1),
            "Reviews_Count": random.randint(800, 30000),
            "Units_Sold": random.randint(5000, 600000),
            "Sales_Channel": random.choice(channels),
            "Region": random.choice(regions),
            "Country": fake.country(),
            "Launch_Date": fake.date_between(start_date="-4y", end_date="today"),
            "Warranty_Years": random.choice([1, 2]),
            "Discount_Percent": random.randint(5, 40),
            "Return_Rate_Percent": round(random.uniform(1.5, 10.0), 2)
        })
    df = pd.DataFrame(data)
    return add_missing_values(df)


apple_df = generate_apple_data()
samsung_df = generate_samsung_data()


apple_df.to_csv("apple_phones_data.csv", index=False)
samsung_df.to_csv("samsung_phones_data.csv", index=False)

apple_df.shape, samsung_df.shape
