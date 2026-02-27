USE product_analysis_db;

-- CHECKING ROWS
SELECT COUNT(*) FROM product_analysis;

select * from product_analysis;


-- HANDLING MISSING VALUES
SET SQL_SAFE_UPDATES = 0;

UPDATE product_analysis
SET Cost_INR = NULL
WHERE Cost_INR = 0;
UPDATE product_analysis SET Price_INR = NULL WHERE Price_INR = 0;
UPDATE product_analysis SET Battery_mAh = NULL WHERE Battery_mAh = 0;
UPDATE product_analysis SET Screen_Size_Inch = NULL WHERE Screen_Size_Inch = 0;
UPDATE product_analysis SET Rating = NULL WHERE Rating = 0;
UPDATE product_analysis SET RAM_GB = NULL WHERE RAM_GB = 0;
UPDATE product_analysis SET Storage_GB = NULL WHERE Storage_GB = 0;


-- FILLING MISSING VALUES WITH AVERAGE VALUES
UPDATE product_analysis 
JOIN (
    SELECT 
        AVG(Price_INR) AS avg_price,
        AVG(Cost_INR) AS avg_cost,
        AVG(Storage_GB) AS avg_storage,
        AVG(RAM_GB) AS avg_ram,
        AVG(Battery_mAh) AS avg_battery,
        AVG(Screen_Size_Inch) AS avg_screen,
        AVG(Rating) AS avg_rating
    FROM product_analysis
) avg_vals
SET 
    Price_INR = COALESCE(Price_INR, avg_vals.avg_price),
    Cost_INR = COALESCE(Cost_INR, avg_vals.avg_cost),
    Storage_GB = COALESCE(Storage_GB, avg_vals.avg_storage),
    RAM_GB = COALESCE(RAM_GB, avg_vals.avg_ram),
    Battery_mAh = COALESCE(Battery_mAh, avg_vals.avg_battery),
    Screen_Size_Inch = COALESCE(Screen_Size_Inch, avg_vals.avg_screen),
    Rating = COALESCE(Rating, avg_vals.avg_rating);

 -- FILLING PROFIT MISSING VALUES BY CALCULATING PRICE & COST INR   
UPDATE product_analysis
SET Profit_INR = Price_INR - Cost_INR;

-- CHECKING IF THERE IS STILL NULL VALUES OR NOT
SELECT 
    SUM(Price_INR IS NULL) AS price_nulls,
    SUM(Cost_INR IS NULL) AS cost_nulls,
    SUM(Profit_INR IS NULL) AS profit_nulls,
    SUM(Storage_GB IS NULL) AS storage_nulls,
    SUM(RAM_GB IS NULL) AS ram_nulls,
    SUM(Battery_mAh IS NULL) AS battery_nulls,
    SUM(Screen_Size_Inch IS NULL) AS screen_nulls,
    SUM(Rating IS NULL) AS rating_nulls
FROM product_analysis;
select * from product_analysis;


-- HANDLING DECIMAL VALUES
UPDATE product_analysis
SET 
    Price_INR = ROUND(Price_INR, 0),
    Cost_INR = ROUND(Cost_INR, 0),
    Screen_Size_Inch = ROUND(Screen_Size_Inch, 1),
    Rating = ROUND(Rating, 1);

UPDATE product_analysis
SET 
    Profit_INR = ROUND(Price_INR - Cost_INR, 0),
    Screen_Size_Inch = ROUND(Screen_Size_Inch, 1),
    Profit_Margin = ROUND((Profit_INR / Price_INR) * 100, 2);
    
UPDATE product_analysis
SET Battery_mAh = ROUND(Battery_mAh, 0);

select * from product_analysis;